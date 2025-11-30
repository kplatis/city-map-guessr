import { expect, Page } from "@playwright/test";

export class HomePage {
  constructor(private page: Page) {}

  async goto() {
    await this.page.goto("http://localhost:3001");
    await this.page.waitForLoadState("networkidle");
  }

  async expectTitleToContain(substring: string) {
    await expect(this.page).toHaveTitle(substring);
  }
}
