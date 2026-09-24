
# __Topological Tensor Products__

## Introduction

The algebraic tensor product of two vector spaces is defined by a universal property, and the property is purely algebraic: bilinear maps on $E \times F$ correspond to linear maps on $E \otimes F$. When $E$ and $F$ carry topologies, the correspondence should be between *continuous* bilinear maps and *continuous* linear maps, and this requires a topology on $E \otimes F$. There is no single natural choice: the finest locally convex topology making the canonical bilinear map continuous is the **projective topology**, and the initial topology induced by the embedding of $E \otimes F$ into the space of separately continuous bilinear forms is the **injective topology**. They coincide exactly when one of the factors is nuclear — a result of *Nuclear Spaces* — and in general the two completions differ, with the injective completion always containing the projective one.

The theory of these two topologies, together with the intermediate tensor topologies, is Grothendieck's theory of topological tensor products. It supplies the exact formulation of the universal property that multilinear analysis needs, the identifications of the completed tensor products of the classical Banach spaces, and the construction of tensor products of algebras and of Hilbert spaces. The last of these is the foundation of the tensor products of operator algebras: a Hilbert space tensor product is a Hilbert space, and the operator algebras on it are the completions of the algebraic tensor products of their factors in the norm or the weak topology. That construction is used throughout the operator-algebraic other articles in this Part.

This article defines the projective and injective topologies, proves the universal property of the projective tensor product, identifies the two completions in the classical cases, treats the tensor product of Hilbert spaces and the operator-space structures that arise from it, and states Grothendieck's inequality and the theorems on when the two topologies coincide, including the nuclear case. The operator theory of the resulting spaces, and the spectral theory of the operators they represent, belong to *Analysis on Linear Spaces* in Part III. Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and all spaces are locally convex over $\mathbb{K}$. For a locally convex space $E$, the dual is $E'$, the weak-star topology on $E'$ is $\sigma(E',E)$, and the space of continuous linear maps is $\mathcal{L}(E,F)$. The **algebraic tensor product** is written $E \otimes F$ and the completions $E \widehat{\otimes}_\pi F$ and $E \widehat{\otimes}_\varepsilon F$ denote the projective and the injective completion respectively.

---

## The Two Topologies

### The Projective Tensor Product

**Definition.** Let $E$ and $F$ be locally convex spaces. The **projective topology** on $E \otimes F$ is the finest locally convex topology for which the canonical bilinear map

$$
\otimes : E \times F \longrightarrow E \otimes F, \qquad (x,y) \longmapsto x \otimes y
$$

is continuous. The **projective tensor product** $E \widehat{\otimes}_\pi F$ is the completion of $E \otimes F$ for that topology.

**Theorem (universal property).** Let $E$, $F$, $G$ be locally convex spaces and let $B : E \times F \to G$ be a continuous bilinear map. Then there is a unique continuous linear map $\widetilde{B} : E \widehat{\otimes}_\pi F \to G$ with $B(x,y) = \widetilde{B}(x \otimes y)$; the correspondence $B \leftrightarrow \widetilde{B}$ is a linear bijection between the continuous bilinear maps and the continuous linear maps.

**Proof.** The projective topology is by definition the finest making $\otimes$ continuous, so $B$ factors through $\otimes$ as a linear map $\widetilde{B}$ on the algebraic tensor product, and the definition of the projective topology as the finest is precisely the statement that $\widetilde{B}$ is continuous; the extension to the completion is the universal property of completion. Uniqueness is the density of $E \otimes F$. $\square$

**Proposition (the projective norm for normed spaces).** Let $E$, $F$ be normed spaces and let $u \in E\otimes F$. Then

$$
\lVert u\rVert_\pi = \inf\Bigl\{\sum_{k=1}^{n}\lVert x_k\rVert\lVert y_k\rVert : u = \sum_{k=1}^n x_k\otimes y_k\Bigr\} ,
$$

the infimum over all finite representations of $u$; this is a norm on $E \otimes F$ generating the projective topology, and its completion is $E\widehat{\otimes}_\pi F$.

**Proof.** The formula defines a seminorm by the standard homogeneity and subadditivity computation, and it is the gauge of the convex balanced hull of $\{x \otimes y : \lVert x\rVert \leq 1, \lVert y\rVert \leq 1\}$; it is a norm because $\lVert x\otimes y\rVert_\pi = \lVert x\rVert\lVert y\rVert$ for elementary tensors and the norm is non-degenerate on the algebraic tensor product. The topology it generates is the projective topology by the universal property, since it is the finest norm making $\otimes$ a contraction. $\square$

**Example (sequence identifications).** The projective tensor product of $\ell^1$ with a Banach space $E$ is the space of summable sequences in $E$:

$$
\ell^1 \widehat{\otimes}_\pi E \cong \Bigl\{(x_k) \in E^{\mathbb{N}} : \sum_k \lVert x_k\rVert < \infty\Bigr\} ,
$$

with the norm $\sum_k\lVert x_k\rVert$; in particular $\ell^1\widehat{\otimes}_\pi\ell^1 \cong \ell^1$, and $L^1[0,1]\widehat{\otimes}_\pi L^1[0,1] \cong L^1([0,1]^2)$ under the identification of the tensor product with functions of two variables. These identifications are proved by using the density of elementary tensors and the universal property of the projective tensor product.

### The Injective Tensor Product

**Definition.** Let $E$ and $F$ be locally convex spaces and let $E'_\sigma$, $F'_\sigma$ denote the duals with the weak-star topologies. The canonical map

$$
E \otimes F \longrightarrow \mathcal{B}\bigl(E'_\sigma \times F'_\sigma\bigr), \qquad x \otimes y \longmapsto \bigl((\xi,\eta) \mapsto \langle x,\xi\rangle\langle y,\eta\rangle\bigr)
$$

is injective when $E$ and $F$ are Hausdorff locally convex spaces. The **injective topology** on $E \otimes F$ is the topology of uniform convergence on the products of equicontinuous subsets of $E'$ and $F'$, that is, the initial topology induced by this embedding when the target carries the topology of uniform convergence on the products of equicontinuous sets. The **injective tensor product** $E \widehat{\otimes}_\varepsilon F$ is the completion.

**Proposition.** Let $E$, $F$ be normed spaces and let $u \in E\otimes F$. Then

$$
\lVert u\rVert_\varepsilon = \sup\bigl\{\lvert (\xi\otimes\eta)(u)\rvert : \xi \in E', \ \eta \in F', \ \lVert\xi\rVert \leq 1, \ \lVert\eta\rVert \leq 1\bigr\} ,
$$

and this is a norm on $E\otimes F$ generating the injective topology; it satisfies $\lVert u\rVert_\varepsilon \leq \lVert u\rVert_\pi$ for every $u$.

**Proof.** The displayed supremum is finite and defines a norm by the description of $\mathcal{B}(E'_1\times F'_1)$ as a space of bounded functions; the inequality $\lVert\cdot\rVert_\varepsilon \leq \lVert\cdot\rVert_\pi$ follows by evaluating the representation $u = \sum_k x_k \otimes y_k$ on $\xi \otimes \eta$ and applying the triangle inequality. $\square$

**Example (the injective identifications).** For compact Hausdorff spaces $X$, $Y$ one has

$$
C(X) \widehat{\otimes}_\varepsilon C(Y) \cong C(X \times Y)
$$

with the supremum norms; similarly the injective tensor product of the sequence space $c_0$ with a Banach space $E$ is the space $c_0(E)$ of $E$-valued sequences tending to $0$ with the supremum norm.

**Theorem (the comparison map).** Let $E$, $F$ be locally convex spaces. Then the identity of $E\otimes F$ extends to a continuous linear map

$$
E \widehat{\otimes}_\pi F \longrightarrow E \widehat{\otimes}_\varepsilon F ,
$$

which is injective when $E$ and $F$ are Hausdorff, and it is a topological isomorphism for all $F$ if and only if $E$ is nuclear.

**Proof.** The continuity is the inequality $\lVert\cdot\rVert_\varepsilon \leq \lVert\cdot\rVert_\pi$ of the preceding proposition in the normed case, and the general case follows by reducing to the seminorm quotients. Injectivity is the injectivity of the canonical map into the space of bilinear forms on the dual, using the Hahn–Banach theorem. The final statement is Grothendieck's characterisation of nuclearity, which was stated and used in *Nuclear Spaces*. $\square$

---

## The Classical Identifications

### Finite Dimensions and Hilbert Spaces

**Example (finite-dimensional spaces).** For $E = \mathbb{K}^m$ and $F = \mathbb{K}^n$ the tensor product $\mathbb{K}^m\otimes\mathbb{K}^n$ is the space $M_{m,n}(\mathbb{K})$ of $m\times n$ matrices under the identification $e_i \otimes f_j \leftrightarrow E_{ij}$, and every tensor topology on a finite-dimensional space is the same. The three norms that arise are the operator norm

$$
\lVert A\rVert_{\mathrm{op}} = \sigma_1 , \qquad \lVert A\rVert_{\mathrm{HS}} = \Bigl(\sum_i \sigma_i^2\Bigr)^{1/2}, \qquad \lVert A\rVert_{\mathrm{nuc}} = \sum_i \sigma_i ,
$$

where $\sigma_1 \geq \sigma_2 \geq \cdots$ are the singular values of $A$; the first is the injective norm, the third is the projective norm, and the second is the norm of the Hilbert tensor product when the factors carry their Euclidean inner products. The three norms agree only for rank-one matrices, and in general they satisfy

$$
\lVert A\rVert_{\mathrm{op}} \leq \lVert A\rVert_{\mathrm{HS}} \leq \lVert A\rVert_{\mathrm{nuc}} .
$$

The chain of inequalities is the elementary comparison $\sigma_1 \leq (\sum_i\sigma_i^2)^{1/2} \leq \sum_i\sigma_i$ of the singular values; the identity matrix has the three norms $1$, $\sqrt2$ and $2$, so the inequalities are strict simultaneously, and the second is an equality exactly when the rank is at most one. The same computation identifies the Hilbert tensor product of the Euclidean spaces with $M_{m,n}$ carrying the Hilbert–Schmidt norm.

**Definition.** Let $H_1$, $H_2$ be Hilbert spaces. The **Hilbert tensor product** $H_1\widehat{\otimes}H_2$ is the completion of the algebraic tensor product for the inner product

$$
\langle x_1\otimes x_2, y_1\otimes y_2\rangle = \langle x_1,y_1\rangle\langle x_2,y_2\rangle ,
$$

extended sesquilinearly. It is a Hilbert space, and if $(e_i)$ and $(f_j)$ are orthonormal bases of $H_1$ and $H_2$ then $(e_i \otimes f_j)$ is an orthonormal basis of $H_1\widehat{\otimes}H_2$.

**Theorem.** Let $H_1$, $H_2$ be Hilbert spaces. Then the Hilbert tensor product $H_1\widehat{\otimes}H_2$ is a Hilbert space with positive definite inner product, and for $H_1 = H_2 = H$ separable of infinite dimension the identifications

$$
H \widehat{\otimes} H \cong S_2(H)
$$

hold, where $S_2(H)$ is the space of Hilbert–Schmidt operators on $H$; the injective completion $H\widehat{\otimes}_\varepsilon H$ is the space of compact operators $S_\infty(H)$, and the projective completion $H\widehat{\otimes}_\pi H$ is the space of trace-class operators $S_1(H)$.

**Proof.** The positivity of the inner product is checked on finite tensor combinations by writing them as matrices in a basis and using that the resulting Gram matrix is positive semidefinite; the orthonormal basis statement is the standard separability computation, and the identifications of the completions are Grothendieck's computations for Hilbert spaces, in which the nuclear and Hilbert–Schmidt norms are compared through the singular values. The operator-theoretic development of the trace class and the Hilbert–Schmidt class belongs to *Analysis on Linear Spaces* in Part III. $\square$

**Example (the Schwartz space tensor product).** For the Schwartz space the nuclearity of *Nuclear Spaces* gives

$$
\mathcal{S}(\mathbb{R}^m) \widehat{\otimes} \mathcal{S}(\mathbb{R}^n) \cong \mathcal{S}(\mathbb{R}^{m+n}) ,
$$

with the two completed tensor topologies agreeing, since $\mathcal{S}$ is nuclear; the same holds for $C^\infty$ and for the holomorphic functions on a product. This is the source of the kernel theorem, and it is the reason the tensor product notation carries no ambiguity for the spaces of analysis.

### Grothendieck's Inequality

**Theorem (Grothendieck's inequality).** There is a universal constant $K_G$, with $1 < K_G < 2$, such that for every $n$, every $m$ and every real matrix $(a_{ij})$,

$$
\max\Bigl\{\sum_{i,j}a_{ij}\langle s_i, t_j\rangle\Bigr\} \leq K_G \max\Bigl\{\Bigl\lvert\sum_{i,j}a_{ij}s_it_j'\Bigr\rvert\Bigr\} ,
$$

the first supremum over Hilbert-space vectors $s_i$, $t_j$ of norm at most $1$ and the second over real numbers $s_i$, $t_j'$ of modulus at most $1$.

**Proof.** The theorem is Grothendieck's inequality, in the form of the comparison between the norms of the tensor product and of the space of bounded bilinear forms; it is proved by a randomisation argument with Gaussian variables, or by the factorisation theory of $\gamma$-summing operators. It is quoted here as standard. The best general bound in the real case is Krivine’s $K_G \leq \pi/(2\ln(1+\sqrt2)) \approx 1.7822$, and the exact value of the real Grothendieck constant is not known; the theorem needs only that $K_G < 2$. $\square$

**Remark.** Grothendieck's inequality quantifies how far the injective and projective tensor products on $\ell^2$ can be from each other: the identity map $\ell^2\widehat{\otimes}_\pi\ell^2 \to \ell^2\widehat{\otimes}_\varepsilon\ell^2$ is a topological isomorphism onto its image with distortion at most $K_G$ in the real case, but it is not surjective onto the injective completion. The constant is the basis of the theory of **absolutely summing operators** and of the metric theory of tensor products, whose operator-theoretic content belongs to *Analysis on Linear Spaces* in Part III.

**Remark (the problem of topologies).** Grothendieck's *problème des topologies* asks whether the completion of the projective tensor product of two Fréchet spaces is Fréchet and whether the injective tensor product of two Fréchet spaces is complete; the answer is negative in general, and the counterexamples are spaces of the type $E = F = $ a Fréchet space of analytic functionals. The positive results are available when one factor is nuclear, in which case the two completions coincide and are Fréchet; the finer theory of the $\varepsilon$-product and the $\pi$-product of Schwartz belongs to the general theory of topological tensor products and is not needed for the operator-algebraic applications below.

---

## Duality and the Nuclear Norm

### Trace Duality

**Theorem (trace duality; standard).** Let $E$, $F$ be Banach spaces. The formula

$$
\langle x\otimes y, T\rangle = \langle y, Tx\rangle , \qquad x \in E, \quad y \in F, \quad T \in \mathcal{B}(E,F') ,
$$

defines a duality under which $(E\widehat{\otimes}_\pi F)'$ is isometrically isomorphic to $\mathcal{B}(E,F')$.

**Proof.** For $T \in \mathcal{B}(E,F')$ the form $(x,y)\mapsto\langle y,Tx\rangle$ is bilinear and continuous with $\lvert\langle y,Tx\rangle\rvert \leq \lVert T\rVert\lVert x\rVert\lVert y\rVert$, so by the universal property of the projective tensor product it defines a functional $J(T)$ on $E\widehat{\otimes}_\pi F$ with $\lVert J(T)\rVert \leq \lVert T\rVert$. Conversely, a functional $\varphi$ on $E\widehat{\otimes}_\pi F$ determines a linear map $T_\varphi : E \to F'$ by $\langle T_\varphi x, y\rangle = \varphi(x\otimes y)$, which is bounded because $\lvert\langle T_\varphi x, y\rangle\rvert \leq \lVert\varphi\rVert\lVert x\rVert\lVert y\rVert$ for all $y$, whence $\lVert T_\varphi\rVert \leq \lVert\varphi\rVert$. The two passages are inverse on the dense subspace of elementary tensors, and the isometry follows because the norm of $J(T)$ is the supremum of $\lvert\langle y,Tx\rangle\rvert$ over the pairs with $\lVert x\rVert \leq 1$, $\lVert y\rVert \leq 1$, that is $\sup\{\lVert Tx\rVert : \lVert x\rVert\leq1\} = \lVert T\rVert$. $\square$

**Corollary (the finite-dimensional duality).** For $E = \mathbb{K}^m$ and $F = \mathbb{K}^n$, with $E\otimes F = M_{m,n}(\mathbb{K})$ as in the previous section, the theorem says that the nuclear norm and the operator norm are dual to one another: the supremum of $\lvert\operatorname{tr}(A^{\mathsf T}B)\rvert$ over the matrices $B$ with $\lVert B\rVert_{\mathrm{op}}\leq1$ equals $\lVert A\rVert_{\mathrm{nuc}}$, so that $(M_{m,n},\lVert\cdot\rVert_{\mathrm{op}})' \cong (M_{m,n},\lVert\cdot\rVert_{\mathrm{nuc}})$ isometrically. In the diagonal case $A = \operatorname{diag}(\sigma_1,\sigma_2)$ with $\sigma_1 \geq \sigma_2 \geq 0$ the value $\sigma_1+\sigma_2$ is attained at the diagonal $B$ with entries $1$ and $\operatorname{sign}$; both norms are invariant under the changes of orthonormal bases that conjugate $A$ into that form, so the identity holds in general, and the inequality $\lvert\operatorname{tr}(A^{\mathsf T}B)\rvert \leq \lVert A\rVert_{\mathrm{nuc}}\lVert B\rVert_{\mathrm{op}}$ has been checked on the general case, with equality at the orthogonal factor of the polar decomposition of $A$.

**Example (the trace class as a predual).** For a Hilbert space $H$ the projective tensor product $H\widehat{\otimes}_\pi H'$, in which the second factor is the dual identified with the conjugate Hilbert space, is isometrically the trace class $S_1(H)$ of operators with $\operatorname{Tr}\lvert T\rvert < \infty$, and the theorem gives

$$
S_1(H)' \cong B(H)
$$

isometrically, with the pairing $\langle T, A\rangle = \operatorname{Tr}(TA)$. Thus the trace class is a predual of $B(H)$; in finite dimensions this is the duality of the preceding corollary.

**Remark.** The dual $(E\widehat{\otimes}_\varepsilon F)'$ is described in the metric theory of tensor products by the integral operators, and the comparison of that description with the nuclear operators of *Nuclear Spaces* involves hypotheses of approximation type on $E$; these are standard results of the metric theory and are quoted where used, while the present article needs only the projective duality above.

---

## Tensor Products of Algebras

**Definition.** Let $A$ and $B$ be locally convex algebras over $\mathbb{K}$. The algebraic tensor product $A\otimes B$ is an algebra with the product $(a_1\otimes b_1)(a_2\otimes b_2) = a_1a_2\otimes b_1b_2$, and the projective tensor topology makes the multiplication continuous when both factors have a continuous multiplication, by applying the universal property to the bilinear multiplication map. The **projective tensor product algebra** $A\widehat{\otimes}_\pi B$ is the completion, and it is a locally convex algebra whose multiplication is continuous.

**Proposition.** Let $A$, $B$ be Banach algebras. Then $A\widehat{\otimes}_\pi B$ is a Banach algebra with $\lVert u v\rVert_\pi \leq \lVert u\rVert_\pi\lVert v\rVert_\pi$; it is commutative if $A$ and $B$ are, and continuous multiplicative bilinear maps on $A\times B$ correspond to continuous algebra homomorphisms on $A\widehat{\otimes}_\pi B$.

**Proof.** The submultiplicativity of the projective norm follows from the representations $u = \sum_k a_k \otimes b_k$, $v = \sum_l a_l'\otimes b_l'$ and the estimate on the products; the universal property is the universal property of the projective tensor product restricted to multiplicative bilinear maps. $\square$

**Remark (the operator-algebraic case).** The Hilbert tensor product of the previous section supplies the model for the tensor products of operator algebras. If $A \subseteq B(H_1)$ and $B \subseteq B(H_2)$ are algebras of operators, the algebraic tensor product acts on the Hilbert tensor product $H_1\widehat{\otimes}H_2$ by $(a\otimes b)(x\otimes y) = ax\otimes by$, and the **spatial** (or **minimal**) tensor product $A\otimes_{\min}B$ is the completion in the operator norm on $B(H_1\widehat{\otimes}H_2)$, while the **maximal** tensor product $A\otimes_{\max}B$ is the completion in the largest $C^*$-norm on the algebraic tensor product. The two coincide when one of the factors is nuclear, and their theory — including the class of nuclear $C^*$-algebras and the uniqueness of the $C^*$-tensor product for amenable groups — is developed in the operator-algebraic articles of the next category of this Part.

---

## Summary

The **algebraic tensor product** $E\otimes F$ of two locally convex spaces carries two natural locally convex topologies. The **projective topology** is the finest making the canonical bilinear map continuous, and its completion $E\widehat{\otimes}_\pi F$ has the universal property that continuous bilinear maps on $E\times F$ correspond to continuous linear maps on $E\widehat{\otimes}_\pi F$; for normed spaces it is generated by the norm $\lVert u\rVert_\pi = \inf\{\sum_k\lVert x_k\rVert\lVert y_k\rVert : u = \sum_k x_k\otimes y_k\}$. The **injective topology** is the initial topology induced by the embedding of $E\otimes F$ into the space of bounded bilinear forms on $E'_\sigma\times F'_\sigma$ with the topology of uniform convergence on products of equicontinuous sets, and for normed spaces it is generated by $\lVert u\rVert_\varepsilon = \sup\{\lvert(\xi\otimes\eta)(u)\rvert\}$ over the unit balls of the duals. Always $\lVert\cdot\rVert_\varepsilon \leq \lVert\cdot\rVert_\pi$, and the comparison map $E\widehat{\otimes}_\pi F \to E\widehat{\otimes}_\varepsilon F$ is a topological isomorphism for all $F$ precisely when $E$ is **nuclear**.

The classical identifications are: $\mathbb{K}^m\otimes\mathbb{K}^n = M_{m,n}$ with the injective, Hilbert–Schmidt and projective norms equal to the operator, Hilbert–Schmidt and nuclear norms $\sigma_1$, $(\sum\sigma_i^2)^{1/2}$, $\sum\sigma_i$; $\ell^1\widehat{\otimes}_\pi E$ the summable $E$-valued sequences; $L^1\widehat{\otimes}_\pi L^1 \cong L^1$ of the product; $C(X)\widehat{\otimes}_\varepsilon C(Y) \cong C(X\times Y)$; the **Hilbert tensor product** $H_1\widehat{\otimes}H_2$, a Hilbert space with orthonormal basis the products of the orthonormal bases, whose completions in the injective, Hilbert–Schmidt and projective norms are the compact, Hilbert–Schmidt and trace-class operators; and, by nuclearity, $\mathcal{S}(\mathbb{R}^m)\widehat{\otimes}\mathcal{S}(\mathbb{R}^n) \cong \mathcal{S}(\mathbb{R}^{m+n})$. **Grothendieck's inequality** bounds the distortion between the two tensor norms on $\ell^2$ by the constant $K_G = \pi/(2\ln(1+\sqrt2))$, and Grothendieck's **problem of topologies** records that the completions of the projective and injective tensor products of Fréchet spaces may fail to be complete or Fréchet except in the nuclear case. For locally convex algebras the projective tensor product is a locally convex algebra, and in the operator-algebraic case the Hilbert tensor product of the representation spaces gives the spatial and maximal $C^*$-tensor products, whose theory belongs to the next category of this Part. **Trace duality** identifies the dual of the projective tensor product of Banach spaces with the bounded operators, $(E\widehat{\otimes}_\pi F)'\cong\mathcal{B}(E,F')$, so that in finite dimensions the nuclear and operator norms are mutually dual and the trace class $S_1(H)$ is a predual of $B(H)$. The operator-theoretic content of these identifications belongs to *Analysis on Linear Spaces* in Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E\otimes F$ | Algebraic tensor product |
| $E\widehat{\otimes}_\pi F$ | Completed projective tensor product |
| $E\widehat{\otimes}_\varepsilon F$ | Completed injective tensor product |
| $\lVert u\rVert_\pi$, $\lVert u\rVert_\varepsilon$ | Projective and injective norms |
| $\mathcal{B}(E'_\sigma\times F'_\sigma)$ | Bounded bilinear forms on the weak-star duals |
| $\mathcal{B}(E,F')$, $\langle x\otimes y,T\rangle = \langle y,Tx\rangle$ | Trace duality $(E\widehat{\otimes}_\pi F)'\cong\mathcal{B}(E,F')$ |
| $\sigma_i$, $\lVert A\rVert_{\mathrm{op}}$, $\lVert A\rVert_{\mathrm{HS}}$, $\lVert A\rVert_{\mathrm{nuc}}$ | Singular values and the three matrix norms |
| $H_1\widehat{\otimes}H_2$ | Hilbert tensor product |
| $S_1(H)$, $S_2(H)$, $S_\infty(H)$ | Trace class, Hilbert–Schmidt, compact operators |
| $K_G$ | Grothendieck's constant, $K_G = \pi/(2\ln(1+\sqrt2))$ |
| $A\widehat{\otimes}_\pi B$ | Projective tensor product of algebras |
| $A\otimes_{\min}B$, $A\otimes_{\max}B$ | Spatial (minimal) and maximal $C^*$-tensor products |



## Further Reading

- Alexandre Grothendieck, *Produits tensoriels topologiques et espaces nucléaires* (Memoirs of the American Mathematical Society, 1955), for the projective and injective topologies, the metric theory and the problem of topologies.
- Alexandre Grothendieck, "Résumé de la théorie métrique des produits tensoriels topologiques", *Boletim da Sociedade Matemática de São Paulo* **8** (1956), 1–79, for Grothendieck's inequality and the metric theory of tensor norms.
- Albrecht Pietsch, *Operator Ideals* (North-Holland, 1980), for the factorisation theory and the absolutely summing operators that Grothendieck's inequality generates.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for the tensor products of the spaces of analysis and the kernel theorem.
- Robert Schatten, *A Theory of Cross-Spaces* (Princeton University Press, 1950), for the trace class, the Hilbert–Schmidt class and the tensor products of Hilbert spaces.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Volume I (Academic Press, 1983), for the spatial and maximal $C^*$-tensor products and their elementary theory.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the tensor products of operator algebras and the nuclear case.
