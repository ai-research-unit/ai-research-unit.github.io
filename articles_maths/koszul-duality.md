
# __Koszul Duality__

## Introduction

A **quadratic algebra** is an algebra presented by generators and homogeneous quadratic relations, and its **Koszul dual** is the quadratic algebra obtained from the orthogonal complement of the space of relations. For the polynomial algebra the dual is the exterior algebra, and for the symmetric algebra of a vector space the dual is the exterior algebra on the dual space; these two are the original instances, and they are the reason the construction carries the names of symmetric and exterior in the first place. An algebra is **Koszul** when its Koszul complex is a resolution, equivalently when its cohomology is as small as possible: it is concentrated in a single degree in each internal degree.

The article is the eighth of the category. It follows *Deformation Quantization*, whose Hochschild cohomology it re-reads through the Koszul complex, and it precedes the homotopical layer that begins: a Koszul algebra is exactly a quadratic algebra whose Koszul dual is a quadratic algebra computing the Ext algebra, and the whole construction is most naturally phrased in the language of differential graded algebras, which is why the duality is developed here and its differential graded form immediately after. Its two structural theorems are the **Koszulity criterion** — the resolution property of the Koszul complex — and the **duality theorem** that for Koszul $A$ the derived category of bounded complexes of finitely generated graded $A$-modules is equivalent to the corresponding derived category over the Koszul dual. That equivalence is the **Koszul duality** proper, and it is the algebraic form of the more elaborate dualities of Part II.

The article is algebraic. The bimodule and Hochschild constructions it uses are those of *Separable Algebras*, *Hochschild Homology* and *Deformation Quantization*; the operadic formulation of Koszul duality, which makes sense for a general quadratic operad, is sketched with a forward pointer to the operads of the menu, and its homotopy-theoretic and model-categorical forms belong to Part II. No form theory, no distance and no topology is used.

Throughout, $k$ is a field, $V$ is a finite-dimensional $k$-vector space, $T(V)$ is the tensor algebra of *Tensor Powers and the Free Algebra*, and for a subspace $R \subseteq V\otimes_k V$ the quadratic algebra is

$$
A = A(V,R) = T(V)/(R), \qquad A_n = V^{\otimes n}\big/\sum_{i+j+2=n}V^{\otimes i}\otimes R\otimes V^{\otimes j} .
$$

A quadratic algebra is graded, $A = \bigoplus_{n\geq0}A_n$, with $A_0 = k$, $A_1 = V$, and generated in degree $1$ with relations in degree $2$. We write $A^!$ for the Koszul dual, $A^{\mathrm{op}}$ for the opposite algebra and $A^{\mathrm{e}} = A\otimes_k A^{\mathrm{op}}$ for the enveloping algebra.

## Quadratic Algebras and Their Duals

### Definition of the dual

**Definition.** Let $A = A(V,R)$ be a quadratic algebra. Its **Koszul dual** (or **quadratic dual**) is

$$
A^! = A(V^*,R^\perp), \qquad R^\perp = \{\xi \in V^*\otimes_k V^* : \xi(r) = 0 \ \text{for all } r \in R\},
$$

where $V^*\otimes_k V^*$ is identified with the dual of $V\otimes_k V$; equivalently, $A^! = T(V^*)/(R^\perp)$. The dual is a quadratic algebra with $A^!_1 = V^*$.

**Proposition.** The construction is involutive up to the natural identifications: $(A^!)^! \cong A$ when $V$ is finite-dimensional, and it reverses the inclusion of relation spaces, so that a quotient $A \to A'$ of quadratic algebras induces a map $A'^! \to A^!$ in the opposite direction.

*Proof.* The orthogonal complement is an inclusion-reversing involution on subspaces of a finite-dimensional space with a non-degenerate pairing, and $R^{\perp\perp} = R$; the identification $(V^*)^* \cong V$ then gives the first statement. The second is immediate because $R \subseteq R'$ implies $R'^\perp \subseteq R^\perp$. $\square$

**Remark.** The dual is defined by the quadratic relations alone and depends on the presentation. Two algebras that are isomorphic as algebras need not have isomorphic duals unless the isomorphism respects the grading and the space of generators; the dual is an invariant of the quadratic algebra, that is, of the pair $(V,R)$, not of the underlying algebra.

### The two model examples

**Example (the symmetric algebra and the exterior algebra).** Let $V$ be of dimension $n$ and let

$$
A = \operatorname{Sym}(V) = T(V)/(v\otimes w - w\otimes v)
$$

with $R = \Lambda^2V \subseteq V\otimes V$ spanned by the antisymmetric tensors. Then $R^\perp = S^2V^* \subseteq V^*\otimes V^*$ is the space of symmetric tensors, and

$$
A^! = T(V^*)/(S^2V^*) = \Lambda(V^*) ,
$$

the exterior algebra of the dual space. Conversely the dual of $\Lambda(V)$ is $\operatorname{Sym}(V^*)$. This pair is the source of the terminology: the Koszul dual of the symmetric algebra is the exterior algebra, and vice versa.

**Example (the tensor algebra and the trivial algebra).** With $R = 0$ the algebra is $T(V)$; then $R^\perp = V^*\otimes V^*$, so $A^! = T(V^*)/(V^*\otimes V^*) = k$. Conversely the dual of $k$ (presented with $R = V\otimes V$) is $T(V^*)$, so $k$ and $T(V)$ are Koszul dual. The duality therefore pairs the free algebra with the trivial algebra, which is the extreme case of the pairing between "no relations" and "all relations".

**Example (the quantum plane and the quantum exterior algebra).** Let $A = k_q[x,y] = T(V)/(q\,x\otimes y - y\otimes x)$ with $V = kx\oplus ky$ and $R = k(q\,x\otimes y - y\otimes x)$, so that the single relation is $yx = q\,xy$. Writing $x^*\otimes y^*$ for the tensor $x^*\otimes y^* \in V^*\otimes_k V^*$, the orthogonal complement is computed by $\xi(qx\otimes y - y\otimes x) = qB - C$ where $B, C$ are the coefficients of $x^*\otimes y^*$ and $y^*\otimes x^*$, so

$$
R^\perp = \operatorname{span}\bigl(x^*\otimes x^*,\ y^*\otimes y^*,\ x^*\otimes y^* + q\,y^*\otimes x^*\bigr), \qquad
A^! = T(V^*)\big/\bigl(x^{*2},\ y^{*2},\ x^*y^* + q\,y^*x^*\bigr) ,
$$

the **quantum exterior algebra** on two variables. Its Hilbert series is $1 + 2t + t^2$, because the relations give $x^{*2} = y^{*2} = 0$, $x^*y^* = -q\,y^*x^*$, and every word of length $\geq3$ reduces to zero; the identity $\mathrm{Hilb}_A(t)\mathrm{Hilb}_{A^!}(-t) = 1$ therefore holds, since $\mathrm{Hilb}_A(t) = (1-t)^{-2}$. The pair (quantum plane, quantum exterior algebra) is the $q$-deformation of the pair (symmetric algebra, exterior algebra), and the duality is the quadratic-algebraic shadow of the symmetry $q\leftrightarrow q^{-1}$ of *Quantum Groups*.

**Example (a truncated polynomial algebra).** Let $A = k[x]/(x^2)$, so $V = kx$ and $R = k(x\otimes x)$; then $R^\perp = 0$ in the one-dimensional space $V^*\otimes_k V^*$, and $A^! = T(V^*) = k[x^*]$ is the polynomial algebra in one variable. Both are Koszul. The Koszul complex of $A$ is

$$
\cdots \longrightarrow A \xrightarrow{\ \cdot x\ } A \xrightarrow{\ \cdot x\ } A \longrightarrow k \longrightarrow 0 ,
$$

with all differentials given up to sign by multiplication by $x$; its homology vanishes because $\ker(x) = (x) = \operatorname{im}(x)$ in $A$, and $H_0 = A/(x) = k$, so the complex is a free resolution of $k$. Dually the Koszul complex of $k[x^*]$ is the classical infinite resolution of $k$ by the powers of $x^*$. In this pair the resolution is infinite on one side and the Koszul dual is infinite-dimensional, showing that neither finiteness hypothesis is part of the definition.

### The Koszul complex

**Definition.** Let $A = A(V,R)$ and $A^! = A(V^*,R^\perp)$. The **Koszul complex** of $A$ is the complex of graded left $A$-modules

$$
K(A) : \quad \cdots \longrightarrow A\otimes_k (A^!_n)^* \xrightarrow{\ d_n\ } A\otimes_k (A^!_{n-1})^* \longrightarrow \cdots \longrightarrow A\otimes_k (A^!_0)^* \longrightarrow k \longrightarrow 0 ,
$$

where $(A^!_n)^*$ denotes the vector-space dual of the $n$-th graded piece of the Koszul dual, and the differential is the unique family of $A$-linear maps with

$$
d_n(1\otimes \xi) = \sum_{i} x_i\otimes (\xi \llcorner x^i) , \qquad x_i \in V = A_1 ,
$$

where $\{x_i\}$ is a basis of $V$, $\{x^i\}$ the dual basis of $V^*$ and $\llcorner$ is the contraction $\xi\mapsto \xi(x^i,\cdot)$ on the second tensor factor. Equivalently, $K(A)$ is the complex whose underlying graded module is $A\otimes_k (A^!)^*$ and whose differential is the derivative with respect to the generators.

**Proposition.** The Koszul complex is a complex, $d^2 = 0$, and $H_0(K(A)) = k$. The construction is natural in $A$.

*Proof.* The graded dual $(A^!_n)^*$ is the subspace of $V^{\otimes n}$ consisting of the tensors that annihilate $R^\perp$ in every pair of adjacent slots; this is the quadratic duality $(A^!_n)^*\cong A_n$. Hence $K(A)$ is $A\otimes_kA^*$ with a differential that is the transpose of the multiplication of $A$, and

$$
d^2(a\otimes\xi) = \sum_{i,j} ax_ix_j\otimes(\xi\llcorner x^i\llcorner x^j) ,
$$

the contractions being taken in the first two slots of $\xi$. The first two slots of the coefficient of $a$ therefore give the tensor $\sum_{i,j}\xi_{ij}\,x_i\otimes x_j \in V\otimes_kV$, where $\xi_{ij} = \xi(x^i,x^j,\cdot)$; because $\xi$ annihilates $R^\perp$ in the first two slots, that tensor is annihilated by every element of $R^\perp$ and hence lies in $(R^\perp)^\perp = R$. Multiplication $V\otimes_kV\to A$ kills $R$ by the definition $A = T(V)/(R)$, so $d^2 = 0$. For the symmetric algebra, where $R = \Lambda^2V$ and $\xi$ is alternating, this is the classical cancellation of the symmetric product $x_ix_j$ against the alternating factor $\xi(x^i,x^j,\cdot)$. The degree-$0$ statement is that $A\otimes_k(A^!_0)^* = A$ maps onto $k$ by the augmentation $A \to A/A_{\geq1} = k$. $\square$

**Definition.** $A$ is **Koszul** if $K(A)$ is a resolution of the trivial module $k$ by free (or, in the graded sense, graded-free) $A$-modules; equivalently $H_n(K(A)) = 0$ for $n \geq 1$.

Since $K(A)$ is a complex of free $A$-modules with $K(A)_n$ generated in internal degree $n$, the condition that it be a resolution is a condition on the growth of the Betti numbers of $k$: it says that the minimal free resolution of $k$ over $A$ has generators exactly in internal degree equal to homological degree. This is the precise meaning of "the cohomology is concentrated in one degree per internal degree".

## Koszulity and the Resolution Criterion

### The criterion

**Theorem (Koszulity criterion, standard).** Let $A = A(V,R)$ be a quadratic algebra. Then the following are equivalent:

1. $A$ is Koszul;
2. $\operatorname{Tor}^A_{i,j}(k,k) = 0$ for $i \neq j$, where the second index is the internal degree;
3. $\operatorname{Ext}^{i,j}_A(k,k) = 0$ for $i \neq j$;
4. the Koszul dual $A^!$ is Koszul, and then $A^!$ is the algebra $\bigoplus_i\operatorname{Ext}^{i,i}_A(k,k)$ with the Yoneda product, up to the identification of $A^!_i$ with $\operatorname{Ext}^{i,i}_A(k,k)$.

*Proof (outline).* The Koszul complex has, by construction, one generator in each bidegree $(i,i)$; it is a resolution exactly when no other bidegrees occur in a minimal resolution, which is the condition on $\operatorname{Tor}$ in degree $i\neq j$. The equivalence of the Tor and Ext statements is the duality between the two, valid because $A$ is graded with finite-dimensional graded pieces and $A_0 = k$. The last statement is the computation of the Ext algebra from the Koszul complex: since $K(A)$ is a complex of free modules, applying $\operatorname{Hom}_A(-,k)$ computes $\operatorname{Ext}^\bullet_A(k,k)$, and when $K(A)$ is a resolution the resulting complex has cohomology in each bidegree $(i,i)$ equal to $(A^!_i)^*$, so that $A^! \cong \operatorname{Ext}^{\bullet,\bullet}_A(k,k)$ as a graded algebra. Applying the same statement to $A^!$ gives the mutual character of Koszulity. $\square$

**Corollary.** If $A$ is Koszul then its Hilbert series $\mathrm{Hilb}_A(t) = \sum_n\dim_k(A_n)t^n$ and the Hilbert series of $A^!$ satisfy

$$
\mathrm{Hilb}_A(t)\,\mathrm{Hilb}_{A^!}(-t) = 1 .
$$

*Proof.* The Euler characteristic of the Koszul complex, which is a resolution of $k$ when $A$ is Koszul, gives $\sum_n(-1)^n\dim_k(A\otimes_k(A^!_n)^*)\,t^n = \dim_k k = 1$ if the internal degree is tracked; substituting the Hilbert series evaluates the alternating sum. $\square$

**Example.** For $A = \operatorname{Sym}(V)$ with $\dim V = n$, $\mathrm{Hilb}_A(t) = (1-t)^{-n}$ and $\mathrm{Hilb}_{A^!}(t) = (1+t)^n$, so $\mathrm{Hilb}_A(t)\mathrm{Hilb}_{A^!}(-t) = (1-t)^{-n}(1-t)^n = 1$. For the quantum plane and its dual of the preceding example the same identity holds, with $(1-t)^{-2}$ and $(1-t)^{2}$. For $A = k[x]/(x^2)$ it reads $(1+t)\cdot(1+t)^{-1} = 1$, again true, and $A^! = k[x]$ in this case. The identity is a necessary condition for Koszulity and is the quickest numerical test; it is not sufficient in general, and the full criterion is the vanishing of $\operatorname{Tor}$ in the off-diagonal bidegrees.

### Sufficient conditions and examples

**Theorem (standard).** The following quadratic algebras are Koszul:

1. the symmetric algebra $\operatorname{Sym}(V)$ with $\operatorname{Sym}(V)^! = \Lambda(V^*)$, and the exterior algebra $\Lambda(V)$ with $\Lambda(V)^! = \operatorname{Sym}(V^*)$, for every finite-dimensional $V$;
2. the free algebra $T(V)$ with $T(V)^! = k$, and $k$ with $k^! = T(V^*)$;
3. the quantum affine space $k_q[x_1,\dots,x_n]$ with relations $x_jx_i = q_{ij}x_ix_j$ for $q$ not a root of unity, whose Koszul dual is the quantum exterior algebra on the dual generators; for $n = 2$ this is the pair computed above;
4. every algebra that admits a **PBW basis** with respect to a degree-compatible monomial order and whose leading monomials are quadratic, in the sense that the monomials not divisible by a leading monomial of a relation form a basis: such algebras are Koszul, and the family includes the quantum affine spaces of item 3 and the $q$-Weyl algebras;
5. the **skew group ring** $A\# G$ of a Koszul algebra $A$ by a finite group $G$ acting by graded algebra automorphisms preserving the space of generators, in the sense of the crossed products of *Crossed Products*.

**Example (Koszul duality of the symmetric and the exterior algebra).** The algebra $A = \operatorname{Sym}(V)$ and its dual $\Lambda(V^*)$ form the model pair. Its Koszul complex is the classical Koszul complex of the polynomial algebra,

$$
0 \to A\otimes_k \Lambda^n(V) \to A\otimes_k\Lambda^{n-1}(V)\to\cdots\to A\otimes_k\Lambda^1(V) \to A \to k \to 0,
$$

with $n = \dim V$, and the exactness of this complex — the statement that the Koszul complex of a regular sequence is a resolution, the algebraic content of the theorem that the polynomial algebra is Cohen–Macaulay — is exactly the Koszulity of $\operatorname{Sym}(V)$. This is the origin of the name.

**Example (a non-Koszul quadratic algebra).** The algebra $A = k[x,y]/(xy)$ has $\mathrm{Hilb}_A(t) = (1+t)/(1-t)$, while its quadratic dual has $\dim_k A^!_2 = 4 - \dim_k R^\perp$ with $\dim_k R^\perp = 3$, so $\dim_kA^!_2 = 1$; the required identity would force $\dim_kA^!_2 = 2$, so the numerical test fails and $A$ is not Koszul. The algebra is a monomial quadratic algebra whose Koszulity is decided by the criterion of Backelin and Fröberg for monomial algebras, and the failure reflects the presence of the zerodivisor $x$: the algebra is the quotient of the polynomial algebra by a non-regular element.

## Koszul Duality as an Equivalence of Derived Categories

### The derived category statement

**Definition.** For a graded $k$-algebra $A$ with $A_n$ finite-dimensional and $A_0 = k$, let $D^{\mathrm{b}}(\operatorname{grmod}A)$ be the bounded derived category of finitely generated graded left $A$-modules, the algebraic derived category introduced in *Homological Algebra*. The **Koszul duality** statement relates this category to the corresponding one for $A^!$.

**Theorem (BGG–Koszul duality, standard).** Let $A$ be a Koszul algebra with Koszul dual $A^!$. Then there is an equivalence of triangulated categories

$$
D^{\mathrm{b}}(\operatorname{grmod}A) \;\simeq\; D^{\mathrm{b}}(\operatorname{grmod}A^!)^{\mathrm{op}}
$$

implemented by the functors $\operatorname{RHom}_A(-,k)$ and $\operatorname{RHom}_{A^!}(-,-,k)$; equivalently, the Koszul complex $K(A)$ is a tilting object of the derived category of graded $A$-modules, and its endomorphism algebra is $A^!$. Under the equivalence the free module $A$ corresponds to $k$ (with a degree shift) and the simple module $k$ corresponds to $A^!$.

*Proof (outline).* The Koszul complex $K(A)$ is a compact object of $D^{\mathrm{b}}(\operatorname{grmod}A)$ when $A$ is Koszul, and the natural map $A^! \to \operatorname{End}_{D(A)}(K(A))^{\mathrm{op}}$ is an isomorphism: this is the content of the resolution criterion, read in the derived category. Every finitely generated graded $A$-module has a finite resolution by direct sums of the $A$-modules underlying the terms of $K(A)$, because $K(A)$ generates the derived category as $k$ does; the general tilting theory then states that $\operatorname{RHom}(K(A),-)$ is an equivalence onto the derived category of modules over $\operatorname{End}(K(A))^{\mathrm{op}} = A^!$, with the opposite handedness recorded by the $\mathrm{op}$ in the statement. $\square$

**Corollary.** For a Koszul algebra the algebra $A$ is determined up to isomorphism by $A^!$ and conversely; in particular Koszul duality is an involution on the class of Koszul algebras.

**Example.** For $A = \operatorname{Sym}(V)$ and $A^! = \Lambda(V^*)$, the duality says that graded modules over the polynomial algebra are equivalent to graded modules over the exterior algebra, with the roles of projective and injective objects exchanged. The **Bernstein–Gelfand–Gelfand correspondence** is the geometric case: for a vector space $V$ the equivalence relates coherent sheaves on the projective space $\mathbb{P}(V)$ to finitely generated graded modules over the exterior algebra, the singularity category of the polynomial ring and the stable module category of the exterior algebra being equivalent. The projective space and the corresponding geometric categories belong to Part II, where the geometry is available; only the algebraic statement is recorded here.

### The operadic and homological formulations

**Definition.** A **quadratic operad** $\mathcal{O}$ is an operad generated by operations in arity $2$ with relations in arity $3$ quadratic in the generators, so that $\mathcal{O}$ has a **Koszul dual** operad $\mathcal{O}^!$ defined by the orthogonal complement of the space of relations with respect to the natural pairing on the operation spaces. An operad is **Koszul** if its Koszul complex is a resolution.

**Theorem (standard).** The associative operad $\mathcal{A}ss$ and the operad of (graded) commutative algebras $\mathcal{C}om$ are Koszul dual, and the operad $\mathcal{L}ie$ is Koszul and self-dual up to the suspension $\mathcal{L}ie^! = \mathcal{C}om$ with a degree shift: exactly, $\mathcal{A}ss^! = \mathcal{A}ss$ up to a shift and $\mathcal{C}om^! = \mathcal{L}ie$, which is the operadic form of the duality between $\operatorname{Sym}(V)$ and $\Lambda(V)$, between the commutative and the Lie structures. The operadic Koszulity is verified by the same criterion: the Koszul complex of a quadratic operad is a resolution exactly when the operad's homology is concentrated in the expected bidegrees. The theory of operads is developed in *Operads*, and the homotopy-coherent generalisations — the $A_\infty$- and $L_\infty$-operads, which are the Koszul resolutions of the associative and the Lie operads — are the subject in the menu.

**Theorem (standard).** Let $A$ be a Koszul algebra with Koszul dual $A^!$. Then the Hochschild cohomology of $A$ is computed by a complex built from the Koszul resolution, and there are duality statements relating the Hochschild theories of $A$ and of $A^!$ with a degree shift: for a Koszul algebra the Hochschild cohomology $HH^\bullet(A,A)$ is the $E_2$-page of a spectral sequence converging to the Hochschild cohomology of $A^!$, and in the graded-complete setting the Hochschild homology of $A$ is dual to the Hochschild cohomology of $A^!$ with a shift of degree,

$$
HH_i(A,A)^* \;\cong\; HH^{i}(A^!,A^!) \qquad \text{(graded-complete case)},
$$

so that the Hochschild theories of a Koszul algebra and of its dual determine one another. The duality is the algebraic prototype of the duality between the homology of a space and the cohomology of a ring of functions on it; the topological reading belongs to Part II, and the transfer of the Calabi–Yau condition along Koszul duality is not covered here.

## Koszul Duality and the Symmetric and Exterior Algebras of this Part

The duality of the article is the algebraic statement that completes the pairing of the two symmetric-side and antisymmetric-side constructions of this Part. The symmetric algebra $\operatorname{Sym}(V)$ and the exterior algebra $\Lambda(V)$ are Koszul dual, and the same is true of the symmetric and divided power algebras in the graded-complete setting. This is the precise sense in which the symmetric and the antisymmetric constructions are dual to each other at the level of algebras, and it explains why the two families run through the corpus in parallel: the polynomial algebra and the Grassmann algebra are not merely analogous, they are exchanged by a duality.

**Proposition.** Let $V$ be finite-dimensional. Then:

1. $\operatorname{Sym}(V)$ is Koszul with $\operatorname{Sym}(V)^! = \Lambda(V^*)$;
2. $\Lambda(V)$ is Koszul with $\Lambda(V)^! = \operatorname{Sym}(V^*)$;
3. the divided power algebra $\Gamma(V)$ is Koszul with $\Gamma(V)^! = \Lambda(V^*)$ in the graded-complete setting, the divided powers being the graded-complete dual of the symmetric powers; the two algebras $\operatorname{Sym}(V)$ and $\Gamma(V)$ consequently share the same Koszul dual, which is the algebraic statement of the mutual duality of the symmetric and divided power algebras.

*Proof.* Statements 1 and 2 are the model examples computed above. Statement 3 follows from the Hilbert-series identity on the graded pieces, $\dim_k\Gamma_n(V) = \dim_kS^n(V^*)$, together with the resolution criterion; it is the statement that the symmetric and divided power algebras are the two graded-complete forms of the Koszul resolution and have the exterior algebra as their common dual. $\square$

## Summary

A **quadratic algebra** is $A = A(V,R) = T(V)/(R)$ with $R \subseteq V\otimes_k V$ homogeneous of degree $2$, and its **Koszul dual** is $A^! = T(V^*)/(R^\perp)$, the quadratic algebra determined by the orthogonal complement of the relations; the construction is an inclusion-reversing involution on quadratic algebras, so $(A^!)^! \cong A$. The model examples are $\operatorname{Sym}(V)^! = \Lambda(V^*)$ and $\Lambda(V)^! = \operatorname{Sym}(V^*)$, together with $T(V)^! = k$ and $k^! = T(V^*)$; the Koszul dual of the quantum plane is the quantum exterior algebra with relations $x^{*2} = y^{*2} = 0$ and $x^*y^* = -q\,y^*x^*$. The **Koszul complex** $K(A)$ is the complex of graded free $A$-modules with $K(A)_n = A\otimes_k(A^!_n)^*$ and differential the derivative with respect to the generators, and $A$ is **Koszul** when $K(A)$ is a resolution of the trivial module, equivalently when $\operatorname{Ext}^{i,j}_A(k,k) = 0$ for $i \neq j$; then $A^! \cong \operatorname{Ext}^{\bullet,\bullet}_A(k,k)$ with the Yoneda product, $A^!$ is again Koszul, and the Hilbert series satisfy $\mathrm{Hilb}_A(t)\mathrm{Hilb}_{A^!}(-t) = 1$.

The **Koszul duality theorem** states that for Koszul $A$ the bounded derived category of finitely generated graded $A$-modules is equivalent to that of $A^!$ with the opposite variance, realised by $\operatorname{RHom}_A(-,k)$ and by the tilting object $K(A)$ whose endomorphism algebra is $A^!$; the algebraic cases are the BGG correspondence and the exchange of $\operatorname{Sym}(V)$ with $\Lambda(V^*)$, and the geometric statements — projective spaces, singularity categories and coherent sheaves — belong to Part II. The operadic version pairs the operads $\mathcal{C}om$ and $\mathcal{L}ie$, up to a shift, identifies $\mathcal{A}ss$ with its dual, and the homotopy-coherent form of the resulting resolutions is not covered here. The duality completes the pairing of the symmetric side and the antisymmetric side of this Part: the symmetric algebra and the exterior algebra, and their divided-power and symmetric-power forms, are exchanged by Koszul duality, and the Hochschild theories of an algebra and of its Koszul dual are related by a Poincaré-type duality.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $V$ | field, finite-dimensional vector space |
| $T(V)$ | tensor algebra, free algebra on $V$ |
| $A(V,R) = T(V)/(R)$ | quadratic algebra with relations $R \subseteq V\otimes_k V$ |
| $A_n$ | $n$-th graded piece, $A_0 = k$, $A_1 = V$ |
| $A^!$ | Koszul (quadratic) dual, $A^! = T(V^*)/(R^\perp)$ |
| $R^\perp$ | orthogonal complement of $R$ in $V^*\otimes_k V^*$ |
| $K(A)$, $d_n$ | Koszul complex and its differential |
| Koszul | $K(A)$ is a resolution of $k$ |
| $\operatorname{Tor}^A_{i,j}(k,k)$, $\operatorname{Ext}^{i,j}_A(k,k)$ | bigraded Tor and Ext, second index internal degree |
| $\mathrm{Hilb}_A(t)$ | Hilbert series; $\mathrm{Hilb}_A(t)\mathrm{Hilb}_{A^!}(-t) = 1$ |
| $\operatorname{grmod}A$, $D^{\mathrm{b}}$ | graded modules, bounded derived category |
| $\mathcal{O}^!$ | Koszul dual of a quadratic operad |
| $\mathcal{A}ss$, $\mathcal{C}om$, $\mathcal{L}ie$ | associative, commutative, Lie operads |
| $\operatorname{Sym}(V)$, $\Lambda(V)$, $\Gamma(V)$ | symmetric, exterior, divided power algebras |
| $k_q[x,y]$ | quantum plane, $yx = qxy$ |





## Further Reading

- Alexander Beilinson, Victor Ginzburg and Wolfgang Soergel, "Koszul duality patterns in representation theory", *Journal of the American Mathematical Society* **9** (1996), 473–527, for the Koszulity criterion, the derived equivalence and the BGG correspondence.
- Stewart B. Priddy, "Koszul resolutions", *Transactions of the American Mathematical Society* **152** (1970), 39–60, for the original definition and the resolution criterion.
- Victor Ginzburg and Mikhail Kapranov, "Koszul duality for operads", *Duke Mathematical Journal* **76** (1994), 203–272, for the operadic formulation.
- Alexander Polishchuk and Leonid Positselski, *Quadratic Algebras* (American Mathematical Society, 2005), for a systematic treatment with the Hilbert-series and derived criteria.
- Joseph Bernstein, Israel Gelfand and Sergei Gelfand, "Algebraic bundles over $\mathbb{P}^n$ and problems of linear algebra", *Functional Analysis and its Applications* **12** (1978), 212–214, for the BGG correspondence.
- Ralph Fröberg, "Determination of a class of Poincaré series", *Mathematica Scandinavica* **37** (1975), for the Hilbert-series criterion for Koszulity.
