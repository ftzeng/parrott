#!/usr/bin/env python

import sys
import os
import yaml
import webbrowser
import tweepy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
	config = yaml.load(open(os.path.join(__location__, 'config.yml')))
	auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])

	if all(key not in config for key in ['access_key', 'access_secret']):
		webbrowser.open(auth.get_authorization_url())

		pin = raw_input('Verification pin number from twitter.com: ').strip()
		token = auth.get_access_token(verifier=pin)

		config['access_key'] = token.key
		config['access_secret'] = token.secret

		with open('config.yml', 'w') as outfile:
			outfile.write( yaml.dump(config, default_flow_style=False) )
	else:
		auth.set_access_token(config['access_key'], config['access_secret'])

	stream = tweepy.streaming.Stream(auth, StreamObserver())
	stream.filter(track=['dinosaur'])

# http://goo.gl/2FpqQ
class StreamObserver(tweepy.StreamListener):
	def on_status(self, status):
		print status.text

	def on_error(self, status_code):
		print >> sys.stderr, 'Encoundered error with status code:', status_code
		return True # Don't kill the stream

	def on_timeout(self):
		print >> sys.stderr, 'Timeout...'
		return True # Don't kill the stream

if __name__ == '__main__':
	sys.exit(main())
