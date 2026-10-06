# __The Laplacian on the Orbital Graphs__

## Introduction

The level Schreier graphs of the previous article grow exponentially and their spectra converge to intervals; the graphs that model a single point of the limit space are smaller and more rigid. The **orbital graph** of a boundary point $\xi$ is the Schreier graph of the action of the group on the orbit $G\xi$, equivalently the pointed limit of the level graphs $(\Gamma_n(G,S),\xi_n)$, and it is the object that carries the analysis of Parts III and IV to a self-similar group: its **Laplacian** is the limit of the finite-dimensional Laplacians, its **heat kernel** measures the diffusion on the limit space, and its **spectrum** is a dynamical invariant of the group. For the groups of intermediate growth the orbital graph embeds in the limit space with polynomial growth, and the spectrum can be wild: Bartholdi and Grigorchuk produced the first connected $4$-regular graph of polynomial growth whose Laplacian has a **Cantor spectrum**, and a second whose spectrum is a Cantor set together with a countable family of isolated points, the two examples being the first graphs of constant vertex degree with a totally disconnected spectrum.

The article develops the orbital graphs and their analysis. It defines the orbital graph of a boundary point as the Schreier graph of its orbit, proves that the pointed level graphs converge to it in the pointed Gromov–Hausdorff sense, and identifies its growth with the degree of the limit space. It defines the Laplacian on the orbital graph, its spectral measure and its Kesten measure, and states the recurrence dichotomy in terms of the spectral radius and the amenability of the group. It states the **Cantor-spectrum theorem** of Bartholdi and Grigorchuk with the two values $\lambda=\tfrac{45}{16}$ and $\lambda=6$ of the quadratic renormalisation, the form $F(J)$ of the spectrum with $J$ the Julia set, and the explicit nested-radical eigenvalues of the group $\overline\Gamma$; and it draws the contrast with the level graphs. It closes with the **heat kernel** on the fractal and with **anomalous diffusion**: the spectral dimension $d_s$ and the walk dimension $d_w$, the Einstein relation $d_s=2d_f/d_w$, the sub-Gaussian estimate of Barlow and Perkins, and the sub-diffusive mean square displacement $t^{2/d_w}$.

The group, the wreath recursion, the self-similarity and the contraction are *Self-Similar Groups*; the level graphs, the limit space, the tiles, the shift and the pointed convergence are *Limit Spaces and Schreier Graphs*; the level spectra and the substitution are *The Spectrum of the Schreier Graphs*; the Dirichlet form, the spectral dimension and the graph Laplacian of the gasket are *The Laplacian on a Self-Similar Set*; the random walk, the heat kernel and the Kesten measure are *Random Walks on Groups*, and the diffusion on a fractal is the probability of Part III. No physics is invoked.

## The Orbital Graphs

### The Orbit of a Boundary Point

**Definition.** Let $G\le\operatorname{Aut}(\mathcal{T})$ be self-similar with generating set $S$, and let $\xi\in\partial\mathcal{T}$. The **orbit** $G\xi=G\cdot\xi$ is countable; the **orbital graph** $\Gamma_\xi=\Gamma_\xi(G,S)$ has the orbit as its vertex set and, for each $s\in S$ and each $\eta\in G\xi$, the edge $\eta-s\eta$; it is the Schreier graph of the action on the orbit, with the base point $\xi$. The **limit graph** of the group is the orbital graph of a point of the limit space under the identification of *Limit Spaces and Schreier Graphs*.

**Definition.** The **growth** of the orbital graph is the growth of the ball, $v(R)=\#\{\eta\in G\xi : d(\eta,\xi)\le R\}$ with the graph distance, and the orbital graph has **polynomial growth of degree $D$** if $v(R)\asymp R^D$. The **degree** of the limit space is the dimension of the limit space in the sense of *Limit Spaces and Schreier Graphs*, and it bounds the growth in the following theorem.

**Theorem (pointed convergence and growth).** The pointed Schreier graphs $(\Gamma_n(G,S),\xi_n)$ converge in the pointed Gromov–Hausdorff sense to the orbital graph $(\Gamma_\xi,\xi)$; the orbital graph embeds in the limit space with the tiles as the balls, its growth is at most polynomial of degree the degree of the limit space, and for a contracting group the orbital graphs of two boundary points are isomorphic as unlabelled graphs whenever the points lie in the same tile class.

*Proof sketch.* The orbits of $\xi_n$ under $G$ on the level $X^n$ are the vertices of $\Gamma_n$, and the ball of radius $R$ around $\xi_n$ in $\Gamma_n$ is $\{g\xi_n:|g|_S\le R\}$; the sections of a word of length $R$ are bounded by the contraction, so the ball stabilises as $n\to\infty$, giving the pointed limit; the stabilisation at the level of the tiles is the definition of the limit space. The growth bound is the polynomial growth of the limit space under the coding of *Limit Spaces and Schreier Graphs*; the proof, and the precise degree, are in the article of Nekrashevych and in Bartholdi–Grigorchuk–Nekrashevych.

### The Embedding in the Limit Space

**Remark (the geometric meaning).** The orbital graph $\Gamma_\xi$ is a **lattice** in the limit space: its vertices are the images of $\xi$ under the group, and the edges are the generators. For the adding machine the orbital graph is the bi-infinite line, for the lamplighter it is the direct product of the line with a lamp graph, and for the groups of intermediate growth it is a fractal lattice of polynomial growth — the graph whose Laplacian the rest of the article studies. The tiles $T_v$ of *Limit Spaces and Schreier Graphs* are the Voronoi cells of the lattice, and the shift acts as the dilation of the lattice.

## The Laplacian on the Orbital Graph

### The Graph Laplacian and Its Spectral Measure

**Definition.** On the orbital graph the **Laplacian** is the graph Laplacian of *Graph Theory*,
$$
\Delta f(\eta)=\sum_{s\in S}\bigl(f(\eta)-f(s\eta)\bigr),
$$
a bounded self-adjoint operator on $\ell^2(G\xi)$ with the spectral resolution $E$ and the **spectral measure** $\mu_{\xi,\xi}(d\lambda)=\langle E(d\lambda)\delta_\xi,\delta_\xi\rangle$; the **Kesten measure** is the normalised spectral measure of the random walk, $\mu=\tfrac1{|S|}\mu_{\xi,\xi}$, and the **spectral radius** is $\rho=\limsup_R v(2R)^{1/2R}$ for the random walk's return generating function.

**Theorem (the spectral measure and the return probabilities).** The return probability of the simple random walk on the orbital graph is the moment sequence of the Kesten measure, $p_{2n}(\xi,\xi)=\int(\tfrac{|S|-\lambda}{|S|})^{2n}\mu(d\lambda)$, and the measure is the limit of the spectral measures of the level graphs; in particular the level spectra of the previous article converge on average to the Kesten measure of the orbital graph, and for the lamplighter the limit is the atomic measure with the atoms $\cos(m\pi/n)$ of the previous article.

*Proof sketch.* The Cayley–Hamilton/Fourier form of the spectral theorem for a self-adjoint operator on $\ell^2$: the heat kernel $e^{t\Delta}\delta_\xi$ is the image of $\delta_\xi$ under the functional calculus, and its norm at time $t$ is the Fourier transform of $\mu$; the identity $e^{t\Delta}\delta_\xi(\eta)=$ the $(2n)$-th return probability at integer times $t=2n$ is the combinatorial identity of the walk. The convergence of the finite-dimensional spectral measures is the pointed convergence and the monotone class argument of *Random Walks on Groups*.

### Recurrence, Transience and Amenability

**Theorem (the dichotomy).** For the simple random walk on the orbital graph,
$$
\sum_n p_{2n}(\xi,\xi)=\infty\quad\text{(recurrent)} \iff \rho=1 ,
$$
and the walk is recurrent exactly when the spectral measure has no gap at the bottom of the spectrum and the group generated by the support of the measure is amenable for the quotient; the Grigorchuk group is amenable, so its random walk is recurrent and $\rho=1$, while the lamplighters at the points with a nonzero tail are transient.

*Proof.* The recurrence criterion is the theorem of Kesten, quoted from *Random Walks on Groups*: the walk is recurrent if and only if the return generating function diverges, which is the statement $\rho=1$; the amenability of the Grigorchuk group is that of *Self-Similar Groups*, so its random walk has no spectral gap by the theorem of Kesten for amenable groups. The transience of the shifted walks follows from the drift in the lamp coordinate. The verification of the criterion on the level graphs is the count of the return probabilities of the cycles for the adding machine, where $\rho=1$ and the walk is recurrent.

## The Cantor Spectrum

### The Theorem of Bartholdi and Grigorchuk

**Theorem (the Cantor spectrum of the orbital graph).** There is a connected $4$-regular graph of polynomial growth which is the orbital (Schreier) graph of a group of intermediate growth and whose Laplacian has **Cantor spectrum**. The spectrum is $K=F(J)$, where $F$ is a simple algebraic function and $J$ is the Julia set of the quadratic map $z\mapsto z^2-\lambda$, with $\lambda=\tfrac{45}{16}$ in the first example and $\lambda=6$ in a second example; in the second the spectrum is the **union of the Cantor set $K$ and a countable set $P$ of isolated points whose accumulation set is $K$**. The Julia set is the set of the points
$$
\pm\sqrt{\lambda\pm\sqrt{\lambda\pm\sqrt{\lambda\pm\cdots}}} .
$$

*Proof sketch.* The orbital graph is the limit of a substitutional family of graphs as in *The Spectrum of the Schreier Graphs*; the Schur complement of the substitution gives the quadratic map, and the level spectra are its iterated preimages of a finite set, hence the spectrum is the Julia set of the quadratic map; the map is real with an escaping critical orbit and its Julia set is a Cantor set, while the isolated points are the finitely supported configurations and the born eigenvalues. The two values of $\lambda$ correspond to the two groups (the group $\overline\Gamma$ and the Grigorchuk-type group) and the details are in the article of Bartholdi and Grigorchuk, where the substitutional rules for $\overline\Gamma$ and $\overline{\overline\Gamma}$ are written out.

### The Explicit Eigenvalues

**Corollary (the nested radicals of the spectrum).** For the group $\overline\Gamma$ the spectrum of the Laplacian is the closure of the set
$$
\left\{4,\ -2,\ 1,\ 1\pm\sqrt{\frac{9\pm3}{2}},\ 1\pm\sqrt{\frac{9\pm\sqrt{45\pm4\cdot3}}{2}},\ 1\pm\sqrt{\frac{9\pm\sqrt{45\pm4\sqrt{45\pm4\cdot3}}}{2}},\ \dots\right\}
$$
with the eigenvalues $\{4\}$ at level $0$, $\{1,4\}$ at level $1$ and $\{-2,1,4\}\cup\bigcup_{3\le m\le n+1}\pi_\pm(X_m)\cup\bigcup_{3\le m\le n-1}\pi_\pm(Y_m)$ at level $n\ge2$, where $\pi_\pm(\theta)=1\pm\sqrt{5-\theta}$; the spectrum is a Cantor set of Lebesgue measure zero, symmetric about $1$, and the spectral measure is concentrated on those algebraic numbers with the indicated weights.

*Proof.* The proposition and the corollary of Bartholdi and Grigorchuk. The renormalisation is the map $\theta\mapsto\pi_\pm(\theta)=1\pm\sqrt{5-\theta}$ composed with the substitution, and the Cantor set is the attractor of its inverse branches; the middle-thirds structure of the nested radicals is the element $1\pm\sqrt{\tfrac12(9\pm\cdots)}$ written out. The verification of the first two levels of the nested radicals returns $4$, $-2$, $1$, $1\pm\sqrt6\approx 3.449490$ and $-1.449490$, against the explicitly computed level spectra of the ternary-tree group.

## The Heat Kernel and Anomalous Diffusion

### The Heat Kernel on the Gasket

**Definition.** Let $\Delta$ be the Laplacian of *The Laplacian on a Self-Similar Set* on the Sierpiński gasket, with the self-similar measure $\mu$ of *The Self-Similar Measure and the Invariant Measure*, and let $p_t(x,y)$ be the heat kernel, the density of the semigroup $e^{t\Delta}$; write $d(x,y)$ for the geodesic distance and $d_f=\log3/\log2$ for the dimension of the gasket.

**Theorem (the sub-Gaussian estimate).** There are constants $c_1,c_2$ such that
$$
p_t(x,x)\asymp t^{-d_s/2},\qquad
p_t(x,y)\asymp t^{-d_s/2}\exp\Bigl(-c\Bigl(\frac{d(x,y)^{d_w}}{t}\Bigr)^{\frac1{d_w-1}}\Bigr),
$$
with the **spectral dimension** $d_s=2\log3/\log5=1.365212$ and the **walk dimension** $d_w=\log5/\log2=2.321928$, and $c_1\le c\le c_2$; the estimate is the theorem of Barlow and Perkins for the gasket, and the two-sidedness — both the diagonal decay and the off-diagonal sub-Gaussian factor — is essential.

*Proof sketch.* The upper bound is the Faber–Krahn/relative Faber–Krahn argument applied to the resistance form of the gasket, using the exact scaling $R_n=(\tfrac53)^n\tfrac23$; the lower bound is the chaining of the Harnack inequality across the levels of the graph, which the same resistance scaling controls. The exponent $d_w-1$ in the exponential is the exponent of the resistance, $R(r)\asymp r^{d_f-d_w}$, so that the exponent of the exponential can be written $(d(x,y)^{d_w}/t)^{1/(d_w-1)}$; for the gasket this is the sub-Gaussian form, not the Euclidean $d(x,y)^2/t$.

### The Spectral and Walk Dimensions

**Theorem (the Einstein relation and the anomalous diffusion).** The dimensions satisfy
$$
d_s=\frac{2d_f}{d_w},
$$
the mean square displacement of the diffusion on the gasket is
$$
\mathbb{E}\,d(X_t,X_0)^2\asymp t^{2/d_w}=t^{\log4/\log5}=t^{0.861353\ldots},
$$
sub-diffusive because $d_w>2$, and the resistance between two points at distance $r$ scales as $R(r)\asymp r^{d_f-d_w}$.

*Proof.* The Einstein relation is the identity $2\log3/\log5=2(\log3/\log2)/(\log5/\log2)$; the mean square displacement is the second moment of the heat kernel, whose scaling $t^{1/d_w}$ around the origin is the content of the sub-Gaussian estimate; the resistance scaling is the $n$-th power $R_n=(5/3)^n$ with the distance $r=2^{-n}$, so $R\asymp r^{-\log(5/3)/\log2}=r^{d_f-d_w}$. The verification of $2d_f/d_w=d_s$ is exact: $2\cdot1.584963/2.321928=1.365212$. The Einstein relation and the sub-Gaussian estimate carry over to the orbital graphs of the groups of polynomial growth with the spectral and walk dimensions determined by the contraction and the growth, which is the content of the theory of Bartholdi, Grigorchuk and Nekrashevych; the estimates for the general p.c.f. sets are those of Kigami.

**Remark (the gap and the decay).** The Cantor spectrum of the theorem of Bartholdi and Grigorchuk has gaps, hence the heat kernel on that orbital graph has an exponential factor in addition to the power $t^{-d_s/2}$: the walk is recurrent but returns more slowly than the power law of the gasket, and the spectral gap is not seen by the level graphs, whose spectra fill the two intervals. This is the analytical difference between the orbital graph and the level graph of the same group.

## Summary

The **orbital graph** $\Gamma_\xi$ of a boundary point is the Schreier graph of the orbit $G\xi$, the pointed limit of the level graphs, and a lattice in the limit space with polynomial growth at most the degree of the limit space; its **Laplacian** $\Delta f(\eta)=\sum_s(f(\eta)-f(s\eta))$ has the spectral measure $\mu_{\xi,\xi}$ and the **Kesten measure**, whose moments are the return probabilities of the random walk, and the walk is recurrent exactly when the spectral radius is one — the case of the amenable Grigorchuk group. For the groups of intermediate growth the spectrum can be totally disconnected: Bartholdi and Grigorchuk produced a connected $4$-regular orbital graph of polynomial growth with **Cantor spectrum** $K=F(J)$, $J$ the Julia set of $z^2-\lambda$, $\lambda=\tfrac{45}{16}$, and a second with spectrum a Cantor set together with countable isolated points, $\lambda=6$; for $\overline\Gamma$ the spectrum is the closure of $\{4,-2,1,1\pm\sqrt{\tfrac12(9\pm3)},1\pm\sqrt{\tfrac12(9\pm\sqrt{45\pm4\cdot3})},\dots\}$ under $\pi_\pm(\theta)=1\pm\sqrt{5-\theta}$, a measure-zero Cantor set symmetric about $1$. The **heat kernel** on the gasket satisfies the sub-Gaussian $p_t(x,y)\asymp t^{-d_s/2}\exp(-c(d(x,y)^{d_w}/t)^{1/(d_w-1)})$ with $d_s=2\log3/\log5=1.365212$ and $d_w=\log5/\log2=2.321928$; the **Einstein relation** $d_s=2d_f/d_w$ and the anomalous displacement $\mathbb{E}d(X_t,X_0)^2\asymp t^{0.861353}$ follow, and the resistance scales as $R(r)\asymp r^{d_f-d_w}$. The Einstein identity and the resistance exponent were verified exactly from the resistance ratios of the previous article; the Cantor spectra and the heat kernel estimates are quoted from Bartholdi–Grigorchuk and Barlow–Perkins.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G\xi$, $\Gamma_\xi(G,S)$ | The orbit of $\xi$; the orbital graph |
| $v(R)$, $D$ | The growth of the orbit; the degree of the limit space |
| $(\Gamma_n,\xi_n)\to(\Gamma_\xi,\xi)$ | Pointed Gromov–Hausdorff convergence |
| $\Delta f(\eta)=\sum_s(f(\eta)-f(s\eta))$ | The Laplacian on the orbital graph |
| $\mu_{\xi,\xi}$, Kesten measure | Spectral measure; normalised spectral measure of the walk |
| $\rho$ | The spectral radius |
| $K=F(J)$, $z^2-\lambda$, $\lambda=\tfrac{45}{16},6$ | The Cantor spectrum and its quadratic renormalisation |
| $\pi_\pm(\theta)=1\pm\sqrt{5-\theta}$ | The renormalisation of the $\overline\Gamma$ spectrum |
| $p_t(x,y)$, $d_s$, $d_w$ | Heat kernel, spectral dimension, walk dimension |
| $d_s=2d_f/d_w$, $R(r)\asymp r^{d_f-d_w}$ | The Einstein relation and the resistance scaling |

## Further Reading

- Laurent Bartholdi and Rostislav I. Grigorchuk, "On the spectrum of Hecke type operators related to some fractal groups", *Trudy Matematicheskogo Instituta imeni V. A. Steklova* **231** (2000), 5–45, for the Cantor spectra, the Julia sets and the explicit nested radicals.
- Laurent Bartholdi, Rostislav Grigorchuk and Volodymyr Nekrashevych, "From fractal groups to fractal sets", in *Fractals in Graz 2001* (Birkhäuser, 2003), 25–118, for the limit space, the orbital graphs and the growth.
- Martin T. Barlow and Edwin A. Perkins, "Brownian motion on the Sierpiński gasket", *Probability Theory and Related Fields* **79** (1988), 543–623, for the heat kernel, the sub-Gaussian estimate and the walk dimension.
- Jun Kigami, *Analysis on Fractals* (Cambridge University Press, 2001), for the heat kernel on p.c.f. self-similar sets and the Einstein relation.
- Harry Kesten, "Symmetric random walks on groups", *Transactions of the American Mathematical Society* **92** (1959), 336–354, for the recurrence criterion and the spectral radius.
- Wolfgang Woess, *Random Walks on Infinite Graphs and Groups* (Cambridge University Press, 2000), for the spectral measure, the return probabilities and the amenability.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the orbital graphs, the limit space and the contraction.
