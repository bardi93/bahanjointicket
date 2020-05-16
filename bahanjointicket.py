wait = {
    "jointicket":False
}


                        elif ("/ti/g/" in msg.text):
                            if wait["jointicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = line.findGroupByTicket(ticket_id)
                                    line.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    line.sendMessage(msg.to, "Bots Berhasil Join Link QR")

                        elif cmd == "jointicket on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["jointicket"] = True
                              line.sendMessage(msg.to, "Join Ticket Diaktifkan")

                        elif cmd == "jointicket off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["jointicket"] = False
                              line.sendMessage(msg.to, "Join Ticket Dinonaktifkan")