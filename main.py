import AmazonNetworkAnalysis
import BarabasiNetwork
import TwitchNetworkAnalysis

print("\nAmazon product network analysis:")
AmazonNetworkAnalysis.analyze_network()

print("\nBarabasi network model analysis for twitch:")
BarabasiNetwork.analyze_network(334863, 4)

print("\nTwitch network model analysis:")
TwitchNetworkAnalysis.analyze_network()

print("\nBarabasi network model analysis for twitch:")
BarabasiNetwork.analyze_network(168114, 60)