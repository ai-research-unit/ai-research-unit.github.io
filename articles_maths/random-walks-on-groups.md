
# __Random Walks on Groups__

## Introduction

A random walk on a group is a sequence of products of independent identically distributed group elements, and it is at once a probability theory, a harmonic analysis and a geometry. The probability theory is the study of the position after $n$ steps; the harmonic analysis appears because the law of the position is the $n$-fold convolution power of the step distribution, so the walk is a semigroup of convolution operators on the group, and the whole Fourier apparatus of the harmonic analysis on groups becomes available; and the geometry appears because the asymptotic behaviour of the walk detects the growth and the amenability of the group, with the striking conclusion that the walk is transient exactly when the group is non-amenable. No other subject joins the harmonic analysis of a group to its probability theory so directly: the walk is the object on which the harmonic analysis of a group is tested, and it is the stochastic process that the theory of Markov chains describes.

This article develops the subject from its definition. It defines the walk and its convolution powers, identifies its transition operator with the convolution operator of the group algebra, computes the return probabilities by Fourier analysis in the abelian and compact cases and by spectral theory in general, states the recurrence and transience criteria and the Chung–Fuchs theorem, proves the equivalence between the transience of the walk and the non-amenability of the group (Kesten's theorem), relates the decay of the return probabilities to the growth of the group (Varopoulos's theorem), and describes the Poisson boundary and the Liouville property. The examples — the walks on $\mathbb{Z}^d$, on the free groups, on the finite and compact groups, and on the lattices of a Lie group — run through the article.

The place of the article is fixed by four boundaries, and the first two are the two categories themselves.

- The **harmonic analysis on groups** — the Haar measure, the convolution algebra $L^1(G)$, the abelian Fourier transform and duality, the Peter–Weyl theorem, the noncommutative Fourier transform and the Plancherel theorem — is articles 1–6 of this part, *Harmonic Analysis on Groups*, *Analysis on Compact Groups*, *The Peter–Weyl Theorem*, *The Convolution Algebra $L^1(G)$*, *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*, and the present article is their probabilistic application: the step distribution is a measure, its Fourier transform is the multiplier of the walk, and the return probabilities are the coefficients of the Fourier transform of the convolution powers. The operators that the walk generates live in the group von Neumann algebra treated in *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*.
- The **Markov chains and processes** — the transition kernel, the Markov and strong Markov properties, the recurrence criterion, the stationary distribution, the ergodic theorem and the generator — are *Markov Chains and Processes*, and the walk on a countable group is the translation-invariant case of a Markov chain; the probabilistic frame is *Measure-Theoretic Probability*, *Independence and Conditional Expectation*, *Laws of Large Numbers and the Central Limit Theorem* and *Martingales*, and the continuous-time analogue is *Brownian Motion and Stochastic Calculus*.
- The **ergodic theory** — the invariance, the ergodicity, the mixing and the equidistribution — is *Ergodic Theory of Group Actions* and *Ergodic Theory*, and the **equidistribution** of the walk on a compact group is the subject of *Equidistribution*; the **amenability** and the **growth** of a group are Part II's (*Amenable Groups*) and Part I's (*Combinatorial Group Theory*, *Geometric Group Theory*), and the lattices and the homogeneous spaces are Part II's, with the dynamics on them in *Homogeneous Dynamics* and *Ratner's Theorems*. The **number-theoretic** counterpart of the model is *Probabilistic Number Theory*.
- The **per-system analysis** of a single number system is Part V's, and the **specific harmonic analysis** of one hypercomplex system is the synthetic studies' in *Harmonic Analysis over Hypercomplex Systems*. No physics is invoked.

Throughout, $G$ is a locally compact second countable group with identity $e$ and left Haar measure $dx$, or a countable group with the discrete topology; $\mu$ is a probability measure on $G$, the **step distribution**, and $\{g_n\}_{n\ge1}$ are independent with law $\mu$. The **random walk** is

$$
X_0 = e, \qquad X_n = g_1g_2\cdots g_n,
$$

with law $\mathbb{P}$, and $\mu^{*n}$ is its $n$-fold convolution power, so that $\mathbb{P}(X_n\in A) = \mu^{*n}(A)$; the return probability is written $p^{(n)}(e)$: for a discrete group, whose Haar measure is counting measure, it is the mass $\mu^{*n}(\{e\})$, while for a compact group with normalised Haar measure $m$ it is the density of $\mu^{*n}$ with respect to $m$, the two notions coinciding exactly when the Haar measure is counting measure. The **transition operator** is $P_\mu f(x) = \int f(xg)\,d\mu(g)$ (a right walk; the left walk is defined with $f(gx)$), and $p^{(n)}(x,y)$ is the transition kernel. A measure is **symmetric** if $\mu(A) = \mu(A^{-1})$ for every measurable $A$, **non-degenerate** if its support generates a dense subgroup, **aperiodic** if the support is not contained in a coset of a proper closed subgroup, and **spread out** if some convolution power has a nonvanishing continuous part. The Green function is $G(x,y) = \sum_{n\ge0}p^{(n)}(x,y)$, and the spectral radius is $\rho = \rho(P_\mu) = \sup\{|\lambda| : \lambda \in \operatorname{Spec}(P_\mu)\}$.

## The Random Walk and Its Convolution Algebra

### Definition and Examples

**Definition.** The **random walk on $G$ with step distribution $\mu$** is the Markov chain $\{X_n\}$ with $X_0=e$ and $X_n = g_1\cdots g_n$, the $g_i$ independent with law $\mu$; equivalently, the Markov chain with transition kernel $p(x,A) = \mu(x^{-1}A)$.

The transition probabilities are invariant under left translation: $p(x,A) = p(gx,gA)$, and the walk is a Markov chain on the homogeneous space $G$ with a group-invariant transition law. The distribution of $X_n$ is the convolution power, $\mu^{*n}$, as the definition of convolution gives

$$
\mathbb{P}(X_n \in A) = \mu^{*n}(A), \qquad \mu^{*n}(A) = \int_G\mathbf{1}_A(x)\,\mu^{*n}(dx),
$$

so the study of the walk is the study of the convolution powers of a probability measure, and every tool of *The Convolution Algebra $L^1(G)$* applies.

**Example (the walks on $\mathbb{Z}$ and $\mathbb{Z}^d$).** Let $G = \mathbb{Z}$ and $\mu = \frac12(\delta_1+\delta_{-1})$, the simple symmetric walk. Then $\mu^{*n}$ is the law of the sum of $n$ independent signs, and $p^{(2n)}(0) = \binom{2n}{n}4^{-n}\sim(\pi n)^{-1/2}$, whose sum diverges; the walk is recurrent. On $\mathbb{Z}^d$ with $\mu = \frac{1}{2d}\sum_{i=1}^d(\delta_{e_i}+\delta_{-e_i})$ one has $p^{(2n)}(0)\sim Cn^{-d/2}$, so the sum diverges for $d\leq2$ and converges for $d\geq3$; this is the arithmetic of Pólya's theorem in *Markov Chains and Processes*, and it is the growth of the group $\mathbb{Z}^d$ that is responsible.

**Example (the free group $\mathbb{F}_2$).** Let $G = \mathbb{F}_2 = \langle a,b\rangle$ and let $\mu = \frac14(\delta_a+\delta_{a^{-1}}+\delta_b+\delta_{b^{-1}})$, the uniform measure on the four generators and their inverses. The Cayley graph is the $4$-regular tree, and a computation on the tree gives

$$
p^{(2n)}(e) \sim C\left(\frac34\right)^n n^{-3/2}, \qquad \rho = \frac{\sqrt3}{2} < 1,
$$

so the return probabilities decay exponentially and the walk is transient; the group is non-amenable, and Kesten's theorem below makes the implication general.

**Example (a finite group).** Let $G$ be finite and $\mu$ a probability measure whose support generates $G$. The convolution powers converge to the uniform (Haar) measure and the rate is governed by the largest nontrivial Fourier coefficient: $\|\mu^{*n}-\mathrm{Haar}\|_{\mathrm{TV}}\le C|\lambda_2|^n$ with $\lambda_2 = \sup_{\pi\neq1}\|\widehat\mu(\pi)\|$, by the Peter–Weyl theorem of *The Peter–Weyl Theorem* and *Analysis on Compact Groups*. The walk on the symmetric group generated by transpositions, with $\mu$ the uniform measure on transpositions, is the model of the **cutoff phenomenon**: the distance to the uniform measure stays at its maximum and then drops sharply at time $\frac12n\log n$ (Diaconis–Shahshahani).

### The Transition Operator as a Convolution

**Proposition.** The transition operator of the walk is the right convolution by $\mu$,

$$
P_\mu f(x) = \int f(xg)\,d\mu(g) = (f*\check\mu)(x), \qquad \check\mu(A) = \mu(A^{-1}),
$$

and its adjoint on $L^2(G)$ is $P_\mu^* = P_{\check\mu}$; the operator is self-adjoint exactly when $\mu$ is symmetric. The iterates satisfy $P_\mu^nf(x) = \int f(xg)\,d\mu^{*n}(g) = f*\check\mu^{*n}(x) = P_{\mu^{*n}}f(x)$.

*Proof.* The first identity is the change of variables and the definition of the convolution of *The Convolution Algebra $L^1(G)$*; the adjoint is computed from $\langle P_\mu f,g\rangle = \iint f(xy)g(x)\,d\mu(y)\,dx = \iint f(x)g(xy^{-1})\,d\mu(y)\,dx = \langle f, P_{\check\mu}g\rangle$, using the unimodularity of the Haar measure for the translation; for a general group the modular function enters and one restricts to the discrete case or uses the two-sided convolution. The iterate formula is immediate from $\mu^{*n}*\mu = \mu^{*(n+1)}$. $\square$

The proposition is the bridge between the harmonic analysis and the probability: the walk is the semigroup $\{P_{\mu^{*n}}\}$ of convolution operators, and the question of the behaviour of the walk is the question of the behaviour of the powers of the convolution operator. On $\ell^2(G)$ in the discrete case the operator $P_\mu$ is the image of $\mu$ under the regular representation, so its spectral theory is that of the group von Neumann algebra of *Noncommutative Harmonic Analysis*.

## Fourier Analysis of the Walk

### The Abelian Case

**Theorem (Fourier description).** Let $G$ be a locally compact abelian group with dual $\widehat G$ and Fourier transform $\widehat\mu(\chi) = \int_G\chi(x)\,d\mu(x)$, as in *Harmonic Analysis on Groups*. Then for the walk with step distribution $\mu$,

$$
\widehat{\mu^{*n}} = \widehat\mu^{\,n}, \qquad p^{(n)}(x,y) = \int_{\widehat G}\chi(x^{-1}y)\,\widehat\mu(\chi)^n\,d\chi
$$

in the sense of the Fourier inversion theorem — the identity is one of densities with respect to the Haar measure, the dual measure being normalised so that inversion holds — and the walk is recurrent if and only if

$$
\int_{[-\pi,\pi]^d}\frac{d\theta}{1-\operatorname{Re}\widehat\mu(\theta)} = +\infty
$$

in the case $G = \mathbb{Z}^d$ with $\mu$ symmetric, aperiodic and of finite support (**Chung–Fuchs criterion**).

The Fourier description is the probabilistic content of the convolution theorem of *Harmonic Analysis on Groups*: the sharpening of the $n$-fold convolution is the $n$-th power of the transform, and the return probabilities are the Fourier coefficients of that power. The Chung–Fuchs criterion reads the recurrence off the singularity of the transform at the identity character: the walk on $\mathbb{Z}^d$ has $\widehat\mu(\theta) = 1 - c|\theta|^2 + O(|\theta|^4)$ near $\theta = 0$, so the integral diverges for $d\leq2$ and converges for $d\geq3$, recovering Pólya's theorem. The same computation in the group setting — the singularity of the Fourier transform at the trivial representation — is the criterion for the recurrence of the walk on a general group.

### The Compact Case and Peter–Weyl

**Theorem (return probabilities on a compact group).** Let $K$ be a compact group with **normalised** Haar measure $m$ and let $\mu$ be a probability measure on $K$; let $\operatorname{Irr}(K)$ be the set of irreducible unitary representations up to equivalence, with dimensions $d_\pi$.

**(a) Density form.** If $\mu$ is absolutely continuous with density $\varphi = d\mu/dm \in L^2(K,m)$, then $\mu^{*n}$ has density $\varphi^{*n}$ with respect to $m$ and

$$
\varphi^{*n}(e) = \sum_{\pi\in\operatorname{Irr}(K)}d_\pi\operatorname{tr}\bigl(\widehat\varphi(\pi)^n\bigr), \qquad \widehat\varphi(\pi) = \int_K\pi(g)\varphi(g)\,dm(g),
$$

the series converging in $L^2(K,m)$; for $n\ge2$ the density $\varphi^{*n}$ is continuous, so the identity holds at the identity as an equality of numbers.

**(b) Finite groups.** If $K = G$ is finite, so that $m$ is the normalised counting measure, then for **every** probability measure $\mu$ on $G$, with $\widehat\mu(\pi) = \sum_{g\in G}\mu(g)\pi(g)$,

$$
\mu^{*n}(\{e\}) = \frac{1}{|G|}\sum_{\pi\in\operatorname{Irr}(G)}d_\pi\operatorname{tr}\bigl(\widehat\mu(\pi)^n\bigr),
$$

the factor $|G|$ being the ratio of the density to the mass in the absolutely continuous case; the discrete case, where the Haar measure is counting measure, has $p^{(n)}(e) = \mu^{*n}(\{e\})$ without a factor.

If the support of $\mu$ generates a dense subgroup then $\mu^{*n}\to m$ weakly; if moreover $\mu$ is not supported on a coset of a closed subgroup, then the convergence is exponentially fast with rate governed by $\Lambda = \sup_{\pi\neq1}\|\widehat\mu(\pi)\| < 1$:

$$
\left\|\mu^{*n}-m\right\|_{\mathrm{TV}} \leq C\,\Lambda^n.
$$

*Proof.* (a) The Fourier transform of $\mu^{*n}$ is $\widehat\varphi(\pi)^n$, and the value of the density at the identity is the inverse Fourier transform, which is the sum of the traces weighted by the dimensions by *Analysis on Compact Groups*. (b) The second identity requires no regularity of $\mu$: the Dirac mass at the identity expands as $\delta_e(g) = \frac{1}{|G|}\sum_\pi d_\pi\chi_\pi(g)$ by the orthogonality relations for the characters of a finite group, and pairing this with $\mu^{*n}$ gives $\sum_g\mu^{*n}(g)\delta_e(g) = \frac{1}{|G|}\sum_\pi d_\pi\operatorname{tr}\bigl(\sum_g\mu^{*n}(g)\pi(g)\bigr) = \frac{1}{|G|}\sum_\pi d_\pi\operatorname{tr}(\widehat\mu(\pi)^n)$. The two forms agree when $\mu$ is absolutely continuous, since then $|G|\mu$ is its density. The convergence is the case of the mixing of a Markov chain on a compact group, and the exponential rate is the spectral gap in the representation ring; the constant $\Lambda$ is the analogue of the spectral radius on the nontrivial part of the spectrum. $\square$

The second form is checked at the extreme case $\mu = \delta_e$, where $\widehat\mu(\pi) = I$ for every $\pi$ and the sum computes $\frac{1}{|G|}\sum_\pi d_\pi^2 = 1$, the mass; the density form would compute the density $|G|$ there, and the two differ by the factor $|G| = |K|$ by which the Haar measure of a finite group differs from counting measure.

The theorem is the exact compact analogue of the abelian Fourier description: the dual group is replaced by the set of irreducible representations, the characters by their traces, and the integral by the sum with the dimension weights. It is the reason the mixing of a random walk on a finite group is computed from the character table, and it is the harmonic-analysis mechanism behind the **cutoff phenomenon**: when the Fourier coefficients are small except for a family of representations whose dimensions grow, the convergence to Haar is abrupt, with the transition at the time at which the largest Fourier coefficient reaches $e^{-1}$.

### The General Case: Spectral Measures

**Theorem (spectral description).** Let $G$ be a discrete group, $\mu$ a symmetric probability measure, and $P_\mu$ the convolution operator on $\ell^2(G)$. Then $P_\mu$ is a self-adjoint contraction, and the **spectral measure** $\sigma$ of the vector $\delta_e$ is a probability measure on $[-1,1]$ with

$$
p^{(2n)}(e) = \langle P_\mu^{2n}\delta_e,\delta_e\rangle = \int_{-1}^{1}\lambda^{2n}\,d\sigma(\lambda).
$$

The support of $\sigma$ is contained in $[-\rho,\rho]$, where $\rho$ is the spectral radius of $P_\mu$, and the walk is transient if and only if $\rho<1$.

*Proof.* The self-adjointness is the proposition above; the spectral theorem of *Banach and Hilbert Spaces* gives the spectral measure and the moment formula. The transience criterion: $\sum_n p^{(n)}(e)$ diverges precisely when the sums $\int\sum_n\lambda^n d\sigma$ diverge, which happens exactly when $1$ is in the support of $\sigma$, that is, when $\rho = 1$; and $\rho = \|P_\mu\|$. $\square$

The spectral description is the general form of the Fourier description, valid without any structure on the group: the walk is transient precisely when the convolution operator has norm strictly below one, and its return probabilities are the moments of a measure on the spectrum. The measure $\sigma$ is the spectral measure of the group von Neumann algebra of *Noncommutative Harmonic Analysis*, and the problem of determining the spectrum of $P_\mu$ for a general group is the problem of the Plancherel theory of *The Plancherel Theorem*, which for non-type-I or non-amenable groups has no explicit form.

## Recurrence, Transience and Amenability

### The Recurrence Criterion

**Theorem (recurrence criterion on a group).** Let $G$ be a countable group and $\mu$ a non-degenerate probability measure. Then the walk is recurrent — every state is visited infinitely often a.s. — if and only if $\sum_{n\ge0}p^{(n)}(e) = +\infty$, and it is transient otherwise; in the transient case the Green function is finite everywhere and $\mathbb{E}_e[N_e] = (1-\mathbb{P}_e(\tau_e^+<\infty))^{-1}$.

*Proof.* The criterion is the recurrence criterion of *Markov Chains and Processes* specialised to a translation-invariant chain: the walk is irreducible by the non-degeneracy and the returns to the identity are the events $X_n = e$, governed by $p^{(n)}(e)$; irreducibility makes the classification of one state apply to all, and the dichotomy follows from the Borel–Cantelli lemma of *Independence and Conditional Expectation* applied to the independent blocks between returns. $\square$

### Kesten's Theorem

**Theorem (Kesten).** Let $G$ be a finitely generated group, and let $\mu$ be a symmetric probability measure on $G$ with finite support generating $G$. Then

$$
\rho(P_\mu) = 1 \quad \Longleftrightarrow \quad G \text{ is amenable},
$$

and $\rho(P_\mu)<1$ otherwise; in particular the random walk is recurrent exactly when $G$ is amenable, and the return probabilities decay exponentially exactly when $G$ is non-amenable.

*Proof (sketch).* If $G$ is amenable, the Følner condition provides finite sets $F_n$ whose boundary is small relative to their size, and testing the operator against the normalised indicator of $F_n$ gives $\|P_\mu\mathbf{1}_{F_n}\|_2/\|\mathbf{1}_{F_n}\|_2\to1$, so $\|P_\mu\| = 1$. If $G$ is non-amenable, the representation theory of *Noncommutative Harmonic Analysis* gives a lower bound for the spectral projection of $P_\mu$ on the regular representation — the Furstenberg–Kesten estimate — producing $\varepsilon>0$ with $\|P_\mu\|\leq1-2\varepsilon$: the operator has a spectral gap. $\square$

Kesten's theorem is the meeting point of the two categories of this part: the amenability of a group, a purely algebraic condition of Part II, is equivalent to the analytic statement that the convolution operator has norm one, and to the probabilistic statement that the walk is recurrent. Its group-algebra form — the criterion $\mathbf{1} \in \operatorname{Spec}_{\ell^2(G)}(\mu)$ in the reduced group C*-algebra — is the statement that the trivial representation is not isolated in the support of the regular representation, and it is the reason the random walk is the standard probe of the representation theory of a group. The free group example above is the case in which the gap is explicit: $\rho = \sqrt3/2$ and the estimate $\|P_\mu\|\leq\rho$ is an equality.

**Theorem (Avez).** Let $G$ be a finitely generated group and $\mu$ a symmetric non-degenerate probability measure of finite first moment. The **asymptotic entropy** $h(\mu) = \lim_{n\to\infty}-\frac1n\log\mu^{*n}(X_n)$ exists a.s., and $h(\mu) = 0$ if and only if $G$ is amenable.

Avez's theorem is the information-theoretic counterpart of Kesten's: the non-amenability of the group is exactly the positivity of the rate at which the walk reveals information about its trajectory, and the entropy and the spectral radius are related by the inequality $h(\mu)\ge-\log\rho(P_\mu)$ of Guivarc'h, with equality for the free groups. The entropy of the walk is the arithmetic of the growth of the group as seen by the walk.

### Growth and the Return Probabilities

**Theorem (Varopoulos).** Let $G$ be a finitely generated group of polynomial growth of degree $d$ — that is, $|B(e,n)| \asymp n^d$ for the balls of the Cayley graph — and let $\mu$ be a symmetric non-degenerate probability measure of finite support. Then

$$
p^{(2n)}(e) \asymp n^{-d/2},
$$

so that the walk is recurrent for $d\leq2$ and transient for $d\geq3$.

*Proof (sketch).* The upper bound is the Nash inequality for the group: the Gagliardo–Nirenberg-type inequality relating the $L^2$ norm, the Dirichlet form $\mathcal{E}(f,f) = \frac12\sum_{g}\mu(g)\sum_x|f(xg)-f(x)|^2$ and the $L^1$ norm, together with the polynomial volume growth; the lower bound is Carne's estimate, from the local central limit theorem on the group. $\square$

Varopoulos's theorem is the geometric form of the recurrence criterion, and it explains the dimension dependence of Pólya's theorem as the polynomial growth of $\mathbb{Z}^d$: the return probability is the reciprocal of the square root of the volume of the ball, and the walk is recurrent exactly when the volume grows at most quadratically. The result holds for all groups of polynomial growth (which, by Gromov's theorem, are the virtually nilpotent groups, treated in *Combinatorial Group Theory*) and for the nilpotent and solvable groups by the local limit theory; for the groups of exponential growth the return probabilities decay exponentially by Kesten's theorem, and the precise rate is the spectral radius.

## Harmonic Functions and the Poisson Boundary

**Definition.** A measurable function $f : G\to\mathbb{R}$ is **$\mu$-harmonic** if $P_\mu f = f$, that is, $f(x) = \int f(xg)\,d\mu(g)$ for all $x$; the bounded $\mu$-harmonic functions form a closed subspace $\mathcal{H}^\infty(G,\mu)$ of $L^\infty(G)$. The group has the **Liouville property** for $\mu$ if every bounded $\mu$-harmonic function is constant.

**Theorem (Choquet–Deny).** Let $G$ be a locally compact abelian group and $\mu$ a probability measure on $G$ whose support generates a dense subgroup. Then every bounded continuous $\mu$-harmonic function is constant.

The Choquet–Deny theorem is the abelian Liouville theorem, and it is the probabilistic form of the fact that the only bounded eigenfunctions of the convolution operator at the eigenvalue $1$ are the constants — the statement that the trivial character is the only character of modulus one that is $\mu$-invariant. For the non-abelian groups the picture is entirely different.

**Theorem (Poisson boundary; Furstenberg, Kaimanovich–Vershik).** Let $G$ be a countable group and $\mu$ a non-degenerate probability measure. There is a measure space $(B,\nu)$ — the **Poisson boundary** — and an isometric isomorphism

$$
\mathcal{H}^\infty(G,\mu) \cong L^\infty(B,\nu),
$$

sending a bounded harmonic function to its boundary values; the boundary is realised as the space of ergodic components of the tail $\sigma$-algebra of the walk, and the harmonic function is recovered by the **Poisson formula** $f(x) = \int_B \hat f\,d\nu_x$, where $\nu_x$ is the law of the limit of the walk started at $x$. The boundary is trivial — and the Liouville property holds — if and only if the walk is trivial in the sense of a trivial tail $\sigma$-algebra.

**Theorem (Dynkin; the Liouville property).** Let $G$ be a finitely generated group of polynomial growth and $\mu$ a symmetric non-degenerate probability measure of finite support. Then $G$ has the Liouville property for $\mu$: every bounded $\mu$-harmonic function is constant.

The Poisson boundary is the object that measures the failure of the Liouville property, and it is the natural home of the harmonic analysis of a non-amenable group: for the free group $\mathbb{F}_2$ it is the space of infinite reduced words with the harmonic measure, and for the semisimple Lie groups it is the Furstenberg boundary $G/P$ of the associated symmetric space. The boundary theory is the analytic side of the representation theory of *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*, and its use in the rigidity and the equidistribution of the homogeneous flows is *Homogeneous Dynamics* and *Ratner's Theorems*.

## Summary

A random walk on a group is the sequence of products of independent group elements with a common step distribution $\mu$, and its law at time $n$ is the convolution power $\mu^{*n}$; its transition operator is the right convolution by $\mu$, an operator whose powers are the convolutions by the iterates and whose spectral theory is that of the group von Neumann algebra. On an abelian group the Fourier transform turns the convolution powers into the powers of the multiplier, and the return probabilities into the Fourier coefficients of $\widehat\mu^{\,n}$, with the Chung–Fuchs criterion deciding the recurrence by the singularity of the transform at the trivial character. On a compact group the Peter–Weyl theorem replaces the Fourier integral by the sum over the irreducible representations weighted by their dimensions, and the convergence of the walk to the Haar measure and the cutoff phenomenon are read from the largest nontrivial Fourier coefficient. In general the spectral measure of the convolution operator computes the return probabilities as moments, and the walk is transient exactly when the spectral radius is below one.

The classification of the walks is the classification of the groups. The walk on a countable group is recurrent if and only if the return probabilities are not summable, and Kesten's theorem identifies this with the amenability of the group: for a symmetric finitely supported non-degenerate measure, the spectral radius is one exactly on the amenable groups, so the random walk is recurrent exactly on the amenable groups and transient exactly on the non-amenable ones. Avez's theorem gives the information-theoretic form: the asymptotic entropy of the walk vanishes exactly on the amenable groups. Varopoulos's theorem gives the geometric form: on a group of polynomial growth of degree $d$ the return probability is of order $n^{-d/2}$, so the walk on a group of growth at most quadratic is recurrent, and the walks on the virtually nilpotent groups, the free groups and the exponential-growth groups are transient with exponentially decaying return probabilities. The bounded harmonic functions of the walk form the space $L^\infty$ of the Poisson boundary, which is trivial for the abelian and the polynomial-growth groups and non-trivial for the non-amenable ones, and which for the semisimple groups is the Furstenberg boundary of the associated symmetric space.

The article is the intersection of the two categories of this part. From the harmonic side it uses *Harmonic Analysis on Groups*, *Analysis on Compact Groups*, *The Peter–Weyl Theorem*, *The Convolution Algebra $L^1(G)$*, *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*; from the probabilistic side it uses *Markov Chains and Processes* with the surrounding block of probability articles, and it borders the ergodic theory of *Ergodic Theory of Group Actions* and *Ergodic Theory*, the equidistribution of *Equidistribution*, the homogeneous dynamics of *Homogeneous Dynamics* and *Ratner's Theorems*, the amenability and growth of Part II and Part I, and the arithmetic model of *Probabilistic Number Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$, $dx$ | Group, identity, Haar measure |
| $\mu$, $\mu^{*n}$ | Step distribution and its $n$-fold convolution power |
| $X_n = g_1\cdots g_n$ | Random walk position |
| $p^{(n)}(x,y)$, $p^{(n)}(e)$ | Transition kernel; return probability (a mass for a discrete group, a density for a compact one) |
| $P_\mu f(x)=\int f(xg)d\mu(g)$ | Transition operator = right convolution by $\mu$ |
| $\check\mu(A)=\mu(A^{-1})$ | Reflection of the measure; $P_\mu^*=P_{\check\mu}$ |
| symmetric, non-degenerate | $\mu(A)=\mu(A^{-1})$; support generates a dense subgroup |
| $\widehat\mu(\chi)$, $\widehat\varphi(\pi)$ | Abelian Fourier transform; compact transform of the density $\varphi$ w.r.t. normalised Haar $m$ |
| Chung–Fuchs | recurrence iff $\int d\theta/(1-\operatorname{Re}\widehat\mu(\theta))=\infty$ |
| $\rho=\rho(P_\mu)$ | Spectral radius; $\rho=1$ iff amenable (Kesten) |
| $h(\mu)$ (Avez) | Asymptotic entropy; $h=0$ iff amenable |
| Varopoulos | polynomial growth degree $d$ $\Rightarrow$ $p^{(2n)}(e)\asymp n^{-d/2}$ |
| $\sigma$ | Spectral measure of $P_\mu$ at $\delta_e$; $p^{(2n)}(e)=\int\lambda^{2n}d\sigma$ |
| $m$, $\varphi=d\mu/dm$ | Normalised Haar measure of a compact group and the density of $\mu$ |
| $\Lambda=\sup_{\pi\ne1}\|\widehat\mu(\pi)\|$ | Rate of exponential mixing to $m$ on a compact group |
| Green function $G(x,y)$ | $\sum_np^{(n)}(x,y)$ |
| $\mathcal{H}^\infty(G,\mu)$ | Bounded $\mu$-harmonic functions |
| Poisson boundary, $\nu_x$ | isometric $L^\infty(B,\nu)$; limit law of the walk |
| Liouville property | every bounded harmonic function is constant |
| cutoff (Diaconis–Shahshahani) | abrupt convergence to Haar on a finite group |

## Further Reading

- Frank Spitzer, *Principles of Random Walk* (Springer, 2nd edition, 1976), for the classical theory on $\mathbb{Z}^d$ and the Chung–Fuchs criterion.
- Wolfgang Woess, *Random Walks on Infinite Graphs and Groups* (Cambridge University Press, 2000), for the recurrence and transience criteria on graphs and groups.
- Harry Kesten, "Full Banach mean values on countable groups", *Mathematica Scandinavica* 7 (1959), 146–156, for the spectral radius and amenability.
- Robert Azencott, "Espaces de Poisson des groupes localement compacts", *Springer Lecture Notes in Mathematics* 148 (1970), for the Poisson boundary and the Liouville property.
- Vadim A. Kaimanovich and Anatoly M. Vershik, "Random walks on discrete groups: boundary and entropy", *Annals of Probability* 11 (1983), 457–490, for the Poisson boundary and the entropy criterion.
- Yves Guivarc'h, "Sur la loi des grands nombres et le rayon spectral d'une marche aléatoire", *Astérisque* 74 (1980), 47–98, for the growth, the entropy and the spectral radius.
- Nicholas Th. Varopoulos, "Isoperimetric inequalities and Markov chains", *Journal of Functional Analysis* 63 (1985), 215–239, for the return probabilities and polynomial growth.
- Gustave Choquet and Jacques Deny, "Sur l'équation de convolution $\mu=\mu*\sigma$", *Comptes Rendus de l'Académie des Sciences* 250 (1960), 799–801, for the abelian Liouville theorem.
- Persi Diaconis, *Group Representations in Probability and Statistics* (Institute of Mathematical Statistics, 1988), for the Fourier analysis of walks on finite groups and the cutoff phenomenon.
- Persi Diaconis and Mehrdad Shahshahani, "Generating a random permutation with random transpositions", *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete* 57 (1981), 159–179, for the cutoff of the transposition walk.
- Harry Furstenberg, "Noncommuting random products", *Transactions of the American Mathematical Society* 108 (1963), 377–428, for the boundary theory of products of random matrices and the harmonic functions.
