from django.shortcuts import render
from django.http import HttpResponseRedirect

from gcm import GCM

from info.models import GcmTable

# Create your views here.
def index(request):
	try:
		title = request.POST['title']
		message = request.POST['message']
	except Exception, e:
		return render(request,'push/push.html')
	else:
		API_KEY = 'AIzaSyCOrMd2EeuSp4YmBStM-qgRUzbulUitmIM'
		URI =  'https://android.googleapis.com/gcm/send'

		gcm = GCM(API_KEY)

		registration_ids = GcmTable.objects.all()

		notification = {
			'title' : title,
			'message' : message,
			'uri' :  URI
		}


		response = gcm.json_request(registration_ids=registration_ids,
                            data=notification,
                            restricted_package_name="gcm.play.android.samples.com.gcmquickstart",
                            priority='high',
                            delay_while_idle=False)

		# Successfully handled registration_ids
		if response and 'success' in response:
		    for reg_id, success_id in response['success'].items():
		        print('Successfully sent notification for reg_id {0}'.format(reg_id))
		
		# Handling errors
		if 'errors' in response:
		    for error, reg_ids in response['errors'].items():
		        # Check for errors and act accordingly
		        if error in ['NotRegistered', 'InvalidRegistration']:
		            # Remove reg_ids from database
		            for reg_id in reg_ids:
		                print("Removing reg_id: {0} from db".format(reg_id))
		
		# Repace reg_id with canonical_id in your database
		if 'canonical' in response:
		    for reg_id, canonical_id in response['canonical'].items():
		        print("Replacing reg_id: {0} with canonical_id: {1} in db".format(reg_id, canonical_id))

		return HttpResponseRedirect('/push')