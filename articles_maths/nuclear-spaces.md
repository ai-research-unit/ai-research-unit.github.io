
# __Nuclear Spaces__

## Introduction

When two locally convex spaces are tensored, the algebraic tensor product carries more than one natural topology, and the two most important of them — the **projective** and the **injective** topology — differ in general. Grothendieck's discovery was that for a large and analytically significant class of spaces they coincide, for every second factor, and that this coincidence is equivalent to a summability condition on the approximation numbers of the space. Such spaces are the **nuclear spaces**, and they are the spaces for which the tensor product is well behaved, the kernel theorem holds, and every continuous linear map into a Banach space has a series representation with summable coefficients.

The class of nuclear spaces is a strict subclass of the Montel spaces, which are in turn a strict subclass of the reflexive spaces, all within the Fréchet class. The spaces of smooth functions, of holomorphic functions, of rapidly decreasing sequences and of distributions are nuclear; the Banach spaces of infinite dimension never are, and this single fact accounts for much of the difference between the behaviour of the two families. Nuclearity is the property that makes the spaces of analysis infinite-dimensional analogues of finite-dimensional spaces in the homological sense: kernels, traces and tensor products behave as they do in finite dimensions.

This article defines nuclear operators, the nuclear norm and the approximation numbers, the nuclear locally convex spaces, and the equivalent characterisations of nuclearity by tensor products, by seminorm factorisations and by summability of approximation numbers. It proves the finite-dimensionality of a nuclear Banach space, develops the closure properties, presents the standard examples, and states the kernel theorem of Grothendieck and the Schwartz kernel theorem. The topological tensor products that the definition uses are the subject in this Part, and the article recalls only what it needs; the theory of distributions and its applications are the subject of *Analysis on Linear Spaces* in Part III. Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and all spaces are locally convex over $\mathbb{K}$; a **Banach space** is a complete normed space, a **Fréchet space** is a complete metrisable locally convex space, and the notation is that of *Locally Convex Spaces*, *Fréchet Spaces* and *Duality Theory*.

---

## Nuclear Operators

### The Nuclear Norm

**Definition.** Let $E$, $F$ be normed spaces and let $T : E \to F$ be a continuous linear map. Then $T$ is **nuclear** if there are sequences $(a_n) \subseteq E'$, $(b_n) \subseteq F$ and $(\lambda_n) \subseteq \mathbb{K}$ with

$$
T x = \sum_{n=1}^\infty \lambda_n \langle x, a_n\rangle b_n , \qquad \sum_{n=1}^\infty \lvert \lambda_n \rvert \lVert a_n \rVert \lVert b_n \rVert < \infty ,
$$

the series converging in the norm of $F$ for every $x \in E$. The **nuclear norm** of $T$ is

$$
\lVert T \rVert_{\mathrm{nuc}} = \inf\Bigl\{\sum_{n=1}^\infty \lvert \lambda_n\rvert \lVert a_n\rVert \lVert b_n\rVert\Bigr\} ,
$$

the infimum over all such representations, and it is a norm on the space of nuclear operators.

**Proposition.** Let $E, F$ be normed spaces and let $T : E \to F$ be nuclear. Then

**(a)** $T$ is compact, and $\lVert T\rVert \leq \lVert T\rVert_{\mathrm{nuc}}$, where $\lVert T\rVert$ is the operator norm;

**(b)** the sum of two nuclear maps is nuclear, with $\lVert T_1 + T_2\rVert_{\mathrm{nuc}} \leq \lVert T_1\rVert_{\mathrm{nuc}} + \lVert T_2\rVert_{\mathrm{nuc}}$;

**(c)** if $S : F \to G$ and $R : G_0 \to E$ are continuous then $S T R$ is nuclear with $\lVert STR\rVert_{\mathrm{nuc}} \leq \lVert S\rVert \lVert T\rVert_{\mathrm{nuc}}\lVert R\rVert$;

**(d)** the nuclear maps form a Banach space under the nuclear norm; the space of nuclear maps is the completed projective tensor product $F \widehat{\otimes}_\pi E'$ when one of the spaces has the approximation property.

**Pro.** (a) The partial sums are finite-rank operators converging in the norm because $\lVert \sum_{n>N}\lambda_n\langle\cdot,a_n\rangle b_n\rVert \leq \sum_{n>N}\lvert\lambda_n\rvert\lVert a_n\rVert\lVert b_n\rVert$, so $T$ is the norm limit of finite-rank maps, hence compact; the inequality $\lVert T\rVert \leq \lVert T\rVert_{\mathrm{nuc}}$ follows by taking the supremum over the unit ball and using $\lvert\langle x,a_n\rangle\rvert \leq \lVert a_n\rVert$ for $\lVert x\rVert \leq 1$. (b) and (c) are immediate from the series representation, summing the two series and composing termwise. (d) is the standard identification of nuclear operators with the completed projective tensor product, which is the tensor-product statement. $\square$

**Example (a nuclear operator on $\ell^2$).** Let $T$ be the diagonal operator on $\ell^2$ with $T e_n = \lambda_n e_n$ where $\lambda_n = n^{-2}$. Then $T$ is nuclear with $\lVert T\rVert_{\mathrm{nuc}} = \sum_n n^{-2} = \pi^2/6 \approx 1.6449$, while $\lVert T\rVert = 1$. The example is the model nuclear operator: the coefficients are summable, the operator is compact of infinite rank, and its trace in the operator-theoretic sense is the sum of the eigenvalues, $\pi^2/6$; the derivation of the trace formula for nuclear operators, and the spectral theory that gives it, belong to *Analysis on Linear Spaces* in Part III.

**Example (the finite-dimensional case).** For $E = F = \mathbb{K}^n$ a linear map is nuclear, and the nuclear norm is the sum $\sigma_1 + \cdots + \sigma_n$ of the singular values; the operator norm is $\sigma_1$, and the identity has nuclear norm $n$ and operator norm $1$. The elementary inequality $\lVert T\rVert \leq \lVert T\rVert_{\mathrm{nuc}}$ is thus the inequality $\sigma_1 \leq \sigma_1 + \cdots + \sigma_n$, which is strict as soon as the rank exceeds $1$. The numerical evaluation of the singular values and of the two norms confirms the inequality on every tested matrix. The identity on $\ell^2$, by contrast, would have nuclear norm $\sum_n 1 = \infty$, which is the first sign that the identity on an infinite-dimensional space is not nuclear.

### Approximation Numbers

**Definition.** Let $E, F$ be Banach spaces and $T : E \to F$ a continuous linear map. The $n$-th **approximation number** (or **Kolmogorov diameter**) of $T$ is

$$
d_n(T) = \inf\{\lVert T - S\rVert : S : E \to F \text{ of rank} < n\} ,
$$

the infimum over the maps of rank at most $n-1$. The sequence $d_1(T) \geq d_2(T) \geq \cdots$ is non-increasing and non-negative, with $d_1(T) = \lVert T\rVert$, and $T$ is compact if and only if $d_n(T) \to 0$.

**Proposition.** Let $T : E \to F$ be a nuclear map of Banach spaces and let $T = \sum_k\lambda_k\langle\cdot,a_k\rangle b_k$ be a nuclear representation. Then for every $n \geq 1$

$$
d_n(T) \leq \sum_{k \geq n}\lvert\lambda_k\rvert\lVert a_k\rVert\lVert b_k\rVert ,
$$

the partial sum $\sum_{k<n}\lambda_k\langle\cdot,a_k\rangle b_k$ being a map of rank at most $n-1$; in particular $d_n(T) \to 0$, so that a nuclear operator between Banach spaces is compact. For operators between Hilbert spaces the two quantities agree, $\sum_{n\geq1} d_n(T) = \lVert T\rVert_{\mathrm{nuc}}$, the common value being the sum of the singular values.

**Proof.** The partial sum $S_{n-1} = \sum_{k<n}\lambda_k\langle\cdot,a_k\rangle b_k$ has rank at most $n-1$, so $d_n(T) \leq \lVert T - S_{n-1}\rVert$ and the norm of the difference is bounded by the triangle inequality and $\lvert\langle x,a_k\rangle\rvert \leq \lVert a_k\rVert\lVert x\rVert$; since the series $\sum_k\lvert\lambda_k\rvert\lVert a_k\rVert\lVert b_k\rVert$ converges, its tails tend to $0$, whence $d_n(T) \to 0$ and $T$ is the norm limit of finite-rank maps. On Hilbert spaces the approximation numbers of a compact operator are its singular values, and the nuclear norm of a diagonal operator with respect to an orthonormal basis is $\sum_k\lvert\lambda_k\rvert$, so the two quantities coincide; the general Hilbert-space statement follows by the spectral decomposition of the compact self-adjoint operator $(T^*T)^{1/2}$. $\square$

**Remark.** On Hilbert spaces the characterisation is exact: a bounded operator is nuclear exactly when the sum of its approximation numbers is finite, and that sum is the nuclear norm. On general Banach spaces the corresponding statement — that $T$ is nuclear if and only if $\sum_n d_n(T) < \infty$, with the nuclear norm equivalent to that sum — requires the approximation property, and it is the criterion by which nuclearity is checked in practice; it is quoted from the standard references, and the Fréchet-space counterpart is the seminorm characterisation given below.

---

## Nuclear Locally Convex Spaces

### The Definition and its Equivalents

**Definition.** A locally convex space $E$ is **nuclear** if for every locally convex space $F$ the canonical map

$$
E \widehat{\otimes}_\pi F \longrightarrow E \widehat{\otimes}_\varepsilon F
$$

from the completed projective tensor product to the completed injective tensor product is a topological isomorphism.

**Remark.** The projective and injective topologies are defined as follows. The projective topology on $E \otimes F$ is the finest locally convex topology for which the canonical bilinear map $E \times F \to E \otimes F$ is continuous; the injective topology is the topology of uniform convergence on the equicontinuous subsets of the dual of the tensor product, equivalently the coarsest topology making the canonical embedding $E \otimes F \hookrightarrow \mathcal{B}(E'_\sigma \times F'_\sigma)$ continuous, where the target carries the topology of uniform convergence on the products of equicontinuous sets. Both are treated systematically, written in this Part; the present article uses only the fact that the identity map $E\widehat{\otimes}_\pi F \to E\widehat{\otimes}_\varepsilon F$ is always continuous and may fail to be a homeomorphism.

**Theorem (characterisation by seminorms).** Let $E$ be a locally convex space. Then $E$ is nuclear if and only if for every continuous seminorm $p$ on $E$ there is a continuous seminorm $q \geq p$ on $E$ such that the canonical map

$$
\widehat{E}_q \longrightarrow \widehat{E}_p
$$

between the completions of the quotients $E/\ker q$ and $E/\ker p$ is nuclear; here $\widehat{E}_p$ carries the norm induced by $p$.

**Proof.** The condition is Grothendieck's description of nuclearity in terms of seminorms; its equivalence with the tensor-product definition is proved by factoring an arbitrary map through the completions of the seminorm quotients and reducing to the Banach case. It is quoted as standard. $\square$

**Theorem (characterisation by approximation numbers).** Let $E$ be a Fréchet space with an increasing generating sequence $(p_n)$ of seminorms. Then $E$ is nuclear if and only if for every $n$ there is $m > n$ such that the canonical map

$$
\widehat{E}_{p_m} \longrightarrow \widehat{E}_{p_n}
$$

has summable approximation numbers,

$$
\sum_{k \geq 1} d_k\bigl(\widehat{E}_{p_m} \to \widehat{E}_{p_n}\bigr) < \infty .
$$

**Proof.** The summability of the approximation numbers is equivalent, by the proposition above, to the nuclearity of the canonical map; the passage from the Banach case to the Fréchet case uses the projective limit description and a diagonal argument to replace the family of seminorms by a cofinal sequence. It is quoted as standard. $\square$

### The Basic Structure Theorems

**Theorem.** Let $E$ be a nuclear locally convex space. Then:

**(a)** every continuous linear map from $E$ into a Banach space is nuclear, the seminorm condition being exactly the factorisation of such a map through a nuclear map between Banach spaces;

**(b)** $E$ is Montel when it is Fréchet; in particular a nuclear Fréchet space is reflexive and separable, and every closed bounded subset is compact;

**(c)** every subspace and every Hausdorff quotient of a nuclear space is nuclear;

**(d)** arbitrary products, countable direct sums and projective limits of nuclear spaces are nuclear;

**(e)** the strong dual of a nuclear Fréchet space is nuclear, and the strong dual is a Montel space.

**Proof.** (a) is the equivalence of the seminorm characterisation with the definition. (b) A Fréchet space is nuclear precisely when the maps between the completions of the seminorm quotients are nuclear, hence compact; it follows that a bounded set, which is bounded in some $\widehat{E}_{p_n}$, is precompact for the topology defined by a larger seminorm, hence relatively compact, so every closed bounded set is compact and the space is Montel. (c)–(e) are standard closure properties, proved by restricting the seminorm condition to subspaces, pushing it forward to quotients, and dualising it for the strong dual. $\square$

**Corollary (a nuclear Banach space is finite-dimensional).** Let $E$ be a Banach space which is nuclear. Then $E$ is finite-dimensional.

**Proof.** The canonical map $\widehat{E}_p \to \widehat{E}_p$ is the identity on a Banach space, and by Proposition (a) above it is compact; the closed unit ball is therefore compact, which is equivalent to finite dimension. $\square$

**Remark.** The corollary is the reason that the examples of nuclear spaces are all infinite-dimensional spaces of functions or sequences with a topology strictly finer than any norm topology. It also shows that nuclearity cannot be checked on a single norm and is genuinely a statement about a whole family of seminorms.

---

## Examples and the Kernel Theorem

### The Standard Examples

**Example ($\mathbb{K}^n$).** Every finite-dimensional locally convex space is nuclear: for the unique Hausdorff locally convex topology, the identity map between the (single) completions is the identity of a finite-dimensional space, which is nuclear. This is the trivial case, and the corollary above shows it is the only case that is also Banach.

**Example ($\mathcal{S}(\mathbb{R}^n)$).** The Schwartz space is nuclear. The seminorms $p_{m,\beta}(f) = \sup_x (1 + \lvert x\rvert^2)^m\lvert\partial^\beta f\rvert$ may be arranged in an increasing sequence, and the canonical map $\widehat{\mathcal{S}}_{p_{m+1,\beta}} \to \widehat{\mathcal{S}}_{p_{m,\beta}}$ is a weighted Sobolev embedding which is nuclear because the weights differ by a factor with summable eigenvalues; this is the standard proof that the Schwartz space is nuclear. In particular $\mathcal{S}$ is a nuclear Fréchet space, and hence Montel, reflexive and separable, and its strong dual $\mathcal{S}'$ is the nuclear space of tempered distributions.

**Example ($C^\infty(U)$ and $\mathcal{O}(\Omega)$).** The space $C^\infty(U)$ of smooth functions on a smooth manifold $U$ is a nuclear Fréchet space: the seminorms over an exhaustion by compacta together with the derivative orders are indexed by a double sequence, and the Sobolev embedding theorem provides the summability of the approximation numbers for the comparison maps. The space $\mathcal{O}(\Omega)$ of holomorphic functions on a domain is nuclear for the same reason, by the Cauchy estimates. The space $C_c^\infty(U)$ of compactly supported smooth functions with its LF topology is nuclear and complete but not metrisable; it is the standard nuclear space outside the Fréchet class.

**Example (rapidly decreasing sequences).** The space $s$ of sequences $(a_k)$ with $\sup_k k^m\lvert a_k\rvert < \infty$ for every $m$ is nuclear Fréchet, and it is isomorphic to $\mathcal{S}(\mathbb{R})$; a structure theorem for nuclear Fréchet spaces states that every one of them is isomorphic to a closed subspace of $s$, which is the sequence-space form of the seminorm characterisation.

**Example (a non-nuclear Fréchet space).** A Banach space of infinite dimension is not nuclear, by the corollary. Consequently $\ell^p$ for $1 \leq p \leq \infty$, $c_0$, $C(X)$ for infinite compact $X$ with the supremum norm and $L^p[0,1]$ are not nuclear, even where they are reflexive or separable; nuclearity is strictly stronger than reflexivity. The space $C(\mathbb{R})$ with the topology of compact convergence is a Fréchet space which is neither Montel nor nuclear: the restriction map onto $C([0,1])$ is a continuous surjection onto an infinite-dimensional Banach space, so nuclearity fails by the closure of nuclearity under quotients and the finite-dimensionality of nuclear Banach spaces, and the bounded sequence $f_n(x) = \sin(nx)$ has no locally uniformly convergent subsequence, so Montel fails. The two properties are independent in general, though nuclear implies Montel.

**Remark (the non-Archimedean analogue).** There is a theory of nuclear spaces over a non-Archimedean field, in which the completed tensor products studied here have a $p$-adic counterpart and in which the spaces of convergent power series and of analytic functions play the role of the smooth and holomorphic spaces; the adic and rigid spaces of the first category of this Part supply the geometric setting. The definitions and the principal theorems are analogous but the proof techniques differ, and the theory is not used in this article.

### The Kernel Theorem

**Theorem (Grothendieck's kernel theorem).** Let $E$ and $F$ be nuclear Fréchet spaces, or more generally let $E$ be nuclear and $F$ a complete locally convex space. Then the canonical map

$$
E \widehat{\otimes}_\pi F \longrightarrow E \widehat{\otimes}_\varepsilon F
$$

is a topological isomorphism, and the completed tensor product is a nuclear space. Consequently every continuous bilinear form on $E \times F$ corresponds to a continuous linear functional on the completed tensor product, and there is no ambiguity in the notation $E \widehat{\otimes} F$ for nuclear $E$.

**Proof.** The isomorphism of the two topologies is the definition of nuclearity, and the nuclearity of the completed tensor product follows from the seminorm characterisation applied to the product family of seminorms; the correspondence of bilinear forms and functionals is the universal property of the projective tensor product. The statement is Grothendieck's theorem; it is quoted as standard. $\square$

**Theorem (Schwartz kernel theorem).** Let $U \subseteq \mathbb{R}^m$ and $V \subseteq \mathbb{R}^n$ be open. Then every continuous linear map $T : C_c^\infty(U) \to \mathcal{D}'(V)$ is represented by a unique distribution $K_T \in \mathcal{D}'(U \times V)$ with

$$
\langle T f, g\rangle = \langle K_T, f \otimes g \rangle \qquad (f \in C_c^\infty(U), \ g \in C_c^\infty(V)) ,
$$

and the correspondence $T \leftrightarrow K_T$ is a linear bijection.

**Proof.** The kernel theorem is the statement that $\mathcal{D}'(U \times V) \cong \mathcal{D}'(U) \widehat{\otimes}\mathcal{D}'(V)$ for the relevant tensor topology, which holds because the spaces $C_c^\infty$ are nuclear; the identification with continuous linear maps is the universal property. The theory of distributions, of which the statement is a part, belongs to *Analysis on Linear Spaces* in Part III; the topological content, namely the coincidence of the tensor topologies for nuclear spaces, is the present article's contribution. $\square$

**Remark.** The kernel theorem is the sharpest illustration of the analytic value of nuclearity: the correspondence between operators and kernels, which in finite dimensions is the correspondence between matrices and linear maps, extends verbatim to the nuclear infinite-dimensional spaces of analysis and fails without the nuclearity hypothesis. This is the sense in which nuclear spaces are the infinite-dimensional spaces that behave like finite-dimensional ones.

---

## Summary

A continuous linear map $T : E \to F$ of normed spaces is **nuclear** if it has a series representation $T = \sum_n\lambda_n\langle\cdot,a_n\rangle b_n$ with $\sum_n\lvert\lambda_n\rvert\lVert a_n\rVert\lVert b_n\rVert < \infty$; the infimum of the sums is the **nuclear norm** $\lVert T\rVert_{\mathrm{nuc}}$, which dominates the operator norm, and a nuclear operator is compact, the sum of two nuclear operators and the composition of a nuclear operator with continuous maps being nuclear. The $n$-th **approximation number** $d_n(T)$ is the distance from $T$ to the maps of rank less than $n$; it satisfies $\sum_n d_n(T) \leq \lVert T\rVert_{\mathrm{nuc}}$. A locally convex space $E$ is **nuclear** if the canonical map $E\widehat{\otimes}_\pi F \to E\widehat{\otimes}_\varepsilon F$ is a topological isomorphism for every locally convex $F$; equivalently, if for every continuous seminorm $p$ there is a larger continuous seminorm $q$ for which the canonical map $\widehat{E}_q \to \widehat{E}_p$ is nuclear; equivalently, for Fréchet spaces, if for every $n$ there is $m>n$ for which the approximation numbers of the canonical map $\widehat{E}_{p_m} \to \widehat{E}_{p_n}$ are summable. A nuclear Banach space is finite-dimensional, so the interesting nuclear spaces are the infinite-dimensional Fréchet and LF spaces.

Nuclear spaces are stable under the formation of subspaces, Hausdorff quotients, products, countable direct sums and projective limits; a nuclear Fréchet space is **Montel**, hence reflexive and separable, and its strong dual is nuclear and Montel. The standard examples are the finite-dimensional spaces, the Schwartz space $\mathcal{S}(\mathbb{R}^n)$ with its strong dual $\mathcal{S}'$ of tempered distributions, the spaces $C^\infty(U)$ and $\mathcal{O}(\Omega)$, the space $s$ of rapidly decreasing sequences, and the LF space $C_c^\infty(U)$; the infinite-dimensional Banach spaces, in particular $\ell^p$, $c_0$, $C(X)$ and $L^p[0,1]$, are not nuclear. **Grothendieck's kernel theorem** states that the projective and injective completed tensor products of nuclear spaces coincide, and **Schwartz's kernel theorem** identifies continuous linear maps between spaces of test functions with distributions on the product, the infinite-dimensional form of the correspondence between linear maps and matrices. The systematic theory of the tensor products used here is standard, and the theory of distributions that the kernel theorem serves belongs to *Analysis on Linear Spaces* in Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T : E \to F$ | Continuous linear map of normed or locally convex spaces |
| $\lVert T\rVert_{\mathrm{nuc}}$ | Nuclear norm |
| $d_n(T)$ | $n$-th approximation number (Kolmogorov diameter) |
| $E\widehat{\otimes}_\pi F$ | Completed projective tensor product |
| $E\widehat{\otimes}_\varepsilon F$ | Completed injective tensor product |
| $\widehat{E}_p$ | Completion of $E/\ker p$ for the seminorm $p$ |
| $(p_n)$ | Increasing generating sequence of seminorms |
| $\mathcal{S}$, $\mathcal{S}'$ | Schwartz space and tempered distributions |
| $s$ | Space of rapidly decreasing sequences |
| $C_c^\infty(U)$, $\mathcal{D}'(U)$ | Test functions and distributions |
| $K_T$ | Schwartz kernel of a continuous linear map |
| Montel, nuclear | Properties of locally convex spaces |



## Further Reading

- Alexandre Grothendieck, *Produits tensoriels topologiques et espaces nucléaires* (Memoirs of the American Mathematical Society, 1955), for the original definition of nuclear spaces, the tensor-product theorem and the kernel theorem.
- Alexandre Grothendieck, "Résumé de la théorie métrique des produits tensoriels topologiques", *Boletim da Sociedade Matemática de São Paulo* **8** (1956), 1–79, for the metric theory of tensor products and the approximation numbers.
- Albrecht Pietsch, *Nuclear Locally Convex Spaces* (Springer, 1972), for the characterisation of nuclearity by approximation numbers and the structure theory.
- Albrecht Pietsch, *Operator Ideals* (North-Holland, 1980), for nuclear, Hilbert–Schmidt and absolutely summing operators and their ideals.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for nuclear spaces, the kernel theorem and its use in distribution theory.
- Laurent Schwartz, *Théorie des distributions* (Hermann, 1966), for the kernel theorem in its original form.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition 1999), for nuclearity and its relation to the approximation property.
