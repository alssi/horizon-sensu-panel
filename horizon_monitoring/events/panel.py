
import horizon
from django.utils.translation import ugettext_lazy as _
from horizon_monitoring import dashboard

class EventsPanel(horizon.Panel):
    name = _("Incidents/Events")
    slug = 'events'

dashboard.MonitoringDashboard.register(EventsPanel)