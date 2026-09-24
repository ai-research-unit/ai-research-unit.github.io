
# __Interpolation Theory__

## Introduction

The Banach spaces that arise in analysis rarely occur alone: the spaces $L^p$ form a one-parameter family, the Sobolev spaces $W^{k,p}$ a two-parameter family, and the analytic properties of an operator are usually known at the two ends of such a family and wanted in the middle. Interpolation theory answers the question that this situation poses. Given two Banach spaces $A_0$ and $A_1$ sitting inside a common ambient space, it constructs the spaces that lie *between* them, and it shows that a linear map bounded on the two endpoints is automatically bounded on every constructed space, with a norm controlled by the two endpoint norms. The construction is a *functor*: it acts on the spaces and on the maps at once.

Two constructions do the work, and the article is organised around them. The **complex method** embeds $A_0$ and $A_1$ as the two edges of a strip in $\mathbb{C}$ and takes the values of bounded analytic functions at an interior point; it is the source of the Riesz–Thorin theorem and of the interpolation of the Fourier transform. The **real method** measures how well an element of $A_0+A_1$ splits into a sum of an element of $A_0$ and an element of $A_1$, and integrates that measure against a weight; it is the source of the Lorentz spaces and of the interpolation of Sobolev spaces, and it produces a second parameter $q$ that the complex method does not see.

Throughout, $\mathbb{K}$ denotes $\mathbb{R}$ or $\mathbb{C}$, all linear spaces are over $\mathbb{K}$, and $X$, $Y$ are Banach spaces. The word *operator* means a bounded linear map; the operator norm and the dual are those of the companion article *Banach and Hilbert Spaces*, and the completeness, quotient and dual-space facts that the constructions need are those of *Normed and Banach Spaces*; the locally convex background, in particular the completeness of the spaces of analytic functions that the complex method uses, is that of *Locally Convex Spaces*. The scalar theory of analytic functions is that of *Analytic Functions and Power Series*, while analytic functions with values in a Banach space are defined in line below, since the complex method cannot dispense with them. Integration is that of *Measure Theory and Integration*. The weak-derivative Sobolev spaces and their embedding theorems belong to the extension of this Part devoted to differential equations; here they are used only through the equivalent Fourier definition, which is recalled and is self-contained. The boundary of the article is deliberate: the interpolation of operators on a single Hilbert space, and the interpolation of abstract operator algebras, are not treated.

No physics is invoked.

## The Interpolation Problem

### Compatible Couples and Intermediate Spaces

**Definition.** A **compatible couple** of Banach spaces is a pair $(A_0,A_1)$ of Banach spaces, with norms $\|\cdot\|_{A_0}$ and $\|\cdot\|_{A_1}$, both continuously embedded in a common Hausdorff topological vector space $\mathcal{X}$. In the situations of this article $A_0 \cap A_1$ is dense in each $A_i$, and the two norms are comparable there; the density is assumed when it is needed, and is not a consequence of the compatibility.

The ambient space is a bookkeeping device; all statements below are invariant under the choice of a larger ambient space. Two Banach spaces then sit at the extremes of the couple.

**Proposition.** Let $(A_0,A_1)$ be a compatible couple. Then

$$
A_0 \cap A_1 \quad \text{with} \quad \|a\|_{A_0\cap A_1}=\max(\|a\|_{A_0},\|a\|_{A_1}),
\qquad
A_0 + A_1 \quad \text{with} \quad \|a\|_{A_0+A_1}=\inf_{a=a_0+a_1}\bigl(\|a_0\|_{A_0}+\|a_1\|_{A_1}\bigr)
$$

are Banach spaces, and $A_0 \cap A_1 \subseteq A_i \subseteq A_0+A_1$ with continuous inclusions.

*Proof.* The maximum norm makes $A_0\cap A_1$ isometrically a closed subspace of the Banach space $A_0 \oplus_\infty A_1$, hence complete. For the sum, the infimum is over all decompositions; the quotient of $A_0 \oplus_1 A_1$ by the closed subspace $\{(a,-a):a \in A_0\cap A_1\}$ is a Banach space by the quotient theorem of *Normed and Banach Spaces*, and the natural map from this quotient to $A_0+A_1$ is a linear isometry onto its image, so the sum is complete. The inclusions are estimatewise immediate. $\square$

**Definition.** An **intermediate space** for $(A_0,A_1)$ is a Banach space $A$ with continuous inclusions $A_0 \cap A_1 \subseteq A \subseteq A_0+A_1$.

**Example.** For $1 \le p \le \infty$ the pair $(L^1(\mu),L^\infty(\mu))$ on a $\sigma$-finite measure space is compatible, both spaces lying in the space of measurable functions; $L^p(\mu)$ is intermediate for every $p$. Likewise $(\ell^1,\ell^\infty)$ is compatible, both spaces lying in the space of all sequences, and $\ell^p$, $c_0$ and the space of finitely supported sequences are intermediate. The pair $(C[0,1],C^1[0,1])$, with the supremum norms of the function and of its derivative, is compatible inside $C[0,1]$.

### Interpolation Functors

**Definition.** An **interpolation functor** assigns to every compatible couple $(A_0,A_1)$ an intermediate space $F(A_0,A_1)$, and to every linear map $T$ that is bounded from $A_0$ to $B_0$ and from $A_1$ to $B_1$ a bounded map $F(T)$ from $F(A_0,A_1)$ to $F(B_0,B_1)$ agreeing with $T$ on $A_0\cap A_1$, in such a way that the assignment respects composition and the identity. The functor is of **exponent** $\theta \in [0,1]$ if

$$
\|T\|_{F(A_0,A_1)\to F(B_0,B_1)} \;\le\; \|T\|_{A_0\to B_0}^{\,1-\theta}\,\|T\|_{A_1\to B_1}^{\,\theta},
$$

and it is **exact** if the inequality holds with constant $1$.

Both constructions below are exact functors of exponent $\theta$; the exponent is the position at which the interpolated space is taken. The two basic inequalities that every interpolation functor satisfies are the **convexity inequality** and the **fundamental lemma** that the norm on $A_0\cap A_1$ controls the interpolated norm.

### The Convexity Inequality

**Proposition.** If $F$ is a functor of exponent $\theta$, then for all $a \in A_0\cap A_1$,

$$
\|a\|_{F(A_0,A_1)} \le \|a\|_{A_0}^{1-\theta}\|a\|_{A_1}^{\theta}.
$$

*Proof.* Apply the functor to the one-dimensional operator $t \mapsto ta$ from $\mathbb{K}$ into $\mathcal{X}$, bounded with the two norms; the value at $1$ is $a$, and the norm of the operator $\mathbb{K}\to A_i$ is $\|a\|_{A_i}$. $\square$

The inequality is the elementary half of the theory and shows that the interpolated norm is honest: it is squeezed between the norms of the couple. The substantive content of a method is that this elementary estimate persists for the interpolated norms of operators, where the target is not one-dimensional.

## The Complex Method

### Analytic Functions with Values in a Banach Space

**Definition.** Let $A$ be a Banach space and $U \subseteq \mathbb{C}$ open. A function $f:U \to A$ is **analytic** if for every $z \in U$ the limit

$$
f'(z)=\lim_{h \to 0}\frac{f(z+h)-f(z)}{h}
$$

exists in the norm of $A$. Equivalently, $f$ is analytic if it is weakly analytic, that is, if $z \mapsto \varphi(f(z))$ is analytic for every $\varphi \in A^*$; the two notions agree because Cauchy's integral formula for a scalar analytic function may be applied to the bounded functional $\varphi$, and then utilised with a norming functional to recover the norm estimate for $f'$.

**Theorem (maximum modulus).** If $f$ is analytic on $U$ and continuous on $\overline U$ with $U$ bounded, then $\|f\|$ attains its maximum on the boundary $\partial U$; more precisely $\sup_U\|f\|\le\sup_{\partial U}\|f\|$.

*Proof.* Apply the scalar maximum modulus principle to $z\mapsto\varphi(f(z))$ for each $\varphi \in A^*$ with $\|\varphi\|\le1$; this gives $\|\varphi(f(z))\|\le\sup_{\partial U}\|\varphi(f)\|$, and taking the supremum over such $\varphi$ and using $\|a\|=\sup_{\|\varphi\|\le1}|\varphi(a)|$, which is a corollary of Hahn–Banach in *Normed and Banach Spaces*, gives the result. $\square$

**Lemma (three-lines).** Let $S=\{z:0<\operatorname{Re}z<1\}$ and let $f$ be bounded and continuous on $\overline S$ and analytic on $S$. Suppose $\|f(it)\| \le M_0$ and $\|f(1+it)\| \le M_1$ for all real $t$. Then $\|f(\theta)\| \le M_0^{1-\theta}M_1^{\theta}$ for $0<\theta<1$.

*Proof.* For $\varepsilon>0$ set $f_\varepsilon(z)=e^{\varepsilon(z^2-1)}f(z)$ and $g(z)=f_\varepsilon(z)M_0^{z-1}M_1^{-z}$. On the two boundary lines $|f_\varepsilon(z)|\le e^{-\varepsilon t^2}M_i$ and $|M_0^{z-1}M_1^{-z}|=M_i^{-1}$, so $\|g\|\le e^{-\varepsilon t^2}\le1$ there, and $g\to0$ at the horizontal ends of the strip; the maximum modulus principle applied to $z\mapsto\varphi(g(z))$ for $\varphi\in A^*$ therefore gives $\|g(z)\|\le1$ throughout the strip. Hence $\|f(\theta)\|\le M_0^{1-\theta}M_1^{\theta}e^{\varepsilon(1-\theta^2)}$, and letting $\varepsilon\to0$ gives the claim, the interpolation of the two endpoint bounds and not merely the larger of them coming from the exponential factor $M_0^{z-1}M_1^{-z}$. $\square$

### The Complex Interpolation Space

**Definition.** Let $(A_0,A_1)$ be a compatible couple. Let $\mathcal A(A_0,A_1)$ be the space of functions $f:\overline S \to A_0+A_1$ that are bounded and continuous on the closed strip, analytic on the open strip, and satisfy $f(it) \in A_0$, $f(1+it) \in A_1$ for all real $t$, with finite norm

$$
\|f\|_{\mathcal A}=\max\Bigl(\sup_{t \in \mathbb{R}}\|f(it)\|_{A_0},\ \sup_{t \in \mathbb{R}}\|f(1+it)\|_{A_1}\Bigr).
$$

For $0<\theta<1$ the **complex interpolation space** is

$$
[A_0,A_1]_\theta=\bigl\{a \in A_0+A_1:\ a=f(\theta) \text{ for some } f \in \mathcal A(A_0,A_1)\bigr\},
\qquad
\|a\|_\theta=\inf_{f(\theta)=a}\|f\|_{\mathcal A}.
$$

**Theorem.** $\mathcal A(A_0,A_1)$ is a Banach space, $[A_0,A_1]_\theta$ is a Banach space, the inclusions $A_0\cap A_1 \subseteq [A_0,A_1]_\theta \subseteq A_0+A_1$ are continuous, and the assignment $(A_0,A_1) \mapsto [A_0,A_1]_\theta$ is an exact interpolation functor of exponent $\theta$.

*Proof (sketch).* The map $f \mapsto (f|_{i\mathbb R},f|_{1+i\mathbb R})$ is an isometry of $\mathcal A(A_0,A_1)$ onto a closed subspace of the Banach space $C_b(\mathbb R,A_0) \times C_b(\mathbb R,A_1)$: the closedness is Montel's theorem, that a locally bounded sequence of analytic functions has a locally uniformly convergent subsequence, which supplies the analytic extension of the limit of a Cauchy sequence. Hence $\mathcal A$ is complete; the evaluation $f \mapsto f(\theta)$ is bounded by the three-lines lemma, $\|f(\theta)\| \le \|f\|_{\mathcal A}$, so its image is a Banach space under the quotient norm defining $\|\cdot\|_\theta$. The inclusions follow from the constant functions and from the estimate of the convexity inequality. For the functoriality, let $T$ be bounded from $A_i$ to $B_i$ with norm $M_i$, and let $a \in [A_0,A_1]_\theta$; choose $f \in \mathcal A(A_0,A_1)$ with $f(\theta)=a$ and $\|f\|_{\mathcal A}\le\|a\|_\theta+\varepsilon$. Then $T \circ f \in \mathcal A(B_0,B_1)$ with norm at most $\max(M_0,M_1)\|f\|_{\mathcal A}$; to obtain the exact exponent, rescale and apply the three-lines lemma to $z \mapsto M_0^{z-1}M_1^{-z}T(f(z))$ whose endpoint norms are at most $\|f\|_{\mathcal A}$. Hence $\|Ta\|_\theta \le M_0^{1-\theta}M_1^{\theta}\|a\|_\theta$. $\square$

**Example.** For a compatible couple and $a \in A_0\cap A_1$ the constant function gives the convexity inequality $\|a\|_\theta \le \|a\|_{A_0}^{1-\theta}\|a\|_{A_1}^{\theta}$. If $A_0=A_1=A$ with equal norms then $[A,A]_\theta=A$ isometrically. If $A_1 \subseteq A_0$ with the inclusion of norm at most $1$, then $[A_0,A_1]_\theta$ contains $A_1$ and is contained in $A_0$.

### The Riesz–Thorin Theorem

The first substantial consequence of the complex method is that boundedness at two $L^p$ endpoints propagates to the whole segment.

**Theorem (Riesz–Thorin).** Let $(X,\mu)$ and $(Y,\nu)$ be $\sigma$-finite measure spaces, let $1 \le p_0,p_1,q_0,q_1 \le \infty$, and let $T$ be a linear map bounded from $L^{p_0}(\mu)$ to $L^{q_0}(\nu)$ with norm $M_0$ and from $L^{p_1}(\mu)$ to $L^{q_1}(\nu)$ with norm $M_1$. For $0<\theta<1$ put

$$
\frac1p=\frac{1-\theta}{p_0}+\frac{\theta}{p_1}, \qquad \frac1q=\frac{1-\theta}{q_0}+\frac{\theta}{q_1}.
$$

Then $T$ maps $L^p(\mu)$ boundedly to $L^q(\nu)$ with

$$
\|T\|_{L^p \to L^q} \le M_0^{1-\theta}M_1^{\theta}.
$$

*Proof (sketch).* The functional $T$ is known on the dense subspace of simple functions. Write $S=\{z:0<\operatorname{Re}z<1\}$ and define, for a simple function $u$ and $z \in \overline S$, the function $G(z)=T\bigl(|u|^{p/p(z)}\operatorname{sgn}u\bigr)$ and pair it against $|v|^{q'/q'(z)}\operatorname{sgn}v$ for a simple $v$, where $1/p(z)=(1-z)/p_0+z/p_1$ and $1/q'(z)=(1-z)/q_0'+z/q_1'$. Then $H(z)=\int G(z)v$ is bounded and continuous on the strip and analytic inside, with $|H(it)| \le M_0\|u\|_p^{p/p_0}\|v\|_{q'}^{q'/q_0'}$ and $|H(1+it)| \le M_1\|u\|_p^{p/p_1}\|v\|_{q'}^{q'/q_1'}$, the two powers of $\|v\|_{q'}$ being the $L^{q_0'}$ and $L^{q_1'}$ norms of $|v|^{q'/q'(z)}$ on the boundary lines; the three-lines lemma, whose exponent $\theta$ combines the four powers into $\|u\|_p^{(1-\theta)p/p_0+\theta p/p_1}=\|u\|_p$ and $\|v\|_{q'}^{(1-\theta)q'/q_0'+\theta q'/q_1'}=\|v\|_{q'}$, gives $|H(\theta)| \le M_0^{1-\theta}M_1^{\theta}\|u\|_p\|v\|_{q'}$, and taking the supremum over simple $v$ of unit $L^{q'}$ norm and then over simple $u$ gives the claim on a dense subspace, hence on $L^p$ by continuity. $\square$

**Corollary (interpolation of $L^p$).** For $1 \le p_0<p_1 \le \infty$ and $0<\theta<1$,

$$
[L^{p_0}(\mu),L^{p_1}(\mu)]_\theta=L^p(\mu), \qquad \frac1p=\frac{1-\theta}{p_0}+\frac{\theta}{p_1},
$$

with equivalence of norms; in particular $[L^1,L^\infty]_\theta=L^{1/(1-\theta)}$. The same holds for the couple $(\ell^{p_0},\ell^{p_1})$ of sequence spaces, and the identity is a statement about the two sets and their norms, not merely about the underlying vector spaces.

*Proof.* The inclusion $[L^{p_0},L^{p_1}]_\theta \subseteq L^p$ with norm at most $1$ is the Riesz–Thorin theorem applied to the identity. For the reverse inclusion, the density of the simple functions in each $L^{p_i}$ makes the dual of the complex space the complex space of the dual couple, $([A_0,A_1]_\theta)^*=[A_0^*,A_1^*]_\theta$, and the interpolation theorem applied to the dual couple $(L^{p_0'},L^{p_1'})$, with $\frac1{p'}=\frac{1-\theta}{p_0'}+\frac{\theta}{p_1'}$, gives $\|v\|_{[A_0^*,A_1^*]_\theta}\le\|v\|_{L^{p'}}$. Hence, for $a \in L^p$, the dual characterisation of the norm of a complex interpolation space gives $\|a\|_{L^p}=\sup\{|\langle a,v\rangle|:\|v\|_{L^{p'}}\le1\}\le\sup\{|\langle a,v\rangle|:\|v\|_{[A_0^*,A_1^*]_\theta}\le1\}=\|a\|_\theta$, with $1<p<\infty$ throughout because $p_0<p_1$ and $0<\theta<1$. The sequence case is the counting measure. $\square$

**Corollary (Hausdorff–Young).** Let $1 \le p \le 2$ and $1/p+1/q=1$. The Fourier transform $\mathcal F$ on $\mathbb{R}^n$, bounded on $L^1$ with norm $1$ and unitary on $L^2$ up to the standard constant, maps $L^p$ boundedly into $L^q$; interpolating at $\theta$ with $1/q=\theta/2$ and $1/p=1-\theta/2$ recovers $1/p+1/q=1$, and the bound is $1$.

The corollary is the classical application: the two endpoint estimates are trivial and the interpolated estimate is not. The transform theory itself, and the conventions for the constant, belong to *Fourier Analysis on Euclidean Spaces*, earlier in this Part.

**Theorem (Stein's interpolation of analytic families).** Let $S$ be the strip and let $\{T_z\}$ be a family of linear maps such that $z \mapsto \int (T_zf)g$ is analytic on $S$ and continuous on $\overline S$ for simple $f,g$. Suppose $\|T_{it}\|_{L^{p_0}\to L^{q_0}}\le M_0(t)$ and $\|T_{1+it}\|_{L^{p_1}\to L^{q_1}}\le M_1(t)$ with $\sup_t M_i(t)<\infty$. Then $T_\theta$ maps $L^p$ to $L^q$ for the indices above with norm at most $\sup_tM_0(t)^{1-\theta}\sup_tM_1(t)^{\theta}$.

Stein's theorem is what permits the endpoint norms to vary with the imaginary part, and it is the version used to interpolate the analytic families of operators that arise in harmonic analysis and in the theory of singular integrals; the applications are treated elsewhere, where the Calderón–Zygmund decomposition provides the endpoint hypotheses.

## The Real Method

### The $K$- and $J$-Functionals

The complex method depends on analytic continuation, and it produces no second parameter. The real method is a construction from the two norms alone.

**Definition.** For a compatible couple $(A_0,A_1)$ and $a \in A_0+A_1$ and $t>0$, the **Peetre $K$-functional** is

$$
K(t,a)=\inf_{a=a_0+a_1}\bigl(\|a_0\|_{A_0}+t\|a_1\|_{A_1}\bigr),
$$

and the **$J$-functional** is, for $a \in A_0\cap A_1$,

$$
J(t,a)=\max\bigl(\|a\|_{A_0},\,t\|a\|_{A_1}\bigr).
$$

The $K$-functional measures the cost of splitting $a$ into a part carrying the $A_0$ norm and a part carrying the $A_1$ norm with weight $t$; it is concave and nondecreasing in $t$ and subadditive in $a$, and it satisfies $K(t,a)\le\min(1,t)\|a\|_{A_0\cap A_1}$ and $K(t,a)\ge\min(1,t)\|a\|_{A_0+A_1}$, so that it is a norm on $A_0+A_1$ equivalent to the sum norm.

**Proposition.** For fixed $a$, $t \mapsto K(t,a)$ is nondecreasing and concave on $(0,\infty)$, and $t \mapsto K(t,a)/t$ is nonincreasing; moreover $K(t,a)\le t\,\|a\|_{A_1}$ if $a \in A_1$ and $K(t,a)\le\|a\|_{A_0}$ if $a \in A_0$.

*Proof.* Concavity is the infimum of the affine functions $a=a_0+a_1 \mapsto \|a_0\|_{A_0}+t\|a_1\|_{A_1}$; monotonicity and the two one-sided bounds are immediate from the definition. $\square$

### The Real Interpolation Space

**Definition.** For $0<\theta<1$ and $1 \le q \le \infty$ the **real interpolation space** $(A_0,A_1)_{\theta,q}$ is the set of $a \in A_0+A_1$ for which

$$
\|a\|_{\theta,q}=\Bigl(\int_0^\infty\bigl(t^{-\theta}K(t,a)\bigr)^q\frac{dt}{t}\Bigr)^{1/q}<\infty
\quad (q<\infty),
\qquad
\|a\|_{\theta,\infty}=\sup_{t>0}\,t^{-\theta}K(t,a)<\infty .
$$

**Theorem.** $(A_0,A_1)_{\theta,q}$ is a Banach space intermediate between $A_0\cap A_1$ and $A_0+A_1$, and the assignment $(A_0,A_1)\mapsto(A_0,A_1)_{\theta,q}$ is an exact interpolation functor of exponent $\theta$.

*Proof (sketch).* The $K$-functional is a norm on the sum for each fixed $t$ up to the constant $\min(1,t)$, so the integral defines a norm; completeness follows by identifying the space with the set of measurable $a$ for which the weighted integral of $K$ is finite, applying Fatou to a Cauchy sequence and using the completeness of $A_0+A_1$. Interpolation: if $T$ is bounded from $A_i$ to $B_i$ with norm $M_i$, then $K_B(t,Ta)\le M_0K_A(M_1t/M_0,a)$, and the change of variable $s=M_1t/M_0$ in the defining integral gives the estimate with the exponent $\theta$. $\square$

**Theorem ($J$-description).** For $a \in A_0\cap A_1$, the norm $\|a\|_{\theta,q}$ is equivalent to

$$
\inf\Bigl\{\Bigl(\int_0^\infty\bigl(t^{-\theta}J(t,u(t))\bigr)^q\frac{dt}{t}\Bigr)^{1/q}: a=\int_0^\infty u(t)\,\frac{dt}{t},\ u(t)\in A_0\cap A_1\Bigr\}.
$$

The two descriptions are the **equivalence theorem** of the real method: every element of the interpolated space admits the representation of the second description, so the construction may be carried out with either functional. The proof is the standard comparison $J(t,a)\ge K(t,a)$ together with a discretisation of the integral.

**Example (Lorentz spaces).** Let $\mu$ be a $\sigma$-finite measure. Then

$$
(L^1(\mu),L^\infty(\mu))_{\theta,q}=L^{p,q}(\mu), \qquad \frac1p=1-\theta,
$$

the **Lorentz space** of measurable functions whose decreasing rearrangement $f^*$ satisfies $\bigl(\int_0^\infty (t^{1/p}f^*(t))^q\,dt/t\bigr)^{1/q}<\infty$. For $q=p$ this is $L^p$, for $q=\infty$ it is the weak $L^p$ space $L^{p,\infty}$; on the sequence side $(\ell^1,\ell^\infty)_{\theta,q}=\ell^{p,q}$. The spaces $\ell^{p,q}$ with $p$ fixed and $q$ varying are distinct as sets, which is exactly the refinement that the complex method misses.

### Duality and Reiteration

**Theorem (duality).** Let $(A_0,A_1)$ be a compatible couple with $A_0\cap A_1$ dense in both $A_0$ and $A_1$. Then for $1\le q<\infty$ and $0<\theta<1$,

$$
\bigl((A_0,A_1)_{\theta,q}\bigr)^*=(A_0^*,A_1^*)_{\theta,q'}, \qquad \frac1q+\frac1{q'}=1,
$$

the dual couple being the compatible couple obtained by embedding $A_0^*$ and $A_1^*$ into $(A_0\cap A_1)^*$.

The density hypothesis is not cosmetic: without it the dual of the intersection, and not the intersection of the duals, enters. For $q=\infty$ the identity fails and is replaced by the inclusion $(A_0^*,A_1^*)_{\theta,1}\subseteq ((A_0,A_1)_{\theta,\infty})^*$.

**Theorem (reiteration).** Let $0<\theta_0<\theta_1<1$, $1\le q_0,q_1,q\le\infty$ and $0<\eta<1$, and put $\theta=(1-\eta)\theta_0+\eta\theta_1$. Then

$$
\bigl((A_0,A_1)_{\theta_0,q_0},(A_0,A_1)_{\theta_1,q_1}\bigr)_{\eta,q}=(A_0,A_1)_{\theta,q},
$$

with equivalence of norms; the two spaces on the left form a compatible couple because both are intermediate for $(A_0,A_1)$. In particular the real method, applied twice, returns the real method at the convex combination of the exponents, so the family $(A_0,A_1)_{\theta,q}$ is closed under its own interpolation.

**Theorem (comparison of the two methods).** For $0<\theta<1$,

$$
(A_0,A_1)_{\theta,1} \subseteq [A_0,A_1]_\theta \subseteq (A_0,A_1)_{\theta,\infty},
$$

with continuous inclusions. Consequently the complex space coincides with a real space only in special cases; for the couple $(L^1,L^\infty)$ one has $[L^1,L^\infty]_\theta=L^{1/(1-\theta)}=(L^1,L^\infty)_{\theta,p}$ with $p=1/(1-\theta)$, so that here the complex space is the real space at the diagonal value $q=p$, but this coincidence is a theorem about the couple and not a general identity.

## Interpolation of the Classical Spaces

The two methods apply to the families of spaces that occur in analysis, and the resulting dictionary is the working content of the theory.

### The $L^p$ and Lorentz Families

**Theorem.** Let $1\le p_0<p_1\le\infty$ and $0<\theta<1$. With $1/p=(1-\theta)/p_0+\theta/p_1$,

$$
[L^{p_0}(\mu),L^{p_1}(\mu)]_\theta=L^p(\mu), \qquad (L^{p_0}(\mu),L^{p_1}(\mu))_{\theta,q}=L^{p,q}(\mu),
$$

where $L^{p,q}$ is the Lorentz space. For $q=p$ the two constructions agree, $L^{p,p}=L^p$.

The case $p_1=\infty$ is the definition of the Lorentz spaces; the case $p_1<\infty$ follows from it by the reiteration theorem, since $(L^{p_0},L^{p_1})_{\theta,q}$ lies between the corresponding Lorentz spaces. This is the mechanism by which the theory of a single family of spaces is generated from the two extreme members.

### The Sobolev and Besov Families

**Definition.** For $s \in \mathbb{R}$ and $1<p<\infty$ the **Bessel-potential space** $H^s_p(\mathbb{R}^n)$ is the set of tempered distributions $u$ whose Fourier transform satisfies

$$
\|u\|_{H^s_p}=\bigl\|\mathcal F^{-1}\bigl((1+|\xi|^2)^{s/2}\hat u\bigr)\bigr\|_{L^p}<\infty .
$$

For $s=k \in \mathbb{N}$ and $1<p<\infty$ the space $H^k_p$ coincides with the Sobolev space $W^{k,p}$ of functions whose weak derivatives of order at most $k$ lie in $L^p$, with equivalent norms; this identification is the content, and only the Fourier description is used here.

**Theorem.** For $s_0,s_1 \in \mathbb{R}$, $1<p_0,p_1<\infty$ and $0<\theta<1$,

$$
[H^{s_0}_{p_0},H^{s_1}_{p_1}]_\theta=H^{s}_p, \qquad s=(1-\theta)s_0+\theta s_1, \quad \frac1p=\frac{1-\theta}{p_0}+\frac{\theta}{p_1},
$$

and for the real method

$$
(H^{s_0}_p,H^{s_1}_p)_{\theta,q}=B^{s}_{p,q}, \qquad s=(1-\theta)s_0+\theta s_1,
$$

where $B^s_{p,q}$ is the **Besov space**. The first identity is the interpolation of the Fourier multiplier $(1+|\xi|^2)^{s/2}$; the second is the reason the Besov scale has a second parameter, and the Besov and Triebel–Lizorkin spaces are the subject of of this category, where the difference-quotient and Littlewood–Paley descriptions of $B^s_{p,q}$ are given and the two-parameter family is developed. Here the Besov space is used only as the output of the real method.

**Corollary (Sobolev embedding, interpolated).** If $0 \le s_1<s_0$ and $1<p<\infty$, then $H^{s_0}_p\subseteq H^{s_1}_p$, and for $s=(1-\theta)s_1+\theta s_0$ the interpolation identity above exhibits $H^s_p$ as an intermediate space. The classical Sobolev embedding $H^{s}_p\subseteq L^r$ with $1/r=1/p-s/n$, when $s<n/p$, is obtained from the endpoint embeddings at $s=0$ and at a large $s$ by interpolation, and the embedding theorems in the sharp form are standard.

### Interpolation of Analytic and Harmonic Spaces

**Theorem (Marcinkiewicz).** Let $T$ be a sublinear map defined on the simple functions of a $\sigma$-finite measure space and taking measurable functions, and suppose $T$ is of weak type $(p_0,p_0)$ with constant $M_0$ and of weak type $(p_1,p_1)$ with constant $M_1$, where $1\le p_0<p_1\le\infty$. Then $T$ is of strong type $(p,p)$ for every $p_0<p<p_1$, with a bound depending only on the constants and the indices.

The proof of Marcinkiewicz's theorem is the standard decomposition of $f$ into a part of large values, controlled by the weak-type hypothesis at $p_0$, and a part of small values, controlled at $p_1$, followed by an application of the $K$-functional calculus in the form $(L^{p_0},L^{p_1})_{\theta,p}=L^p$. The theorem is the real-method counterpart of Riesz–Thor, and it is the version that applies to singular integral operators, where the endpoint estimate is weak; the operators themselves are treated, and the interpolation step is the one recorded here.

## Summary

An interpolation theory begins with a compatible couple $(A_0,A_1)$ of Banach spaces inside a common ambient space and constructs the intermediate spaces. The intersection $A_0\cap A_1$ with the maximum norm and the sum $A_0+A_1$ with the infimum norm are Banach spaces, and every intermediate space lies between them. An interpolation functor assigns to the couple a space and to the maps between couples a map, and it is of exponent $\theta$ when the operator norm obeys $\|T\| \le \|T\|_{A_0\to B_0}^{1-\theta}\|T\|_{A_1\to B_1}^{\theta}$; both methods below are exact functors of exponent $\theta$.

The complex method takes the values at the interior point $\theta$ of the bounded analytic functions on the strip whose boundary values lie in $A_0$ and $A_1$; the three-lines lemma and the maximum modulus principle for Banach-space-valued analytic functions make the construction a Banach space and a functor. Its principal theorem is Riesz–Thorin: a linear map bounded between two pairs of $L^p$ spaces is bounded between the interpolated pair, with norm at most $M_0^{1-\theta}M_1^{\theta}$, where the exponents interpolate reciprocally. The method gives $[L^{p_0},L^{p_1}]_\theta=L^p$, the Hausdorff–Young theorem for the Fourier transform, and, in Stein's form, the interpolation of analytic families of operators.

The real method uses the Peetre functional $K(t,a)=\inf_{a=a_0+a_1}(\|a_0\|_{A_0}+t\|a_1\|_{A_1})$, integrated against the weight $t^{-\theta q}\,dt/t$, and produces a space $(A_0,A_1)_{\theta,q}$ with a second parameter $q$; the $J$-functional gives an equivalent description, and the two descriptions coincide. The method yields the Lorentz spaces $(L^1,L^\infty)_{\theta,q}=L^{p,q}$ with $1/p=1-\theta$, is self-reiterating, and dualises to the pair of dual couples for $1\le q<\infty$. The complex space lies between the real spaces at $q=1$ and $q=\infty$, and the two methods agree on $(L^1,L^\infty)$ at the diagonal $q=p$.

On the classical families the dictionary reads $[L^{p_0},L^{p_1}]_\theta=L^p$, $(L^{p_0},L^{p_1})_{\theta,q}=L^{p,q}$, $[H^{s_0}_{p_0},H^{s_1}_{p_1}]_\theta=H^s_p$ and $(H^{s_0}_p,H^{s_1}_p)_{\theta,q}=B^s_{p,q}$, with the exponent interpolated linearly and the Lebesgue index reciprocally; Marcinkiewicz's theorem complements Riesz–Thorin by interpolating weak endpoint estimates into strong ones, and the Besov scale, the Sobolev embeddings and the singular integral operators are the places where the theory is applied.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ |
| $(A_0,A_1)$ | compatible couple of Banach spaces |
| $\mathcal{X}$ | ambient Hausdorff topological vector space |
| $A_0\cap A_1$, $A_0+A_1$ | intersection and sum with maximum and infimum norms |
| $\theta$, $1-\theta$ | interpolation exponent |
| $F(A_0,A_1)$ | interpolated space of a functor $F$ |
| $\mathcal A(A_0,A_1)$, $\|f\|_{\mathcal A}$ | bounded analytic functions on the strip, and the strip norm |
| $[A_0,A_1]_\theta$ | complex interpolation space |
| $K(t,a)$, $J(t,a)$ | Peetre $K$- and $J$-functionals |
| $(A_0,A_1)_{\theta,q}$ | real interpolation space |
| $L^{p,q}$ | Lorentz space |
| $\ell^{p,q}$ | Lorentz sequence space |
| $H^s_p$ | Bessel-potential (Sobolev) space |
| $W^{k,p}$, $B^s_{p,q}$ | Sobolev and Besov spaces |
| $M_0$, $M_1$ | endpoint operator norms |
| $\mathcal F$ | Fourier transform on $\mathbb{R}^n$ |
| $M_0(t)$, $M_1(t)$ | endpoint norms of an analytic family |
| $q'$ | conjugate exponent $1/q+1/q'=1$ |



## Further Reading

- Colin Bennett and Robert Sharpley, *Interpolation of Operators* (Academic Press, 1988), for the real and complex methods and the Lorentz spaces in detail.
- Jöran Bergh and Jörgen Löfström, *Interpolation Spaces: An Introduction* (Springer, 1976), for the $K$- and $J$-methods, duality and reiteration.
- Alberto P. Calderón, "Intermediate spaces and interpolation, the complex method", *Studia Mathematica* 24 (1964), 113–190, for the complex method as a functor.
- Elias M. Stein, "Interpolation of linear operators", *Transactions of the American Mathematical Society* 83 (1956), 482–492, for the analytic-family version.
- Marcel Riesz, "Sur les maxima des formes bilinéaires et sur les fonctionnelles linéaires", *Acta Mathematica* 49 (1927), 465–497, for the convexity theorem that Riesz–Thorin generalises.
- G. Olof Thorin, "Convexity theorems generalizing those of M. Riesz and Hadamard with some applications", *Meddelanden Lunds Universitets Matematiska Seminarium* 9 (1948), 1–58, for the theorem bearing his name.
- Hans Triebel, *Interpolation Theory, Function Spaces, Differential Operators* (North-Holland, 1978), for the interpolation of Sobolev, Besov and Triebel–Lizorkin spaces.
- Antoni Zygmund, *Trigonometric Series*, 3rd ed. (Cambridge University Press, 2002), for the Marcinkiewicz interpolation theorem and its applications.
