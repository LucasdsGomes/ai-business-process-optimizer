from app.integrations.webhook_client import WebhookClient

class ProcessAnalysisService:

    def analyze(self, process):
        analysis_result = self.run_analysis(process)

        process.analysis_result = analysis_result
        process.status = "ANALYZED"
        self.repository.save(process)

        webhook = WebhookClient()
        webhook.send({
            "process_id": process.id,
            "name": process.name,
            "type": process.type,
            "status": process.status,
            "analysis": analysis_result
        })

        return process
