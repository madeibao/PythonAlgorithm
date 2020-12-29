torch.manual_seed(args.seed) 


#为CPU设置种子用于生成随机数，以使得结果是确定的 
if args.cuda: 
    torch.cuda.manual_seed(args.seed)
    #为当前GPU设置随机种子；


    # 如果使用多个GPU，应该使用torch.cuda.manual_seed_all()为所有的GPU设置种子。




