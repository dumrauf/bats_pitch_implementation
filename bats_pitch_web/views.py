import gzip

from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

from bats_pitch_web.forms import BATSPitchFileForm
from bats_pitch_web.utils import analyze_stream


def upload(request):
    """
    The main view which accepts a gzipped file, analyzes it and eventually returns a page with statistics
    about the number of BATS PITCH messages found in the file.
    """
    if request.method == 'POST':
        form = BATSPitchFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            context = {
                'file': f,
            }

            try:
                gzf = gzip.GzipFile(fileobj=f)
                detected_messages, analysis = analyze_stream(gzf)
            except IOError:
                return render_to_response('gzip_error.html',
                                          context,
                                          context_instance=RequestContext(request))
            context.update({
                'IS_INCLUDING_ANALYSIS_IN_RETURNED_HTML': settings.IS_INCLUDING_ANALYSIS_IN_RETURNED_HTML,
                'detected_messages': detected_messages,
                'analysis': analysis,
            })
            return render_to_response('upload_results.html',
                                      context,
                                      context_instance=RequestContext(request))
    else:
        form = BATSPitchFileForm()
    return render_to_response('upload.html',
                              {'form': form},
                              context_instance=RequestContext(request))
