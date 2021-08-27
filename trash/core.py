# @classmethod
#     def __act_del(cls, files: List[osp.ifile]):
#         if files is None:
#             cls.pinfo('Warning', 'File list is empty')
#             return
#         comar = cls.__Fix_args['del'].split(',')
#         for i, ifs in enumerate(files):
#             sufx = ifs.file.suffix
#             n1 = ifs.file.name.replace(sufx, '')
#             nx = n1
#             for c in comar:
#                 nx = nx.replace(c, '')
#             if n1 != nx:
#                 n2 = f'{"".join(nx)}{sufx}'
#                 n2p = osp.plib.Path(ifs.file.parent, n2)
#                 if n2p.exists() == True:
#                     n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
#                     n4p = osp.plib.Path(ifs.file.parent, n4)
#                     cls.pfile_L(i, ifs.file.name, n4)
#                     if cls.__act_save():
#                         ifs.file.rename(n4p)
#                 else:
#                     cls.pfile_L(i, ifs.file.name, n2)
#                     if cls.__act_save():
#                         ifs.file.rename(n2p)

# @classmethod
#     def __act_add(cls, file: osp.ifile):
#         if file is None:
#             cls.pinfo('Warning', 'File list is empty')
#             return
#         comar = cls.__Fix_args['add'].split('@')
#         sx, ix = [[comar[-1], 0], comar][len(comar) == 2]
#         ix = [ix, int(ix)][type(ix) is str]
#         for i, ifs in enumerate(files):
#             sufx = ifs.file.suffix
#             n1 = ifs.file.name.replace(sufx, '')
#             nx = list(n1)
#             nx.insert(ix, sx)
#             n2 = f'{"".join(nx)}{sufx}'
#             n2p = osp.plib.Path(ifs.file.parent, n2)
#             if n2p.exists() == True:
#                 n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
#                 n4p = osp.plib.Path(ifs.file.parent, n4)
#                 cls.pfile_L(i, ifs.file.name, n4)
#                 if cls.__act_save():
#                     ifs.file.rename(n4p)
#             else:
#                 cls.pfile_L(i, ifs.file.name, n2)
#                 if cls.__act_save():
#                     ifs.file.rename(n2p)

# @classmethod
# def __act_rep(cls, files: List[osp.ifile]):
#     if files is None:
#         cls.pinfo('Warning', 'File list is empty')
#         return
#     comar = cls.__Fix_args['rep'].split(':')
#     if len(comar) > 2:
#         cls.pinfo('Error', '-r xxx:yyy Parameter error')
#         return
#     for i, ifs in enumerate(files):
#         o, n = comar
#         sufx = ifs.file.suffix
#         n1 = ifs.file.name.replace(sufx, '')
#         nx = n1.replace(o, n)
#         if n1 != nx:
#             n2 = f'{"".join(nx)}{sufx}'
#             n2p = osp.plib.Path(ifs.file.parent, n2)
#             if n2p.exists() == True:
#                 n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
#                 n4p = osp.plib.Path(ifs.file.parent, n4)
#                 cls.pfile_L(i, ifs.file.name, n4)
#                 if cls.__act_save():
#                     ifs.file.rename(n4p)
#             else:
#                 cls.pfile_L(i, ifs.file.name, n2)
#                 if cls.__act_save():
#                     ifs.file.rename(n2p)

# @classmethod
#     def __act_delete(cls, files: List[osp.ifile]):
#         if files is None:
#             cls.pinfo('Warning', 'File list is empty')
#             return
#         dxpath = osp.plib.PosixPath(cls.__Fix_args['dfx'])
#         if dxpath.exists() == False:
#             cls.pinfo('Error', '{dxpath} Path does not exist')
#         else:
#             with open(dxpath, 'r') as reads:
#                 lines = reads.read().split('\n')
#                 for i, ifs in enumerate(files):
#                     sufx = ifs.file.suffix
#                     n1 = ifs.file.name.replace(sufx, '')
#                     nx = n1
#                     for L in lines:
#                         nx = nx.replace(L, '')
#                     if nx != n1:
#                         n2 = f'{"".join(nx)}{sufx}'
#                         n2p = osp.plib.Path(ifs.file.parent, n2)
#                         if n2p.exists() == True:
#                             n4 = f'{"".join(nx)}{cls.__r4()}{sufx}'
#                             n4p = osp.plib.Path(ifs.file.parent, n4)
#                             cls.pfile_L(i, ifs.file.name, n4)
#                             if cls.__act_save():
#                                 ifs.file.rename(n4p)
#                         else:
#                             cls.pfile_L(i, ifs.file.name, n2)
#                             if cls.__act_save():
#                                 ifs.file.rename(n2p)

# @classmethod
#     def __act_sn(cls, files: List[osp.ifile]):
#         if files is None:
#             cls.pinfo('Warning', 'File list is empty')
#             return
#         else:
#             fileslen = f'{len(files)}'.__len__()
#             fls = fileslen if fileslen >= 2 else 2
#             fmz = f'{{s:0{fls}}}'
#             for i, ifs in enumerate(files):
#                 sufx = ifs.file.suffix
#                 n1 = ifs.file.name.replace(sufx, '')
#                 match = re.match('[\d]{2,}[.]', n1)
#                 pa, pb = match.span()
#                 if pa == 0 and pb >= 3:
#                     cls.pfile_L(i, ifs.file.name, n1)
#                 else:
#                     nx = f'{fmz.format(s=i)}.{n1}{sufx}'
#                     if nx != n1:
#                         n1p = osp.plib.Path(ifs.file.parent, nx)
#                         cls.pfile_L(i, ifs.file.name, nx)
#                         if cls.__act_save():
#                             ifs.file.rename(n1p)