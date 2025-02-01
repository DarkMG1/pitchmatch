import getStripe from "@/utils/get-stripe";
import { SignedIn, SignedOut, UserButton } from "@clerk/nextjs";
import { AppBar, Container, Toolbar, Typography, Button, Box, Grid } from "@mui/material";
import Head from "next/head";

export default function Home() {

  const handleSubmit = async () => {
    const checkoutSession = await fetch('/api/checkout_session', {
      method: 'POST',
      headers: {
        origin: 'http://localhost:3000'
      }
    })

    const checkoutSessionJson = await checkoutSession.json()

    if (checkoutSession.statusCode === 5000) {
      console.error(checkoutSession.message)
      return
    }

    const stripe = await getStripe()
    const {error} = await stripe.redirectToCheckout({
      sessionId: checkoutSessionJson.id
    })

    if (error) {
      console.warn(error.message) 
    }

  }
  return (
    <Container maxWidth="100vw">
      <Head>
        <title>PitchMatch</title>
        <meta name="description" content="Create flashcard from your text" />
      </Head>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>PitchMatch</Typography>
          <SignedOut>
            <Button color="inherit" href="/sign-in">Login</Button>
            <Button color="inherit" href="/sign-up">Sign Up</Button>
          </SignedOut>
          <SignedIn>
            <UserButton />
          </SignedIn>
        </Toolbar>
      </AppBar>

      <Box sx={{ textAlign: 'center', my: 4 }}>
        <Typography variant="h2" component="h1" gutterBottom>
          Welcome to PitchMatch
        </Typography>
        <Typography variant="h5" component="h2" gutterBottom>
          The easiest way to 
        </Typography>
        <Button variant="contained" color="primary" sx={{ mt: 2, mr: 2 }} href="/generate">
          Get Started
        </Button>
        <Button variant="outlined" color="primary" sx={{ mt: 2 }}>
          Learn More
        </Button>
      </Box>

      <Box sx={{ my: 6, textAlign: 'center' }}>
        <Typography variant="h4" component="h2" gutterBottom>Features</Typography>
        <Grid container spacing={4}>
          <Grid item xs={12} md={4}>
            <Typography variant="h6">Easy Text Input</Typography>
            <Typography>
              {' '}
              //TODO
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="h6"></Typography>
            <Typography>
              {' '}
                //TODO
            </Typography>
          </Grid>
          <Grid item xs={12} md={4}>
            <Typography variant="h6"></Typography>
            <Typography>
              {' '}
                //TODO
            </Typography>
          </Grid>
        </Grid>
      </Box>

      <Box sx={{ my: 6, textAlign: 'center' }}>
        <Typography variant="h4" component="h2" gutterBottom>Pricing</Typography>
        <Grid container spacing={4} justifyContent="center">
          <Grid item xs={12} md={4}>
            <Box
              sx={{
                p: 3,
                border: '1px solid',
                borderColor: 'grey.300',
                borderRadius: 2
              }}
            >
              <Typography variant="h5">Basic</Typography>
              <Typography variant="h6">$5 / month</Typography>
              <Typography>
                {' '}
                20 swipes per day
              </Typography>
              <Button varriant="contained" color="primary" sx={{ mt: 2 }}>
                Choose Basic
              </Button>
            </Box>
          </Grid>
          <Grid item xs={12} md={4}>
            <Box
              sx={{
                p: 3,
                border: '1px solid',
                borderColor: 'grey.300',
                borderRadius: 2
              }}
            >
              <Typography variant="h5">Pro</Typography>
              <Typography variant="h6">$10 / month</Typography>
              <Typography>
                {' '}
                100 swipes per day
              </Typography>
              <Button varriant="contained" color="primary" sx={{ mt: 2 }} onClick={handleSubmit}>
                Choose Pro
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}