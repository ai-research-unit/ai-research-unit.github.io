
# __Banach and Hilbert Spaces__

## Introduction

A norm on a vector space turns it into a metric space, and completeness of that metric space makes it possible to take limits of series; a norm that comes from an inner product carries in addition the geometry of angles and orthogonality, and completeness then yields the projection theorem, orthonormal bases and the spectral theorem. This article develops the inner-product theory and the Hilbert-space theory it generates, with the normed-space theory and its Baire-based cornerstones taken as background from the companion article of this category on normed and Banach spaces, and the general topological theory from the article on topological modules and vector spaces.

Throughout, $\mathbb{K}$ denotes $\mathbb{R}$ or $\mathbb{C}$ and all vector spaces are over $\mathbb{K}$; the conjugate-linear slot of a sesquilinear form is the second one. The article is organised so that the purely metric facts — completeness, bounded operators, the operator norm — are stated once and used, while the genuinely inner-product-theoretic material occupies the centre: the Cauchy–Schwarz inequality, the parallelogram law and the Jordan–von Neumann theorem, the projection theorem, orthonormal bases, the Riesz representation theorem, the adjoint, the spectral theorem for bounded self-adjoint and normal operators, and the spectral theory of compact operators with the Fredholm alternative.

The two standard examples are the sequence space $\ell^2$ and the function space $L^2(\mu)$, and the finite-dimensional case closes the article: there every operator is a matrix, the projection theorem is the orthogonal decomposition of linear algebra, and the spectral theorem reduces to the orthogonal diagonalisation of normal matrices established in the article of this category on eigenvalues and diagonalisation.

## The Setting: Normed and Banach Spaces

**Definition.** A **norm** on a $\mathbb{K}$-vector space $X$ is a function $\|\cdot\|:X \to \mathbb{R}_{\ge0}$ with $\|x\|=0$ iff $x=0$, $\|\lambda x\|=|\lambda|\|x\|$ and $\|x+y\| \le \|x\|+\|y\|$. The pair $(X,\|\cdot\|)$ is a **normed space**, and $d(x,y)=\|x-y\|$ is its metric. A normed space that is complete for this metric is a **Banach space**.

**Definition.** A linear map $T:X \to Y$ between normed spaces is **bounded** if there is $C$ with $\|Tx\| \le C\|x\|$ for all $x$. The least such $C$ is the **operator norm**

$$
\|T\|=\sup_{x \neq 0}\frac{\|Tx\|}{\|x\|}=\sup_{\|x\| \le 1}\|Tx\| .
$$

**Theorem.** For linear $T$ the following are equivalent: $T$ is continuous; $T$ is continuous at $0$; $T$ is bounded; $T$ is uniformly continuous. The set $B(X,Y)$ of bounded linear maps is a normed space under the operator norm, complete when $Y$ is complete, and the operator norm is submultiplicative, $\|ST\| \le \|S\|\,\|T\|$, for composable bounded maps.

These are the basic facts of the normed theory; they are proved in the companion article *Normed and Banach Spaces*, which also proves the cornerstones resting on completeness and Baire category: the Hahn–Banach extension theorem, the open mapping theorem, the closed graph theorem and the uniform boundedness principle. This article uses them where the Hilbert-space theory needs them, namely in the construction of orthonormal bases and in the Riesz theorem, and does not re-prove them.

**Example.** For $1 \le p < \infty$, the space $\ell^p$ of sequences $x=(x_1,x_2,\dots)$ with $\sum_i|x_i|^p<\infty$ is a Banach space under $\|x\|_p=(\sum_i|x_i|^p)^{1/p}$. The space $\ell^\infty$ of bounded sequences is a Banach space under $\|x\|_\infty=\sup_i|x_i|$. The space $C(K)$ of continuous functions on a compact Hausdorff space $K$ is a Banach space under the supremum norm. The space $L^p(\mu)$ of $p$-integrable functions modulo null functions is a Banach space under $\|f\|_p=(\int|f|^p\,d\mu)^{1/p}$.

## Inner Product Spaces

### Definition and the Induced Norm

**Definition.** An **inner product** on a $\mathbb{K}$-vector space $H$ is a map $\langle\cdot,\cdot\rangle:H \times H \to \mathbb{K}$ that is linear in the first argument, conjugate-linear in the second, satisfies $\langle x,y\rangle=\overline{\langle y,x\rangle}$, and is positive definite, $\langle x,x\rangle>0$ for $x \neq 0$. An **inner product space** is a pair $(H,\langle\cdot,\cdot\rangle)$. The induced norm is

$$
\|x\|=\sqrt{\langle x,x\rangle} .
$$

Together with the norm comes the **polar form** of the inner product, and over $\mathbb{C}$ the inner product is recovered from the norm by the **polarisation identity**

$$
\langle x,y\rangle=\tfrac14\sum_{k=0}^{3}i^k\|x+i^ky\|^2 .
$$

**Theorem (Cauchy–Schwarz).** For all $x,y$ in an inner product space,

$$
|\langle x,y\rangle| \le \|x\|\,\|y\| ,
$$

with equality if and only if $x,y$ are linearly dependent.

*Proof.* If $y=0$ both sides vanish. Otherwise write $x=\alpha y+z$ with $\alpha=\langle x,y\rangle/\|y\|^2$, so that $\langle z,y\rangle=0$. Then

$$
\|x\|^2=|\alpha|^2\|y\|^2+\|z\|^2 \ge |\alpha|^2\|y\|^2=\frac{|\langle x,y\rangle|^2}{\|y\|^2},
$$

which is the inequality; equality forces $z=0$, so $x=\alpha y$. $\square$

**Corollary.** The induced norm satisfies the triangle inequality, so $\|\cdot\|$ is a norm, and the inner product is continuous in each argument with respect to it.

*Proof.* $\|x+y\|^2=\|x\|^2+2\operatorname{Re}\langle x,y\rangle+\|y\|^2 \le \|x\|^2+2\|x\|\|y\|+\|y\|^2=(\|x\|+\|y\|)^2$. $\square$

### The Parallelogram Law

**Proposition (parallelogram law).** In any inner product space,

$$
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2 .
$$

*Proof.* Expand both squares and add: the cross terms cancel. $\square$

**Theorem (Jordan–von Neumann).** A norm $\|\cdot\|$ on a $\mathbb{K}$-vector space arises from an inner product if and only if it satisfies the parallelogram law; the inner product is then given by the polarisation identity.

*Proof.* Necessity is the proposition. For sufficiency, define $\langle x,y\rangle$ by the polarisation identity and verify additivity and homogeneity; the parallelogram law is exactly the identity needed to prove $\langle x,y+z\rangle=\langle x,y\rangle+\langle x,z\rangle$, and the remaining properties follow from the norm axioms. $\square$

The parallelogram law therefore characterises the inner-product norms among all norms, and this is the source of many non-Hilbert Banach spaces: $\ell^p$ for $p \neq 2$ and $C(K)$ for $K$ with more than one point fail the law, so they carry no inner product inducing their norms.

## Hilbert Spaces

### Definition and Examples

**Definition.** A **Hilbert space** is an inner product space that is complete for the induced norm.

**Example.** The space $\ell^2$ of square-summable sequences with $\langle x,y\rangle=\sum_i x_i\overline{y_i}$ is a Hilbert space. For a measure space $(X,\mu)$, the space $L^2(\mu)$ with $\langle f,g\rangle=\int f\bar g\,d\mu$ is a Hilbert space, after identifying functions equal almost everywhere. Every finite-dimensional inner product space is complete, hence a Hilbert space.

**Proposition.** A closed subspace $M$ of a Hilbert space is itself a Hilbert space with the restricted inner product. Conversely a subspace of a Hilbert space is complete exactly when it is closed: a complete subspace of a metric space is closed, and a closed subspace of a complete space is complete. An inner product space that is not complete therefore sits inside its completion as a non-closed dense subspace.

### The Projection Theorem

**Definition.** A subset $C$ of a normed space is **convex** if $(1-t)x+ty \in C$ for $x,y \in C$ and $0 \le t \le 1$.

**Theorem (projection).** Let $C$ be a nonempty closed convex subset of a Hilbert space $H$. For every $x \in H$ there is a unique $p \in C$ with $\|x-p\|=d(x,C)=\inf_{c \in C}\|x-c\|$. If $C=M$ is a closed subspace, then $x-p \perp M$ and every $x$ has a unique decomposition

$$
x=p+q, \qquad p \in M,\ q \in M^{\perp} ,
$$

so $H=M \oplus M^{\perp}$, where $M^{\perp}=\{y : \langle y,m\rangle=0 \text{ for all } m \in M\}$.

*Proof.* Choose a minimising sequence $c_n$; the parallelogram law applied to $x-c_m$ and $x-c_n$ gives

$$
\|c_m-c_n\|^2=2\|x-c_m\|^2+2\|x-c_n\|^2-4\|x-\tfrac12(c_m+c_n)\|^2 \le 2\|x-c_m\|^2+2\|x-c_n\|^2-4d^2,
$$

and the right-hand side tends to $0$, so $c_n$ is Cauchy; completeness gives a limit $p \in C$, which is a nearest point, and uniqueness follows from the same inequality. For a subspace $M$, if $p$ is the nearest point of $M$ to $x$ and $m \in M$, then minimising $t \mapsto \|x-p-tm\|^2$ over $t$ gives $\operatorname{Re}\langle x-p,m\rangle=0$ and, replacing $m$ by $im$ over $\mathbb{C}$, $\langle x-p,m\rangle=0$. So $q=x-p \perp M$, and $H=M+M^{\perp}$ with $M \cap M^{\perp}=0$. $\square$

**Corollary.** $(M^{\perp})^{\perp}=\overline{M}$ for any subspace $M$, and $M$ is dense in $H$ if and only if $M^{\perp}=0$.

### Orthonormal Sets and Bases

**Definition.** A subset $\{e_\alpha\}$ of $H$ is **orthonormal** if $\langle e_\alpha,e_\beta\rangle=\delta_{\alpha\beta}$. An orthonormal set is an **orthonormal basis** if it is maximal, equivalently if no nonzero vector is orthogonal to all of it.

**Theorem (Bessel).** For every orthonormal set $\{e_\alpha\}$ and every $x \in H$,

$$
\sum_\alpha |\langle x,e_\alpha\rangle|^2 \le \|x\|^2 ,
$$

and only countably many terms are nonzero.

*Proof.* Every finite subfamily gives $\|x-\sum\langle x,e_\alpha\rangle e_\alpha\|^2=\|x\|^2-\sum|\langle x,e_\alpha\rangle|^2 \ge 0$, using orthonormality; the general case follows by taking suprema. For the countability, if the set $\{\alpha:|\langle x,e_\alpha\rangle|>1/n\}$ were infinite for some $n$, a finite subfamily of it would already make the sum of squares exceed $\|x\|^2$; each such set is therefore finite, and their union over $n \ge 1$ is the countable set of indices with $\langle x,e_\alpha\rangle \neq 0$. $\square$

**Theorem (Parseval and bases).** For an orthonormal set $\{e_\alpha\}$ the following are equivalent: (i) it is complete; (ii) $x=\sum_\alpha\langle x,e_\alpha\rangle e_\alpha$ for every $x$; (iii) $\|x\|^2=\sum_\alpha|\langle x,e_\alpha\rangle|^2$ for every $x$. Every Hilbert space has an orthonormal basis, and it is separable if and only if it has a countable one, in which case the basis is a Schauder basis and every orthonormal basis is countably infinite or finite.

*Proof.* The equivalence is the finite-subfamily identity in the limit, since (ii) and (iii) are its two sides in the sense of convergence. Existence: Zorn's lemma applied to the orthonormal sets ordered by inclusion gives a maximal one; a maximal orthonormal set is complete, because a vector orthogonal to all of it can be normalised and added. Separability follows from the density of the rational finite linear combinations of a countable basis. $\square$

### The Classification of Separable Hilbert Spaces

Orthonormal bases make the Hilbert-space axioms concrete: the coordinates in a basis describe the space completely.

**Theorem (Riesz–Fischer).** For a set $A$ let $\ell^2(A)=\{(x_\alpha)_{\alpha \in A}:\sum_\alpha|x_\alpha|^2<\infty\}$, with $\langle x,y\rangle=\sum_\alpha x_\alpha\overline{y_\alpha}$. Then $\ell^2(A)$ is a Hilbert space.

*Proof.* The sum defining the inner product converges absolutely by Cauchy–Schwarz applied to finite partial sums, so the form is defined and the norm axioms hold. For completeness, let $(x^{(n)})$ be Cauchy. Each coordinate converges, since $|x^{(n)}_\alpha-x^{(m)}_\alpha| \le \|x^{(n)}-x^{(m)}\|$, giving $x=(x_\alpha)$; for a finite set $F \subseteq A$ one has $\sum_{\alpha \in F}|x_\alpha|^2=\lim_n\sum_{\alpha \in F}|x^{(n)}_\alpha|^2 \le \sup_n\|x^{(n)}\|^2<\infty$, so $x \in \ell^2(A)$, and letting $F$ grow and $n,m$ tend to infinity in $\sum_{\alpha \in F}|x^{(n)}_\alpha-x^{(m)}_\alpha|^2 \le \varepsilon^2$ gives $\|x-x^{(n)}\| \to 0$. $\square$

**Theorem.** For an orthonormal set $\{e_\alpha\}_{\alpha \in A}$ in a Hilbert space $H$ the map

$$
\Lambda:\ell^2(A) \longrightarrow H, \qquad \Lambda(x)=\sum_\alpha x_\alpha e_\alpha ,
$$

is a linear isometry onto the closed span of $\{e_\alpha\}$; it is onto $H$ exactly when the set is an orthonormal basis.

*Proof.* The finite partial sums of $\sum_\alpha x_\alpha e_\alpha$ satisfy $\|\sum_{\alpha \in F}x_\alpha e_\alpha\|^2=\sum_{\alpha \in F}|x_\alpha|^2$ by orthonormality, so they are Cauchy and $\Lambda$ is defined, linear and isometric by the completeness of $\ell^2(A)$; being isometric it is injective, and its image is closed and contains every $e_\alpha$, hence contains the closed span. If the set is complete then the closed span is $H$; conversely if $\Lambda$ is onto and $x \perp e_\alpha$ for every $\alpha$, then $x=\Lambda(y)$ with $\langle y,\delta_\beta\rangle=\langle x,e_\beta\rangle=0$ for every $\beta$, so $y=0$ and $x=0$. $\square$

**Theorem (classification).** Two Hilbert spaces are isometrically isomorphic if and only if they have orthonormal bases of the same cardinality. In particular every separable infinite-dimensional Hilbert space is isometrically isomorphic to $\ell^2$, and every $n$-dimensional one to $\mathbb{K}^n$.

*Proof.* An isometry carries an orthonormal basis to an orthonormal basis and preserves cardinality. Conversely, if $\{e_\alpha\}_{\alpha \in A}$ and $\{f_\alpha\}_{\alpha \in A}$ are orthonormal bases indexed by the same set, the maps $\Lambda$ and $\Lambda'$ of the previous theorem are isometries onto the two spaces, and $\Lambda' \circ \Lambda^{-1}$ is an isometric isomorphism. A separable space has a countable orthonormal basis, which is finite, giving $\mathbb{K}^n$, or countably infinite, giving $\ell^2=\ell^2(\mathbb{N})$. $\square$

The cardinality of an orthonormal basis is therefore a complete invariant of a Hilbert space, called its **Hilbert dimension**; for a separable space it is finite or $\aleph_0$ and no other invariant is needed, so every Hilbert space is $\ell^2(A)$ for a suitable $A$ up to isometric isomorphism.

## Bounded Operators and the Adjoint

**Definition.** For bounded $T:H \to H$ the **adjoint** $T^*$ is the unique bounded operator with

$$
\langle Tx,y\rangle=\langle x,T^*y\rangle \qquad \text{for all } x,y \in H .
$$

**Proposition.** The adjoint exists, is bounded with $\|T^*\|=\|T\|$, and $(T+S)^*=T^*+S^*$, $(\lambda T)^*=\bar\lambda T^*$, $(TS)^*=S^*T^*$, $T^{**}=T$.

*Proof.* For fixed $y$ the map $x \mapsto \langle Tx,y\rangle$ is a bounded linear functional, so by the Riesz representation theorem below there is a unique $T^*y$ with $\langle Tx,y\rangle=\langle x,T^*y\rangle$; the map $y \mapsto T^*y$ is linear and $\|T^*y\|=\sup_{\|x\|\le1}|\langle Tx,y\rangle| \le \|T\|\|y\|$, so $\|T^*\|\le\|T\|$, and applying this to $T^*$ with $T^{**}=T$ gives equality. The algebraic identities are direct from the defining relation. $\square$

**Definition.** $T$ is **self-adjoint** if $T^*=T$, **normal** if $TT^*=T^*T$, **unitary** if $T^*T=TT^*=I$, and a **projection** if $T^2=T=T^*$. The **resolvent set** of $T$ is the set of $\lambda$ with $T-\lambda I$ invertible with bounded inverse, the **spectrum** $\sigma(T)$ its complement, and the **spectral radius** is $\rho(T)=\sup_{\lambda \in \sigma(T)}|\lambda|=\lim\|T^n\|^{1/n}$.

**Proposition.** Self-adjoint operators have real spectrum: if $T=T^*$ and $\lambda \in \sigma(T)$ then $\lambda \in \mathbb{R}$. Moreover $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$ for self-adjoint $T$, and a self-adjoint $T$ is **positive**, meaning $\langle Tx,x\rangle \ge 0$ for all $x$, exactly when $\sigma(T)\subseteq[0,\infty)$.

**Remark.** Over $\mathbb{C}$ the inequality $\langle Tx,x\rangle \ge 0$ for all $x$ already forces $T=T^*$, by polarisation, so positivity needs no separate self-adjointness hypothesis there. Over $\mathbb{R}$ it does: the operator with matrix $\begin{pmatrix}1&-1\\1&1\end{pmatrix}$ satisfies $\langle Tx,x\rangle=x_1^2+x_2^2 \ge 0$ and is not self-adjoint.

*Proof.* If $Tx=\lambda x$ with $x \neq 0$ then $\lambda\|x\|^2=\langle Tx,x\rangle=\overline{\langle x,Tx\rangle}=\bar\lambda\|x\|^2$, so $\lambda=\bar\lambda$, and the statement is immediate for eigenvalues. For an arbitrary $\lambda \in \mathbb{C}$ and $x \neq 0$, the scalar $\langle Tx,x\rangle$ is real, so $\operatorname{Im}\langle(T-\lambda)x,x\rangle=-(\operatorname{Im}\lambda)\|x\|^2$, and Cauchy–Schwarz gives

$$
|\operatorname{Im}\lambda|\,\|x\|^2 \le |\langle(T-\lambda)x,x\rangle| \le \|(T-\lambda)x\|\,\|x\| , \qquad \text{so} \qquad |\operatorname{Im}\lambda|\,\|x\| \le \|(T-\lambda)x\| .
$$

If $\operatorname{Im}\lambda \neq 0$ then $T-\lambda I$ is injective with closed range, and its adjoint $T-\bar\lambda I$ satisfies the same estimate with $\operatorname{Im}\bar\lambda=-\operatorname{Im}\lambda \neq 0$, so $\ker(T-\bar\lambda I)=0$ and the range of $T-\lambda I$, being the orthogonal complement of that kernel, is dense as well; hence $T-\lambda I$ is invertible with bounded inverse and $\lambda \notin \sigma(T)$. Therefore $\sigma(T) \subseteq \mathbb{R}$. The norm formula and the positivity criterion for self-adjoint operators are standard consequences of the spectral theorem below. $\square$

## The Riesz Representation Theorem

**Theorem (Riesz).** Let $H$ be a Hilbert space and $\varphi:H \to \mathbb{K}$ a bounded linear functional. Then there is a unique $y \in H$ with

$$
\varphi(x)=\langle x,y\rangle \quad \text{for all } x \in H, \qquad \text{and then} \qquad \|\varphi\|=\|y\| .
$$

*Proof.* If $\varphi=0$ take $y=0$. Otherwise $M=\ker\varphi$ is a closed subspace of codimension $1$, so $M^{\perp}$ is one-dimensional, spanned by a unit vector $e$. Then $\varphi(e) \neq 0$, and $y=\overline{\varphi(e)}\,e$ satisfies $\varphi(x)=\langle x,y\rangle$ for all $x$: both sides vanish on $M$ and agree on $e$. Uniqueness: $\langle x,y-y'\rangle=0$ for all $x$ forces $y=y'$. The norm identity follows from Cauchy–Schwarz with equality. $\square$

**Corollary.** The map $y \mapsto \langle\cdot,y\rangle$ is a conjugate-linear isometric bijection $H \to H^*$, so $H$ is reflexive and $H^*$ is again a Hilbert space with $\langle \varphi,\psi\rangle=\langle y_\varphi,y_\psi\rangle$. In particular a Hilbert space is its own dual up to the conjugate-linear identification, a property false for a general Banach space.

## The Spectral Theorem

**Definition.** A **spectral measure** on $H$ is a map $E$ from the Borel sets of $\sigma(T) \subseteq \mathbb{R}$ to projections with $E(\varnothing)=0$, $E(\sigma(T))=I$, countable additivity in the strong operator topology and $E(S \cap S')=E(S)E(S')$.

**Theorem (spectral theorem, self-adjoint case).** Let $T$ be a bounded self-adjoint operator on a Hilbert space $H$. Then there is a spectral measure $E$ supported on the compact set $\sigma(T) \subseteq \mathbb{R}$ such that

$$
T=\int_{\sigma(T)}\lambda\,dE(\lambda), \qquad \text{so that} \qquad \langle Tx,y\rangle=\int_{\sigma(T)}\lambda\,d\langle E(\lambda)x,y\rangle ,
$$

and for every bounded measurable function $f$ on $\sigma(T)$ the operator $f(T)=\int f\,dE$ is bounded with $\|f(T)\|=\sup_{\lambda \in \sigma(T)}|f(\lambda)|$. The map $f \mapsto f(T)$ is a $\mathbb{K}$-algebra homomorphism from the bounded Borel functions to $B(H)$ sending $1$ to $I$ and the identity function to $T$.

**Theorem (spectral theorem, normal case).** A bounded operator $T$ on a complex Hilbert space is normal if and only if there is a spectral measure $E$ supported on the compact subset $\sigma(T) \subseteq \mathbb{C}$ with $T=\int \lambda\,dE(\lambda)$. Equivalently, $T$ is unitarily equivalent to multiplication by the identity function on a direct sum of spaces $L^2(\sigma(T),\mu_j)$.

*Proof.* Both theorems are quoted as standard. The self-adjoint case follows from the continuous functional calculus, built by approximating continuous functions on $\sigma(T)$ by polynomials in $T$ and completing; the normal case reduces to the self-adjoint case through the real and imaginary parts and the *commuting* operators $T+T^*$ and $(T-T^*)/i$. $\square$

**Corollary (finite-dimensional case).** In finite dimension the spectral measure is atomic, its atoms are the eigenspaces, and the theorem is the statement that a self-adjoint operator has an orthonormal basis of eigenvectors with real eigenvalues, and a normal operator one with complex eigenvalues. This is the orthogonal diagonalisation of the article on eigenvalues and diagonalisation, and the spectral theorem is its infinite-dimensional extension.

## Compact Operators and the Fredholm Alternative

**Definition.** A bounded operator $K:H \to H$ is **compact** if the image of the closed unit ball is relatively compact, equivalently if every bounded sequence has a subsequence whose images converge.

**Theorem (spectral theory of compact self-adjoint operators).** Let $K$ be compact and self-adjoint. Then:

(i) every nonzero $\lambda \in \sigma(K)$ is an eigenvalue of finite multiplicity, and the eigenspaces are finite-dimensional and mutually orthogonal;

(ii) the eigenvalues form a sequence $\lambda_1,\lambda_2,\dots$ of real numbers with $|\lambda_1| \ge |\lambda_2| \ge \cdots$ and $\lambda_n \to 0$ if the sequence is infinite, together with possibly the eigenvalue $0$;

(iii) the eigenvectors form an orthonormal basis of $H$, so that, enumerating an orthonormal eigenbasis $e_1,e_2,\dots$ with $\lambda_n$ the eigenvalue of $e_n$ and the eigenvalue $0$ included,

$$
K=\sum_n \lambda_n \langle \cdot,e_n\rangle e_n ,
$$

the series converging in operator norm; the nonzero eigenvalues have no accumulation point except $0$.

*Proof.* Quoted as standard. The key point is that a nonzero spectral value must be an eigenvalue by the spectral theorem and the compactness, which forbids a continuous part of the spectrum away from $0$. $\square$

**Theorem (Fredholm alternative).** Let $K$ be compact and consider the equation $x-Kx=y$. Then:

(i) $\ker(I-K)$ is finite-dimensional, $\ker(I-K^*)$ is finite-dimensional, and $\dim\ker(I-K)=\dim\ker(I-K^*)$;

(ii) the equation is solvable if and only if $y \perp \ker(I-K^*)$, that is, $y$ is orthogonal to every solution of $x=K^*x$;

(iii) if $\ker(I-K)=0$ then $I-K$ is invertible with bounded inverse.

*Proof.* Quoted as standard; it is the Riesz–Schauder theory, and the self-adjoint case follows from the spectral theorem above by expanding in the orthonormal eigenbasis. $\square$

**Example.** Integral operators with square-integrable kernel on $L^2[0,1]$ are compact, so the Fredholm alternative applies to integral equations $f(x)-\int_0^1k(x,t)f(t)\,dt=g(x)$; in contrast the identity on an infinite-dimensional Hilbert space is bounded and not compact, and its spectrum is the single eigenvalue $1$ of infinite multiplicity, so the finite-multiplicity conclusion of the compact theory fails for it.

## Summary

A normed space is a vector space with a norm, and a Banach space is one that is complete; bounded linear maps form a normed space under the operator norm, which is submultiplicative. The Hahn–Banach, open mapping, closed graph and uniform boundedness theorems belong to the normed theory and are used here as background; the article of this category on normed and Banach spaces carries their proofs, and the article on topological modules and vector spaces carries the general topological setting.

An inner product space carries a norm $\|x\|=\sqrt{\langle x,x\rangle}$ satisfying the Cauchy–Schwarz inequality $|\langle x,y\rangle|\le\|x\|\|y\|$ and the parallelogram law, and by the Jordan–von Neumann theorem a norm arises from an inner product exactly when the parallelogram law holds. A Hilbert space is a complete inner product space; in it every closed convex set has a unique nearest point, and for a closed subspace $M$ this gives the orthogonal decomposition $H=M\oplus M^{\perp}$. Orthonormal sets satisfy Bessel's inequality, complete ones satisfy Parseval's identity and give the expansion $x=\sum\langle x,e_\alpha\rangle e_\alpha$, and every Hilbert space has an orthonormal basis, countable exactly when the space is separable.

The adjoint of a bounded operator is characterised by $\langle Tx,y\rangle=\langle x,T^*y\rangle$ and satisfies $\|T^*\|=\|T\|$; self-adjoint, normal and unitary operators are defined by $T=T^*$, $TT^*=T^*T$ and $T^*T=TT^*=I$. The Riesz representation theorem identifies the dual of a Hilbert space with itself conjugate-linearly and isometrically, so Hilbert spaces are reflexive. The spectral theorem represents every bounded self-adjoint operator as an integral against a spectral measure on its real spectrum, and every bounded normal operator as an integral over a compact subset of $\mathbb{C}$, with a functional calculus for bounded Borel functions; in finite dimension this is the orthogonal diagonalisation of normal matrices. Compact self-adjoint operators have a discrete spectrum of finite-multiplicity eigenvalues tending to $0$ and an orthonormal eigenbasis, and the Fredholm alternative describes the solvability of $x-Kx=y$ in terms of $\ker(I-K^*)$. The spaces $\ell^2$ and $L^2(\mu)$ are the standard examples throughout.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ |
| $\langle x,y\rangle$ | inner product, linear in the first argument |
| $\|x\|$, $\|T\|$ | norm and operator norm |
| $B(X,Y)$, $B(H)$ | bounded linear operators |
| $H$ | Hilbert space |
| $M^{\perp}$ | orthogonal complement |
| $\{e_\alpha\}$, $\delta_{\alpha\beta}$ | orthonormal set and Kronecker delta |
| $T^*$ | adjoint, $\langle Tx,y\rangle=\langle x,T^*y\rangle$ |
| $I$ | identity operator |
| $\sigma(T)$, $\rho(T)$ | spectrum and spectral radius |
| $E(\lambda)$ | spectral measure |
| $f(T)$ | functional calculus |
| $L^2(\mu)$, $\ell^2$ | standard Hilbert spaces |
| $K$ | compact operator |
| $\lambda_n$, $e_n$ | eigenvalues and eigenvectors of a compact self-adjoint operator |
| $C(K)$, $\ell^p$, $L^p$ | Banach spaces that are not Hilbert spaces for $p \neq 2$ |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the spectral theorem and compact operators.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the general theory of bounded operators.
- Israel Gohberg, Seymour Goldberg and Marinus A. Kaashoek, *Classes of Linear Operators* (Birkhäuser, 1990), for the Fredholm alternative and its generalisations.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the geometry of Hilbert space and its counterexamples.
- Paul R. Halmos, *Introduction to Hilbert Space* (Chelsea, 2nd ed. 1957), for orthonormal bases and the projection theorem.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the spectral theorem with applications to $L^2$.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 3rd ed. 1987), for $L^2$ theory and the Riesz representation theorem.
- Kosaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the Banach-space background and the cornerstones.
