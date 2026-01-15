import os
from textwrap import dedent

import nbgrader.exchange.default.fetch_assignment as default_fetch_assignment
from nbgrader.utils import check_mode

from .exchange import Exchange


class ExchangeFetchAssignment(Exchange, default_fetch_assignment.ExchangeFetchAssignment):
    def init_src(self):
        if self.coursedir.course_id == "":
            self.fail("No course id specified. Re-run with --course flag.")
        if not self.authenticator.has_access(self.coursedir.student_id, self.coursedir.course_id):
            self.fail("You do not have access to this course.")

        self.course_path = os.path.join(self.root, self.coursedir.course_id)
        self.outbound_path = os.path.join(self.course_path, self.outbound_directory)
        if self.personalized_outbound:
            self.src_path = os.path.join(
                self.outbound_path,
                os.getenv("JUPYTERHUB_USER"),
                self.coursedir.assignment_id,
            )
        else:
            self.src_path = os.path.join(self.outbound_path, self.coursedir.assignment_id)

        if not os.path.isdir(self.src_path):
            self._assignment_not_found(self.src_path, os.path.join(self.outbound_path, "*"))
        if not check_mode(self.src_path, read=True, execute=True):
            self.fail("You don't have read permissions for the directory: {}".format(self.src_path))

    def copy_files(self):
        self.log.info("Source: {}".format(self.src_path))
        self.log.info("Destination: {}".format(self.dest_path))
        self.do_copy(self.src_path, self.dest_path)
        self.log.info(
            "Fetched as: {} {}".format(self.coursedir.course_id, self.coursedir.assignment_id)
        )

    def do_copy(self, src, dest):
        if self.personalized_outbound:
            personalized_src = os.path.join(src, os.getenv("JUPYTERHUB_USER"))
            if os.path.exists(personalized_src):
                src = personalized_src
            else:
                self.log.warning(
                    dedent(
                        f"""
                    Using personalized outbound, but no directory for
                    user {os.getenv("JUPYTERHUB_USER")} exists.
                    """
                    )
                )
        super().do_copy(src, dest)
