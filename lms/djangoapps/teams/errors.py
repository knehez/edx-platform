"""Errors thrown in the Team API"""


class NotEnrolledInCourseForTeam(Exception):
    """User is not enrolled in the course for the team they are trying to join."""
    pass


class AlreadyOnTeamInCourse(Exception):
    """User is already a member of another team in the same course."""
    pass
