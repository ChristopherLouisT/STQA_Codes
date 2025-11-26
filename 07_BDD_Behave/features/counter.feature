Feature: Hit Counter

As a Website User
I want a button that can make the counter go up
So that I can know how many times I have clicked the button

Scenario: The counter goes up when the button is clicked
Given the counter is reset
When a user clicks the "Hit" Button
Then the counter should be at 1
When a user clicks the "Hit" Button
Then the counter should be at 2