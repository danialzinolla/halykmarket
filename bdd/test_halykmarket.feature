Feature: Halyk Market Test

  Background:
    Given I am on the Halyk Market page

  Scenario: Search for a product and add favorites
    When I search for a product
    When I click on a product
    Then I should see the product title


