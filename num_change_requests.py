"""A module for measuring the number of change requests a GitHub PR receives.

Functions:
    num_change_requests(
        pull_request: github3.pulls.PullRequest
    ) -> Int
        Measure the number of times reviewers have requested changes.

"""
import github3


def num_change_requests(
    pull_request: github3.pulls.PullRequest) -> int:
    """Measure the number of times changes have been requested

    Args:
        pull_request (github3.pulls.PullRequest): A GitHub pull request.

    Returns:
        Int: The number of times reviewers have requested changes.

    """
    reviews = pull_request.reviews()
    state = 'CHANGES_REQUESTED'
    change_requests = [r for r in reviews if r.state == state]
    return len(change_requests)
