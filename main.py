import _thread

import reception
import transmission

_thread.start_new_thread(reception.rec, ())
transmission.trans()
