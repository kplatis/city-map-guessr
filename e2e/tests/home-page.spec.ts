import test, { expect } from "@playwright/test";
import { HomePage } from "../pages/HomePage";

test("has title", async ({ page }) => {
  const homePage = new HomePage(page);

  await homePage.goto();

  await expect(page.locator("h1")).toHaveText("Hello World");
});
