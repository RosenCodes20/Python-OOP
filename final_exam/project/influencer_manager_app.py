from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGNS = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        if influencer_type not in self.VALID_INFLUENCERS:
            return f"{influencer_type} is not an allowed influencer type."

        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."

        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)

        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))

        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))

        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        if influencer.calculate_payment(campaign) > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        final_dict = {}
        for campaign in self.campaigns:
            if campaign.approved_influencers:
                final_dict[campaign] = sum([influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers])

        return final_dict

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username][0]

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted([c for c in self.campaigns], key=lambda c: (len(c.approved_influencers), -c.budget))
        result = [f"$$ Campaign Statistics $$"]
        for campaign in sorted_campaigns:
            result.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, " 
                      f"Total budget: ${campaign.budget:.2f}, " 
                      f"Total reached followers: {sum([influencer.reached_followers(campaign.__class__.__name__) for influencer in campaign.approved_influencers])}")

        return "\n".join(result)