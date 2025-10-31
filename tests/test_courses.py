import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_toolbar_title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_list_toolbar_title_text).to_be_visible()
    expect(courses_list_toolbar_title_text).to_have_text("Courses")

    courses_list_empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_view_icon).to_be_visible()

    courses_list_empty_view_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty_view_icon).to_be_visible()
    expect(courses_list_empty_view_title_text).to_have_text("There is no results")

    courses_list_empty_view_description_text = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-description-text'
    )
    expect(courses_list_empty_view_icon).to_be_visible()
    expect(courses_list_empty_view_description_text).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    title = "Playwright"
    description = "Playwright"
    estimated_time = "2 weeks"
    max_score = "100"
    min_score = "10"

    create_course_page.fill_create_course_form(
        title=title,
        estimated_time=estimated_time,
        description=description,
        max_score=max_score,
        min_score=min_score
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title=title,
        max_score=max_score,
        min_score=min_score,
        estimated_time=estimated_time
    )
