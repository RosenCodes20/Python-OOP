from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5000

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate):
        if engagement_rate >= self.required_engagement * 1.2:
            return True

        return False

