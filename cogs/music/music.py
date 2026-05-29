    @commands.command()
    async def skip(self, ctx):

        vc = ctx.voice_client

        if vc:
            await vc.skip()

            await ctx.send("⏭️ Skipped song.")