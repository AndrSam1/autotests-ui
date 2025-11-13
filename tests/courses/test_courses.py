import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:

    @allure.severity(Severity.NORMAL)
    @allure.title("Check displaying of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Create course")
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
        )
        create_course_page.create_exercise_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        title = "Playwright"
        description = "Playwright"
        estimated_time = "2 weeks"
        max_score = "100"
        min_score = "10"

        create_course_page.create_course_form.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time
        )

    @allure.severity(Severity.CRITICAL)
    @allure.title("Edit course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        title = "Playwright"
        description = "Playwright"
        estimated_time = "2 weeks"
        max_score = "100"
        min_score = "10"

        create_course_page.create_course_form.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time
        )

        courses_list_page.course_view.menu.click_edit(index=0)

        new_title = "Playwright New"
        new_description = "Playwright New"
        new_estimated_time = "3 weeks"
        new_max_score = "110"
        new_min_score = "20"

        create_course_page.create_course_form.fill(
            title=new_title,
            estimated_time=new_estimated_time,
            description=new_description,
            max_score=new_max_score,
            min_score=new_min_score
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title=new_title,
            max_score=new_max_score,
            min_score=new_min_score,
            estimated_time=new_estimated_time
        )

