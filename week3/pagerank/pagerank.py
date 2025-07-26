import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result = {}
    for k in corpus.keys():
        result[k] = 0
    page_set = corpus[page]
    if not page_set:
        page_set = set(corpus.keys())
    prob_for_each = damping_factor / len(page_set)
    prob_2 = (1 - damping_factor) / len(corpus)
    for page in page_set:
        result[page] += prob_for_each
    for k in corpus.keys():
        result[k] += prob_2
    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    choosen = []
    page_random_first_it = random.choice(list(corpus.keys()))
    choosen.append(page_random_first_it)
    result_first = transition_model(corpus,page_random_first_it,damping_factor)
    for i in range(n):
        x = random.choices(list(result_first.keys()), weights=list(result_first.values()), k = 1)[0]
        choosen.append(x)
        result_first = transition_model(corpus, x, damping_factor)
    final_result = {}
    for k in corpus.keys():
        value = choosen.count(k) / n
        final_result[k] = value
    return final_result


def check_threshold(before, actual, threshold):
    for k in before.keys():
        if(abs(before[k] - actual[k]) >= threshold):
            return True
    return False 


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    threshold = 0.001
    go = True
    final_result = {}
    for k in corpus.keys():
        value = 1 / len(corpus)
        final_result[k] = value
    while go:
        recent_one = final_result.copy()
        for k in corpus.keys():
            first_cond = (1 - damping_factor) / len(corpus)
            sum = 0
            for page in corpus.keys():
                if not corpus[page]:
                    sum += recent_one[page] / len(corpus)
                elif k in corpus[page]:
                    sum += recent_one[page] / len(corpus[page])
            second_cond = damping_factor * sum
            pr_p = first_cond + second_cond
            final_result[k] = pr_p
        go = check_threshold(recent_one, final_result, threshold)
    return final_result
    

if __name__ == "__main__":
    main()
