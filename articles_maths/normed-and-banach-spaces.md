
# __Normed and Banach Spaces__

## Introduction

A norm measures the size of a vector and makes the space a metric space; when the metric is complete the space is a Banach space, and completeness is what allows the theorems of functional analysis to be proved. This article develops the normed theory: norms and the equivalence of norms in finite dimension, bounded linear maps and the operator norm, completeness and its consequences for series, and the four cornerstones that rest on completeness and on Baire's category theorem — the Hahn–Banach theorem, the uniform boundedness principle, the open mapping theorem and the closed graph theorem. It closes with the dual space and its main examples.

Throughout, $\mathbb{K}$ denotes $\mathbb{R}$ or $\mathbb{C}$ and all spaces are normed spaces over $\mathbb{K}$ unless stated. This is the normed article of the category. The general topological theory — linear topologies, completions of topological modules, seminorms, Fréchet spaces — is the companion article on topological modules and vector spaces, and the inner-product and Hilbert-space theory is the companion article on Banach and Hilbert spaces; a Hilbert space is a Banach space whose norm satisfies the parallelogram law, and it is discussed here only where the normed theory needs it.

## Norms

### Definition and Examples

**Definition.** A **norm** on a $\mathbb{K}$-vector space $X$ is a function $\|\cdot\|:X \to \mathbb{R}_{\ge0}$ with $\|x\|=0$ if and only if $x=0$, $\|\lambda x\|=|\lambda|\|x\|$, and $\|x+y\| \le \|x\|+\|y\|$. The pair $(X,\|\cdot\|)$ is a **normed space**; the metric is $d(x,y)=\|x-y\|$ and the topology is the metric topology, with neighbourhoods of $0$ the open balls $B_\varepsilon=\{x:\|x\|<\varepsilon\}$.

**Example.** (i) $\mathbb{K}^n$ with $\|x\|_p=(\sum_i|x_i|^p)^{1/p}$ for $1 \le p<\infty$, and $\|x\|_\infty=\max_i|x_i|$.

(ii) The sequence space $\ell^p$ of $x$ with $\sum_i|x_i|^p<\infty$, $1 \le p<\infty$, under $\|x\|_p$; the space $c_0$ of sequences tending to $0$ and $\ell^\infty$ of bounded sequences under $\|\cdot\|_\infty$.

(iii) $C(K)$ for a compact Hausdorff space $K$, under $\|f\|_\infty=\sup_{x \in K}|f(x)|$.

(iv) $L^p(\mu)$, $1 \le p<\infty$, under $\|f\|_p=(\int|f|^p\,d\mu)^{1/p}$, after identifying functions equal almost everywhere.

(v) For normed spaces $X,Y$, the space $B(X,Y)$ of bounded linear maps under the operator norm defined below; this is the standard example of a normed space whose elements are themselves maps.

In $\mathbb{K}^n$ the three norms $\|\cdot\|_1,\|\cdot\|_2,\|\cdot\|_\infty$ are distinct as functions but equivalent as norms, defining the same topology; this is a special case of the next theorem.

### Equivalence of Norms

**Definition.** Two norms $\|\cdot\|$ and $\|\cdot\|'$ on $X$ are **equivalent** if there are constants $c_1,c_2>0$ with $c_1\|x\| \le \|x\|' \le c_2\|x\|$ for all $x$; equivalently, if they induce the same topology. Equivalent norms have the same bounded sets, the same Cauchy sequences and the same bounded operators.

**Theorem.** On a finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$, any two norms are equivalent.

*Proof.* It suffices to compare an arbitrary norm $\|\cdot\|$ with the Euclidean norm $\|\cdot\|_2$ on $\mathbb{K}^n$. Upper bound: writing $x=\sum x_ie_i$, one has $\|x\| \le \sum_i|x_i|\|e_i\| \le c_2\|x\|_2$ with $c_2=(\sum_i\|e_i\|^2)^{1/2}$ by Cauchy–Schwarz. Lower bound: the function $x \mapsto \|x\|$ is continuous for $\|\cdot\|_2$ because $|\|x\|-\|y\|| \le \|x-y\| \le c_2\|x-y\|_2$, and the sphere $\{x:\|x\|_2=1\}$ is compact by Heine–Borel; the continuous function attains a positive minimum $c_1>0$ there, and homogeneity extends $c_1\|x\|_2 \le \|x\|$ to all $x$. $\square$

**Corollary.** A linear map between finite-dimensional normed spaces is automatically continuous, and every finite-dimensional normed space is complete.

## Bounded Linear Maps

### Continuity and Boundedness

**Definition.** A linear map $T:X \to Y$ between normed spaces is **bounded** if there is $C \ge 0$ with $\|Tx\| \le C\|x\|$ for all $x$, and the least such constant is the **operator norm**

$$
\|T\|=\sup_{x \neq 0}\frac{\|Tx\|}{\|x\|}=\sup_{\|x\| \le 1}\|Tx\|=\sup_{\|x\|=1}\|Tx\| .
$$

**Theorem.** For linear $T:X \to Y$ the following are equivalent: (i) $T$ is continuous; (ii) $T$ is continuous at $0$; (iii) $T$ is bounded; (iv) $T$ maps bounded sets to bounded sets. In this case $\ker T$ is closed.

*Proof.* (i)$\Rightarrow$(ii) is trivial. (ii)$\Rightarrow$(iii): continuity at $0$ gives $\delta>0$ with $\|x\|\le\delta \Rightarrow \|Tx\|\le1$, hence $\|Tx\| \le \delta^{-1}\|x\|$. (iii)$\Rightarrow$(i): $\|Tx-Tx_0\| \le C\|x-x_0\|$. The equivalence with (iv) is immediate from the definitions, and $\ker T$ is the preimage of the closed set $\{0\}$. $\square$

**Proposition.** $B(X,Y)$ is a normed space under the operator norm and a Banach space when $Y$ is a Banach space; the operator norm is submultiplicative, $\|ST\| \le \|S\|\|T\|$, and composition of bounded maps is continuous. The dual space $X^*=B(X,\mathbb{K})$ is always a Banach space.

*Proof.* The norm axioms are immediate. For completeness, if $(T_n)$ is Cauchy then $(T_nx)$ is Cauchy for each $x$; define $Tx=\lim T_nx$, check linearity, and let $m \to \infty$ in $\|T_nx-T_mx\| \le \varepsilon\|x\|$ to obtain $\|T-T_m\| \le \varepsilon$. Submultiplicativity is $\|STx\| \le \|S\|\|Tx\| \le \|S\|\|T\|\|x\|$. $\square$

### Isomorphisms and Isometries

**Definition.** A linear bijection $T:X \to Y$ is a **topological isomorphism** if $T$ and $T^{-1}$ are bounded, and an **isometry** if $\|Tx\|=\|x\|$ for all $x$; an isometric isomorphism is a **linear isometry**. Two norms are equivalent exactly when the identity is a topological isomorphism.

**Example.** The map $\ell^p \to (\ell^q)^*$, $x \mapsto (y \mapsto \sum_i x_i\overline{y_i})$, is an isometric isomorphism for $1<p<\infty$ with $1/p+1/q=1$; the same formula identifies $\ell^1$ with $(c_0)^*$ and $\ell^\infty$ with $(\ell^1)^*$. The dual of $L^p(\mu)$ is $L^q(\mu)$ for $1<p<\infty$ and $\mu$ $\sigma$-finite, and the dual of $C(K)$ is the space of finite signed or complex measures by the Riesz–Markov theorem.

## Completeness

### Banach Spaces and Series

**Definition.** A normed space that is complete for its metric is a **Banach space**.

**Theorem.** In a normed space $X$, if a series satisfies $\sum_n\|x_n\|<\infty$ then $\sum_nx_n$ converges and $\|\sum_nx_n\| \le \sum_n\|x_n\|$. In a Banach space the converse holds: if every absolutely convergent series converges, then $X$ is complete.

*Proof.* The partial sums are Cauchy because $\|\sum_{n=m}^{N}x_n\| \le \sum_{n=m}^N\|x_n\|$ tends to $0$. Conversely, a Cauchy sequence $(y_k)$ has a subsequence with $\|y_{k_{j+1}}-y_{k_j}\| \le 2^{-j}$; the telescoping series converges absolutely, hence converges to some $y$, and the Cauchy property forces $y_k \to y$. $\square$

**Definition.** A **Schauder basis** of a Banach space $X$ is a sequence $(e_n)$ such that every $x \in X$ has a unique expansion $x=\sum_n a_ne_n$ convergent in norm. Not every separable Banach space has one; in contrast every separable Hilbert space has an orthonormal basis, which is a Schauder basis, by the companion article on Banach and Hilbert spaces.

### Finite Dimension and Compactness

**Lemma (Riesz).** Let $Y$ be a proper closed subspace of a normed space $X$, and let $0<\varepsilon<1$. Then there is $x \in X$ with $\|x\|=1$ and $d(x,Y) \ge 1-\varepsilon$.

*Proof.* Choose $z \notin Y$ with $d(z,Y)=d>0$ and pick $y \in Y$ with $\|z-y\| \le d/(1-\varepsilon)$; set $x=(z-y)/\|z-y\|$. For $y' \in Y$ one has $y+\|z-y\|y' \in Y$ and hence

$$
\|x-y'\|=\frac{1}{\|z-y\|}\bigl\|z-\bigl(y+\|z-y\|y'\bigr)\bigr\| \ge \frac{d}{\|z-y\|} \ge 1-\varepsilon . \qquad \square
$$

**Theorem.** A normed space is finite-dimensional if and only if its closed unit ball is compact. Consequently every locally compact normed space is finite-dimensional.

*Proof.* In finite dimension the ball is compact by Heine–Borel and the equivalence of norms. Conversely, if the ball is compact and $X$ is infinite-dimensional, construct by Riesz's lemma a sequence $(x_n)$ in the unit sphere with $\|x_m-x_n\| \ge 1/2$ for $m \neq n$, which has no convergent subsequence, contradiction. $\square$

## The Baire-Based Cornerstones

### Baire Category

**Theorem (Baire).** A complete metric space is not the union of countably many nowhere dense subsets; equivalently, a countable intersection of dense open subsets of a complete metric space is dense.

*Proof.* Standard: given dense open $G_n$ and a nonempty open $U$, choose a closed ball $\overline B_1 \subseteq G_1 \cap U$ of radius $<1$, then $\overline B_{k+1}\subseteq G_{k+1}\cap B_k$ of radius $<2^{-k}$; the centres form a Cauchy sequence whose limit lies in every $G_n \cap U$. $\square$

### Uniform Boundedness

**Theorem (uniform boundedness principle, Banach–Steinhaus).** Let $X$ be a Banach space, $Y$ a normed space, and $\mathcal{F} \subseteq B(X,Y)$ a family that is pointwise bounded: $\sup_{T \in \mathcal{F}}\|Tx\|<\infty$ for every $x$. Then $\mathcal{F}$ is uniformly bounded, $\sup_{T \in \mathcal{F}}\|T\|<\infty$.

*Proof.* Put $X_n=\{x:\sup_{T \in \mathcal{F}}\|Tx\| \le n\}$; each $X_n$ is closed and the hypothesis is $X=\bigcup_nX_n$. By Baire, some $X_N$ has nonempty interior, so there are $x_0$ and $\delta>0$ with $\|x\| \le \delta \Rightarrow \sup_T\|T(x_0+x)\| \le N$. Then for $\|x\|\le\delta$ and $T \in \mathcal{F}$, $\|Tx\| \le \|T(x_0+x)\|+\|Tx_0\| \le 2N$, so $\|T\| \le 2N/\delta$. $\square$

### Open Mapping and Closed Graph

**Theorem (open mapping).** Let $X,Y$ be Banach spaces and $T:X \to Y$ a surjective bounded linear map. Then $T$ is open: the image of every open set is open. Consequently a bounded linear bijection between Banach spaces has a bounded inverse (the bounded inverse theorem).

*Proof (sketch).* The Baire category theorem applied to $Y=\bigcup_n \overline{T(nB_X)}$ gives some $\overline{T(rB_X)}$ with nonempty interior, and by linearity this implies $T(B_X)$ contains a ball around $0$, hence $T$ is open; the bounded inverse statement follows by applying openness to the open set $T^{-1}(\cdot)$. Full details are standard. $\square$

**Theorem (closed graph).** Let $X,Y$ be Banach spaces and $T:X \to Y$ linear. Then $T$ is bounded if and only if its graph $\Gamma_T=\{(x,Tx)\} \subseteq X \times Y$ is closed.

*Proof.* If $T$ is bounded then $\Gamma_T$ is the preimage of the diagonal under the continuous map $(x,y)\mapsto Tx-y$, hence closed. Conversely, if $\Gamma_T$ is closed, it is a Banach space under the norm of $X \times Y$, and the projection $\Gamma_T \to X$ is a bounded linear bijection; by the bounded inverse theorem its inverse $x \mapsto (x,Tx)$ is bounded, so $T$ is bounded. $\square$

### Hahn–Banach

**Theorem (Hahn–Banach, analytic form).** Let $X$ be a real vector space, $p:X \to \mathbb{R}$ a seminorm, $M \subseteq X$ a subspace and $f:M \to \mathbb{R}$ linear with $f \le p$ on $M$. Then $f$ extends to a linear $\tilde f:X \to \mathbb{R}$ with $\tilde f \le p$ on $X$. Over $\mathbb{C}$ the extension preserves the norm of a bounded functional.

*Proof (sketch).* The one-step extension: for $x \notin M$, the values $\tilde f(x)=t$ making $\tilde f \le p$ on $M+\mathbb{R}x$ are those with $\sup_{m \in M}(f(m)-p(m-x)) \le t \le \inf_{m \in M}(p(m+x)-f(m))$, an interval shown nonempty by subadditivity of $p$; transfinite induction over a well-ordered basis of $X/M$ completes the extension. $\square$

**Corollary.** (i) For every $x \neq 0$ in a normed space there is $f \in X^*$ with $\|f\|=1$ and $f(x)=\|x\|$; hence $X^*$ separates points and $\|x\|=\sup_{\|f\|\le1}|f(x)|$. (ii) A subspace $M$ is dense if and only if every $f \in X^*$ vanishing on $M$ is zero. (iii) If $Y \subseteq X$ is a closed subspace and $x \notin Y$, there is $f \in X^*$ with $f|_Y=0$ and $f(x) \neq 0$.

*Proof.* (i) Apply the theorem to $M=\mathbb{K}x$ with the norm and the functional $\lambda x \mapsto \lambda\|x\|$. (ii) and (iii) are immediate from (i) applied in the quotient $X/\overline Y$. $\square$

## The Dual Space

**Definition.** The **dual space** of a normed space $X$ is $X^*=B(X,\mathbb{K})$ with the operator norm, and the **bidual** is $X^{**}=(X^*)^*$. The canonical map $J:X \to X^{**}$, $J(x)(f)=f(x)$, is a linear isometry by the corollary above. $X$ is **reflexive** if $J$ is surjective.

**Proposition.** $X^*$ is a Banach space for every normed $X$; $J$ is an isometry but need not be surjective; the weak topology on $X$ is the coarsest making every $f \in X^*$ continuous, and the weak-$*$ topology on $X^*$ is the coarsest making every evaluation $f \mapsto f(x)$ continuous. By the Banach–Alaoglu theorem, the closed unit ball of $X^*$ is weak-$*$ compact.

*Proof.* The completeness and the isometry were established above; the topologies are defined by the stated families of functionals, and Banach–Alaoglu is the statement that the product of the closed discs $\{|f(x)| \le \|x\|\}$ is compact, the ball being closed inside it. $\square$

**Example.** $\ell^p$ is reflexive for $1<p<\infty$, while $\ell^1$ and $\ell^\infty$ are not; $c_0$ is not reflexive, since $c_0^{**}=\ell^\infty \neq c_0$. Hilbert spaces are reflexive, by the Riesz representation theorem of the companion article on Banach and Hilbert spaces.

## Quotients, Direct Sums and Completion

**Theorem.** Let $X$ be a normed space and $M \subseteq X$ a closed subspace. Then the quotient $X/M$ with $\|x+M\|=\inf_{m \in M}\|x+m\|$ is a normed space, the quotient map is bounded and open with norm $1$ if $M \neq X$, and $X/M$ is a Banach space whenever $X$ is.

*Proof.* The quotient norm is well defined, since translating $x$ by an element of $M$ does not change the set of distances, and it satisfies the norm axioms; the quotient map has norm at most $1$ and exactly $1$ when $M \neq X$, choosing $x$ with $d(x,M)<1+\varepsilon$. Completeness passes to the quotient directly: from a Cauchy sequence $(x_n+M)$ pass to a subsequence with $\|(x_{n_{k+1}}-x_{n_k})+M\| \le 2^{-k}$ and choose representatives $u_k \in M$ with $\|x_{n_{k+1}}-x_{n_k}+u_k\| \le 2^{-k}$; the series $\sum_k(x_{n_{k+1}}-x_{n_k}+u_k)$ converges absolutely, hence converges in the Banach space $X$, and its partial sums differ from the $x_{n_j}$ by elements of $M$, so the subsequence, and therefore the Cauchy sequence itself, converges in $X/M$. $\square$

**Theorem.** For normed spaces $X_1,\dots,X_n$ the direct sum is a normed space under each of $\|(x_i)\|=\sum_i\|x_i\|$, $\max_i\|x_i\|$ and $(\sum_i\|x_i\|^2)^{1/2}$, these norms being equivalent, and it is complete exactly when every $X_i$ is. The direct sum of countably many nonzero Banach spaces is incomplete for each of these norms: its completion for the sum norm is the space of sequences with $\sum_i\|x_i\|<\infty$, and its completion for the supremum norm is the space of sequences with $\|x_i\| \to 0$.

*Proof.* Equivalence of the three norms reduces to equivalence of the corresponding norms on $\mathbb{K}^n$, together with homogeneity. Cauchy sequences are Cauchy in each coordinate and conversely, which gives both the completeness statement and the diagonal limit. For the countable case fix nonzero $x_i \in X_i$ with $\sum_i\|x_i\|<\infty$, and put $x^{(k)}=(x_1,\dots,x_k,0,\dots)$. Then $\|x^{(k)}-x^{(m)}\|$ is $\sum_{i>\min(k,m)}^{\max(k,m)}\|x_i\|$ for the sum norm and $\max_{i>\min(k,m)}\|x_i\|$ for the supremum norm, and both tend to $0$, so $(x^{(k)})$ is Cauchy in either norm. It has no limit in the direct sum: a limit $y$ there has finite support, and for $j$ outside that support and $k \ge j$ one has $\|x^{(k)}-y\| \ge \|x_j\|$, a fixed positive number, so the distance does not tend to $0$. Hence the direct sum is incomplete in both norms, and the two completions are the sequences with $\sum_i\|x_i\|<\infty$ and those with $\|x_i\| \to 0$. $\square$

**Corollary (completion).** Every normed space $X$ has a completion $\widehat X$, unique up to isometric isomorphism, which is a Banach space containing $X$ as a dense subspace. The completion of the finitely supported sequences under $\|\cdot\|_p$ is $\ell^p$, and the completion of $C[0,1]$ under $\|\cdot\|_1$ is $L^1[0,1]$.

*Proof.* Complete the metric space $X$; the vector operations and the norm extend by continuity and uniformity, and the result is a Banach space. Uniqueness is the universal property of the completion of a metric space. The finitely supported sequences are dense in $\ell^p$ and the continuous functions are dense in $L^1[0,1]$. $\square$

## Summary

A norm on a vector space gives it a metric and a topology; two norms are equivalent when each is bounded by a multiple of the other, and on a finite-dimensional space over $\mathbb{R}$ or $\mathbb{C}$ all norms are equivalent, so every finite-dimensional normed space is complete and every linear map out of one is continuous. A linear map is bounded exactly when it is continuous, and the bounded maps form a normed space under the operator norm, which is submultiplicative and complete when the target is complete; the dual $X^*$ is always a Banach space.

A Banach space is a complete normed space; in it absolute convergence implies convergence, and conversely that property characterises completeness. The closed unit ball is compact exactly in finite dimension, by Riesz's lemma, and separable Banach spaces need not have a Schauder basis, although separable Hilbert spaces do.

The four cornerstones rest on completeness and Baire category: the uniform boundedness principle says that a pointwise bounded family of bounded operators on a Banach space is uniformly bounded; the open mapping theorem says that a surjective bounded map between Banach spaces is open, so a bounded bijection has a bounded inverse; the closed graph theorem says that a linear map between Banach spaces with closed graph is bounded; and the Hahn–Banach theorem extends a linear functional bounded by a seminorm from a subspace to the whole space, giving the existence of norming functionals, the separation of points, and the description $\|x\|=\sup_{\|f\|\le1}|f(x)|$. The dual space and the canonical isometry $J:X \to X^{**}$ complete the picture; reflexivity is the surjectivity of $J$, it holds for $\ell^p$ with $1<p<\infty$ and for Hilbert spaces, and it fails for $c_0$, $\ell^1$ and $\ell^\infty$.

A quotient $X/M$ by a closed subspace is a normed space with the quotient norm, the quotient map is bounded and open, and the quotient is complete when $X$ is; a finite direct sum carries the equivalent sum, maximum and Euclidean norms and is complete exactly when every summand is, and every normed space has a unique completion, the completion of the finitely supported sequences under $\|\cdot\|_p$ being $\ell^p$ and that of $C[0,1]$ under $\|\cdot\|_1$ being $L^1[0,1]$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ |
| $\|\cdot\|$, $\|T\|$ | norm and operator norm |
| $B_\varepsilon$ | open ball of radius $\varepsilon$ |
| $B(X,Y)$ | bounded linear maps |
| $X^*=B(X,\mathbb{K})$ | dual space |
| $X^{**}$, $J$ | bidual and canonical isometry |
| $c_0$, $\ell^p$, $\ell^\infty$ | sequence spaces |
| $C(K)$, $L^p(\mu)$ | function spaces |
| $c_1$, $c_2$ | equivalence constants for norms |
| $M$, $Y$ | subspace, closed subspace |
| $\mathcal{F}$ | pointwise bounded family of operators |
| $\Gamma_T$ | graph of $T$ |

## Further Reading

- Stefan Banach, *Theory of Linear Operations* (North-Holland, 1987), for the original treatment of the cornerstones.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the standard proofs and the dual space.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the general theory.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the sharpness of the theorems.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, 2nd ed. 1991), for the Baire-based theorems and their applications.
- Kosaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the classical development of the normed theory.
