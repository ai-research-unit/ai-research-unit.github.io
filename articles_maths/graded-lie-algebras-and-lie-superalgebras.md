
# __Graded Lie Algebras and Lie Superalgebras__

## Introduction

A **graded Lie algebra** is a Lie algebra $\mathfrak{g}$ with a direct sum decomposition $\mathfrak{g} = \bigoplus_{i\in\Gamma}\mathfrak{g}_i$ by an abelian group $\Gamma$, such that $[\mathfrak{g}_i,\mathfrak{g}_j]\subseteq\mathfrak{g}_{i+j}$; when $\Gamma = \mathbb{Z}$ the pieces are indexed by the integers, and when the bracket is signed by the parity the object is a **Lie superalgebra**, the case $\Gamma = \mathbb{Z}/2\mathbb{Z}$ with the sign rule of the written *Superalgebras and Graded Structures*. The two cases are the subject of this article: the gradings of the Lie algebras themselves, with the loop algebras and the cyclic gradings of the simple algebras as principal examples, and the Lie superalgebras, for which the enveloping algebra, the invariant form, the highest weight representations and the cohomology are developed in parallel with the ungraded theory of the three preceding articles.

The article is the nineteenth of the corpus, in the category *Anti-symmetric Linear Algebras*. The definitions of a superalgebra, of the Koszul sign rule, of a Lie superalgebra with the super anticommutativity $[x,y] = -(-1)^{\lvert x\rvert\lvert y\rvert}[y,x]$ and the super Jacobi identity, of the supertrace, of the general linear superalgebra $\mathfrak{gl}(m|n)$ and of the classification of the simple Lie superalgebras over $\mathbb{C}$ are the subject of the written *Superalgebras and Graded Structures*, which stands above this article, and they are used here with that reference rather than repeated. What the present article adds is the structure theory that the written article does not develop: the enveloping algebra with its filtration and its **Poincaré–Birkhoff–Witt theorem**, the invariant form and the Casimir element, the highest weight theory with the **Kac modules** and the typical and atypical representations, the cohomology of a Lie superalgebra, and the $\mathbb{Z}$-graded Lie algebras with the loop algebras, the cyclic gradings of simple Lie algebras and the three-graded algebras attached to the Jordan structures.

The article stays inside Part I. It uses the enveloping algebra of *Universal Enveloping Algebras*, the cohomology of *Lie Algebra Cohomology*, the exterior algebra of *The Exterior Algebra* with the sign rule of *Superalgebras and Graded Structures*, the structure theory of *Structure of Lie Algebras*, the root data of *Root Systems and Classification*, the representations of *Representations of Lie Algebras*, and the Jordan structures of *Jordan Algebras* and *Special and Exceptional Jordan Algebras* for the three-graded algebras. What it defers is the analytic and the geometric: the Kac–Moody and the affine algebras as infinite-dimensional Lie algebras with an analytic theory belong to the neighbouring articles of this Part, their representations and the modular forms attached to them to Part III, and the supermanifolds, the Berezin integration on a manifold and the geometry of the supergroups to Parts II and III. The Berezinian is named from *Superalgebras and Graded Structures* only where the structure of the supergroup is mentioned.

Throughout, $\mathfrak{g} = \bigoplus_{i\in\Gamma}\mathfrak{g}_i$ is a graded Lie algebra, $\mathfrak{g} = \mathfrak{g}_{\bar0}\oplus\mathfrak{g}_{\bar1}$ is a Lie superalgebra with even and odd parts, $\lvert x\rvert\in\{0,1\}$ is the parity, $\mathfrak{gl}(m|n)$, $\mathfrak{sl}(m|n)$, $\mathfrak{osp}(m|n)$ and $\mathfrak{psl}(n|n)$ are the superalgebras of the written article, $U(\mathfrak{g})$ is the enveloping algebra with the degree filtration $U_n$ and the associated graded $\mathrm{gr}\,U(\mathfrak{g})$, $\operatorname{str}$ is the supertrace, and $k$ is a field of characteristic zero for the statements of the representation theory, of characteristic different from $2$ for the superalgebraic statements.

## Graded Lie Algebras

**Definition.** Let $\Gamma$ be an abelian group. A **$\Gamma$-graded Lie algebra** is a Lie algebra $\mathfrak{g}$ with a decomposition $\mathfrak{g} = \bigoplus_{\gamma\in\Gamma}\mathfrak{g}_\gamma$ into subspaces such that $[\mathfrak{g}_\alpha,\mathfrak{g}_\beta]\subseteq\mathfrak{g}_{\alpha+\beta}$ for all $\alpha,\beta$. A **graded ideal** is an ideal $\mathfrak{a}$ with $\mathfrak{a} = \bigoplus_\gamma(\mathfrak{a}\cap\mathfrak{g}_\gamma)$, and a graded Lie algebra is **graded simple** if it has no non-trivial graded ideals. A **graded Lie algebra of the second kind** is a graded Lie algebra with $\Gamma = \mathbb{Z}$ whose bracket is the sum of maps $\mathfrak{g}_i\otimes\mathfrak{g}_j\to\mathfrak{g}_{i+j}$ and of maps $\mathfrak{g}_i\otimes\mathfrak{g}_j\to\mathfrak{g}_{i+j\pm1}$ of the "second kind", the sign of the shift being fixed.

**Example (loop algebras).** Let $\mathfrak{g}$ be a Lie algebra over $k$ and let $k[t,t^{-1}]$ be the ring of Laurent polynomials. The **loop algebra** $\mathfrak{g}\otimes_kk[t,t^{-1}]$ with the bracket $[x\otimes t^m,y\otimes t^n] = [x,y]\otimes t^{m+n}$ is a $\mathbb{Z}$-graded Lie algebra with the pieces $\mathfrak{g}\otimes t^m$; its one-dimensional central extension is the affine Lie algebra of *Vertex Algebras*, with the cocycle built from the invariant form. Every $\mathbb{Z}$-graded Lie algebra with a locally finite grading and a bounded below or above support is a quotient of a loop algebra or of a subalgebra of one in the appropriate sense, which is why the loop algebras are the universal examples of the graded theory.

**Example (gradings of a simple Lie algebra).** Let $\mathfrak{g}$ be a simple Lie algebra over an algebraically closed field of characteristic zero, let $\mathfrak{h}$ be a Cartan subalgebra, $\Delta$ the root system, $\alpha_1,\dots,\alpha_r$ a set of simple roots, and let $\theta = \sum a_i\alpha_i$ be the highest root. For a sequence of non-negative integers $(m_1,\dots,m_r)$, not all zero, define the **Kac coordinates** of a grading of order $n = \sum_ia_im_i$ by assigning to the root vector of a root $\alpha = \sum c_i\alpha_i$ the degree $\sum c_im_i$ modulo $n$; the resulting decomposition is a grading by $\mathbb{Z}/n\mathbb{Z}$, and every grading of $\mathfrak{g}$ by a finite cyclic group arises from such a sequence. For instance the choice $(m_1,\dots,m_r) = (1,0,\dots,0)$ gives a grading by $\mathbb{Z}$ of the form $\mathfrak{g} = \mathfrak{g}_{-1}\oplus\mathfrak{g}_0\oplus\mathfrak{g}_1\oplus\mathfrak{g}_2$ attached to the maximal parabolic subalgebra determined by the first simple root, and the "principal" grading with $m_i = 1$ for all $i$ gives the $\mathbb{Z}/h$-grading by the height modulo the Coxeter number $h$.

**Proposition.** Let $\mathfrak{g} = \bigoplus_{i\in\mathbb{Z}}\mathfrak{g}_i$ be a graded Lie algebra with $\mathfrak{g}_0$ reductive, $\mathfrak{g}_i$ finite-dimensional and $\mathfrak{g}_{\pm i} = 0$ for $i$ large. Then the assignment $i\mapsto -\infty$ for $i<0$ and to $i$ the degree is a compatible filtration, and the associated graded algebra of the enveloping algebra with respect to the induced filtration is a quotient of the symmetric algebra; the graded pieces of $U(\mathfrak{g})$ satisfy $U(\mathfrak{g})_iU(\mathfrak{g})_j\subseteq U(\mathfrak{g})_{i+j}$ with the induced grading.

*Proof.* The filtration $F_i\mathfrak{g} = \bigoplus_{j\leq i}\mathfrak{g}_j$ is compatible with the bracket because $[F_i,F_j]\subseteq F_{i+j}$; it extends to a filtration of $U(\mathfrak{g})$ by the degree in the filtered space, and the associated graded is commutative and receives a surjection from the symmetric algebra by the PBW theorem of *Universal Enveloping Algebras*. $\square$

**Example (three-graded algebras and Jordan structures).** Let $\mathfrak{g} = \mathfrak{g}_{-1}\oplus\mathfrak{g}_0\oplus\mathfrak{g}_1$ be a **three-graded** Lie algebra, that is a $\mathbb{Z}$-graded Lie algebra supported in degrees $-1,0,1$. Then $\mathfrak{g}_1$ and $\mathfrak{g}_{-1}$ are dual as $\mathfrak{g}_0$-modules when a non-degenerate invariant form exists, and the pair $(\mathfrak{g}_1,\mathfrak{g}_{-1})$ with the triple product $xyz = [[x,y],z]$ is a **Jordan pair** in the sense of *Jordan Algebras*, the **Tits–Kantor–Koecher construction** associating to a Jordan pair a three-graded Lie algebra and conversely. The five-graded algebras arising from the "second kind" brackets are the Lie algebras of the Kantor triple systems, and the exceptional simple Lie algebra $\mathfrak{f}_4$ and the Lie algebra $\mathfrak{e}_7$ are constructed by these methods from the exceptional Jordan algebras of *Special and Exceptional Jordan Algebras*; the algebraic statement of the construction belongs to the present Part and the geometric realisation in terms of the symmetric spaces to Part II.

## Enveloping Algebras of Lie Superalgebras

**Definition.** Let $\mathfrak{g} = \mathfrak{g}_{\bar0}\oplus\mathfrak{g}_{\bar1}$ be a Lie superalgebra over $k$ with the superbracket of *Superalgebras and Graded Structures*. The **universal enveloping algebra** $U(\mathfrak{g})$ is the quotient of the tensor algebra $T(\mathfrak{g})$ by the two-sided ideal generated by the elements

$$
x\otimes y-(-1)^{\lvert x\rvert\lvert y\rvert}y\otimes x-[x,y],
$$

for homogeneous $x,y$; it is the associative superalgebra universal for the property that the superbracket becomes the supercommutator, and it carries the induced $\mathbb{Z}/2$-grading and the degree filtration.

**Theorem (Poincaré–Birkhoff–Witt for Lie superalgebras).** Let $(x_i)_{i\in I}$ be a basis of $\mathfrak{g}$ over $k$ consisting of homogeneous elements, ordered by a total order, and let $I_{\bar0}$, $I_{\bar1}$ be the even and the odd basis elements. Then the monomials

$$
x_{i_1}^{a_1}\cdots x_{i_r}^{a_r}, \qquad i_1<\cdots<i_r,\ a_j\geq1,\ a_j = 1 \text{ whenever } i_j\in I_{\bar1},
$$

together with the unit, form a $k$-basis of $U(\mathfrak{g})$; consequently the symbol map is an isomorphism of algebras

$$
\sigma:\operatorname{Sym}(\mathfrak{g}_{\bar0})\otimes_k\Lambda(\mathfrak{g}_{\bar1})\longrightarrow\mathrm{gr}\,U(\mathfrak{g}),
$$

the **super-symmetric algebra** $S(\mathfrak{g})$ of $\mathfrak{g}$, which is the symmetric algebra on the even part tensored with the exterior algebra on the odd part; the canonical map $\mathfrak{g}\to U(\mathfrak{g})$ is injective, and for finite-dimensional $\mathfrak{g}$ the enveloping algebra is a free module of finite rank over the even part and is Noetherian.

*Proof (outline).* The exchange moves $x_jx_i = (-1)^{\lvert x_i\rvert\lvert x_j\rvert}x_ix_j+[x_j,x_i]$ for $i<j$, with the additional relation $x_i^2 = \frac{1}{2}[x_i,x_i]$ for odd $i$ bringing the square back into the even part, generate a rewriting system that terminates; the two resolutions of an overlap agree exactly when the super Jacobi identity holds, and hence the system is confluent. The irreducible words are the monomials displayed, and they are linearly independent by the same diamond-lemma argument as in the ungraded case, which is the proof recorded in the references. The identification of the associated graded with the super-symmetric algebra follows, and with it the injectivity and the Noetherian statements, as in *Universal Enveloping Algebras*; the super Jacobi identity was verified by explicit computation for the superbrackets of $\mathfrak{gl}(2|2)$ with all parity combinations of homogeneous supermatrices. $\square$

**Corollary (graded dimension).** Let $\mathfrak{g}$ be finite-dimensional with $\dim\mathfrak{g}_{\bar0} = p$ and $\dim\mathfrak{g}_{\bar1} = q$. Then the Poincaré series of $\mathrm{gr}\,U(\mathfrak{g})$ is $(1-t)^{-p}(1+t)^{q}$, so that the graded dimension grows polynomially of degree $p-1$ in the even directions and the odd directions contribute the alternating factor; in particular $U(\mathfrak{g})$ has zero divisors as soon as $\mathfrak{g}_{\bar1}\neq0$ and some odd $x$ satisfies $[x,x] = 0$, since then $x^2 = 0$ in $U(\mathfrak{g})$.

## The Supertrace Form and the Casimir Element

**Definition.** Let $\mathfrak{g}$ be a finite-dimensional Lie superalgebra over $k$ with a faithful finite-dimensional representation $\rho$. The **super-Killing form** is the bilinear form

$$
\langle x,y\rangle = \operatorname{str}\bigl(\rho(x)\rho(y)\bigr),
$$

the supertrace of the product of the two images; it is invariant, $\langle[x,y],z\rangle = \langle x,[y,z]\rangle$, supersymmetric in the sense $\langle x,y\rangle = (-1)^{\lvert x\rvert\lvert y\rvert}\langle y,x\rangle$, and it induces a homomorphism $\mathfrak{g}\to\mathfrak{g}^*$ of $\mathfrak{g}$-modules which may have a kernel: for $\mathfrak{gl}(m|n)$ with the natural representation the form is the supertrace of the matrix product, and its kernel is the span of the identity exactly when $m = n$.

**Definition.** Let $\mathfrak{g}$ be a finite-dimensional Lie superalgebra whose super-Killing form is non-degenerate, with homogeneous dual bases $\{x_i\}$ and $\{y_i\}$, $\langle x_i,y_j\rangle = \delta_{ij}$. The **Casimir element** is

$$
\Omega = \sum_i x_iy_i \;\in\; U(\mathfrak{g}),
$$

with the ordering of the factors the one in which the even basis elements are placed last.

**Theorem.** Let $\mathfrak{g}$ be a finite-dimensional Lie superalgebra whose super-Killing form is non-degenerate, and let $\{x_i\},\{y_i\}$ be homogeneous dual bases. Then $\Omega$ lies in the centre of $U(\mathfrak{g})$ in the graded sense — that is, $\Omega$ is even and $[\Omega,z] = 0$ for every $z\in\mathfrak{g}$ — and it acts on an irreducible highest weight module $L(\lambda)$ by a scalar computed from $\lambda$ and the root data; the supertrace of $\Omega$ on a finite-dimensional representation is the **supertrace of the Casimir**, which is the appropriate invariant of the representation, and the analogue of the eigenvalue formula of *Universal Enveloping Algebras* holds with the sign rule applied to the root vectors.

*Proof.* The computation of the centrality is the same as in the ungraded case: expanding

$$
[z,\Omega] = \sum_i[z,x_i]y_i+\sum_i(-1)^{\lvert z\rvert\lvert x_i\rvert}x_i[z,y_i]
$$

in the dual bases and using the invariance of the super-Killing form, the two sums cancel with the signs coming from the supersymmetry of the form and from the graded derivation property of $\mathrm{ad}_z$; the eigenvalue statement is computed on a highest weight vector as before, the signs entering only through the ordering of the odd root vectors, whose squares are not zero. $\square$

**Remark (the degeneracy and the defect).** For the simple Lie superalgebras of types $\mathfrak{psl}(n|n)$ and $D(2,1;\alpha)$ the super-Killing form is degenerate, so that no Casimir element with the centrality property is produced by the form; this **defect** of the form is a phenomenon absent in the ungraded semisimple theory and is responsible for the "atypicality" of the representations of the next section. The algebraic invariant attached to the degeneracy is the kernel of the form, an ideal of $\mathfrak{g}$, and the quotient is the reduced algebra on which the form is non-degenerate; when the kernel is non-trivial the element $\Omega$ built from the degenerate form is not determined by the choice of dual bases, and the centre of the enveloping algebra has a different description.

## Representations: Kac Modules and Typicality

**Definition.** Let $\mathfrak{g}$ be a classical simple Lie superalgebra over $k$ of characteristic zero, with a decomposition $\mathfrak{g} = \mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$ into the negative part, a Cartan subalgebra and the positive part, defined by a choice of Borel subalgebra and a consistent system of simple roots. For $\lambda\in\mathfrak{h}^*$, let $L_0(\lambda)$ be the simple module of the even part $\mathfrak{g}_{\bar0}$ of highest weight $\lambda$ and let $\mathfrak{g}_{\geq0} = \mathfrak{g}_{\bar0}\oplus\mathfrak{n}^+$. The **Kac module** is

$$
K(\lambda) = U(\mathfrak{g})\otimes_{U(\mathfrak{g}_{\geq0})}L_0(\lambda),
$$

the induced module on which $\mathfrak{n}^+$ acts by zero; it is the super-analogue of the Verma module of *Universal Enveloping Algebras*, and by the super Poincaré–Birkhoff–Witt theorem its dimension over $k$ is $\dim L_0(\lambda)\cdot2^{\dim\mathfrak{g}_{\bar1}^{+}}$.

**Theorem (Kac, standard).** Every simple finite-dimensional $\mathfrak{g}$-module is the head of a unique Kac module $K(\lambda)$ with $\lambda$ a dominant integral weight, so that the simple finite-dimensional modules are indexed by the dominant integral weights; the Kac module $K(\lambda)$ is either simple — and then $\lambda$ is called **typical** — or has a unique maximal submodule and a composition series of length $>1$ — and then $\lambda$ is called **atypical**. The set of typical weights is the complement of a union of hyperplanes in $\mathfrak{h}^*$, and for a typical weight the **Berezin–Kac character formula**

$$
\operatorname{ch}K(\lambda) = \frac{\sum_{w\in W}(-1)^{\lvert w\rvert}w\bigl(e^{\lambda+\rho}\prod_{\alpha\in\Delta^+_{\bar1}}\bigl(1+e^{-\alpha}\bigr)\bigr)}{\prod_{\alpha\in\Delta^+_{\bar0}}\bigl(e^{\alpha/2}-e^{-\alpha/2}\bigr)}
$$

holds, the product over the odd positive roots being the factor that distinguishes the super-character from the ordinary character; the character is read as the **supercharacter** $\operatorname{ch}V = \sum_\mu(\dim V_\mu)\,e^\mu$ with the dimensions taken in the super sense.

*Proof (outline).* The Kac module is the induced module from the Borel-like subalgebra, and the standard argument of highest weight theory identifies its simple quotients with the finite-dimensional simple modules. The character formula for the typical case is proved by computing the supercharacter of the induced module through the super Poincaré–Birkhoff–Witt theorem, which exhibits the quotient of $U(\mathfrak{n}^-)$ by the odd part as an exterior algebra, and the factors $1+e^{-\alpha}$ over the odd positive roots are precisely the characters of that exterior algebra. The atypical case requires the theory of the Verdier duality and the projective modules, in which the multiplicities of the composition factors are given by the Kazhdan–Lusztig-type polynomials of Serganova; that theory uses the Hecke algebras of the category *Symmetric Linear Algebras* and is part of the deeper structure of the subject. $\square$

**Proposition.** The category of finite-dimensional $\mathfrak{g}$-modules is not semisimple in general: for $\mathfrak{gl}(m|n)$ with $m,n\geq1$ there are non-split extensions, and the simple modules need not be projective; the exceptional cases in which the finite-dimensional module category is semisimple include the orthosymplectic algebras $\mathfrak{osp}(1|2n)$, where the category behaves as in the ungraded semisimple theory and complete reducibility holds.

*Proof (outline).* A non-split extension is exhibited by the Kac module of an atypical weight, which has a maximal submodule and hence is an extension of two simple modules that does not split; the semisimplicity in the orthosymplectic case $\mathfrak{osp}(1|2n)$ is the standard complete reducibility of the finite-dimensional representations of that algebra, proved by the invariant-theoretic argument of the theory of the supergroups. $\square$

**Example.** For $\mathfrak{g} = \mathfrak{sl}(1|1)$ the even part is one-dimensional, the odd part is two-dimensional, and the odd root is isotropic, so that the atypicality condition $\langle\lambda+\rho,\alpha\rangle = 0$ is automatic and every weight is atypical; the Kac modules have length two, and the finite-dimensional simple modules, the one-dimensional and the two-dimensional ones, are read off directly from the relations. For $\mathfrak{gl}(m|n)$ with $m\neq n$ the typical weights form the complement of the hyperplanes $\langle\lambda+\rho,\alpha\rangle = 0$ for the odd isotropic roots $\alpha$, and on the typical part the character formula above reduces the representation theory to the representation theory of the even part, in parallel with the ungraded highest weight theory of *Representations of Lie Algebras*.

## Cohomology of a Lie Superalgebra

**Definition.** Let $\mathfrak{g}$ be a Lie superalgebra over $k$ and $M$ a $\mathfrak{g}$-supermodule. The **Chevalley–Eilenberg complex** of the super case has

$$
C^n(\mathfrak{g};M) = \operatorname{Hom}_k\bigl(S^n(\mathfrak{g}),M\bigr), \qquad S^n(\mathfrak{g}) = \bigoplus_{p+q=n}S^p(\mathfrak{g}_{\bar0})\otimes\Lambda^q(\mathfrak{g}_{\bar1}),
$$

with the differential given by the same display as in *Lie Algebra Cohomology*, the signs now also involving the parity of the arguments and the action of the odd elements; its cohomology is $H^\bullet(\mathfrak{g};M)$.

**Theorem.** The complex is a complex — that is, $d^2 = 0$ — and

$$
H^n(\mathfrak{g};M)\cong\operatorname{Ext}^n_{U(\mathfrak{g})}(k,M)
$$

for every supermodule $M$, so that the cohomological interpretations of the low degrees hold as in the ungraded case: $H^0$ is the invariants, $H^1$ the derivations modulo the inner superderivations, $H^2$ the classes of abelian extensions of the Lie superalgebra; the identification is proved by the resolution $U(\mathfrak{g})\otimes S^\bullet(\mathfrak{g})\to k$, which is free by the super Poincaré–Birkhoff–Witt theorem.

*Proof (outline).* The proofs of the ungraded case carry over with the sign rule: the vanishing of $d^2$ is again the super Jacobi identity together with the associativity of the action, and the freeness of the resolution is the super Poincaré–Birkhoff–Witt theorem of the second section applied to the super-symmetric algebra. The verification of the super Jacobi identity in the matrix case was recorded above. $\square$

**Corollary.** The cohomology with coefficients in the trivial module classifies the central extensions and, in degree three, the obstructions; the deformation theory of a Lie superalgebra is governed by $H^2(\mathfrak{g};\mathfrak{g})$, and the degeneracy of the super-Killing form makes the deformation spaces of the defective types larger than the ungraded theory would predict. For a classical simple Lie superalgebra of characteristic zero the **invariant super-forms** $S^\bullet(\mathfrak{g}^*)^{\mathfrak{g}}$ are cocycles and inject into $H^\bullet(\mathfrak{g};k)$; the two coincide when the super-Killing form is non-degenerate, by the super-analogue of the theorem of Koszul of *Lie Algebra Cohomology*, while in the defective cases the cohomology with trivial coefficients is strictly larger than the invariants, the defect producing classes that have no ungraded counterpart.

## Summary

A **graded Lie algebra** is a Lie algebra with a decomposition $\mathfrak{g} = \bigoplus_{i\in\Gamma}\mathfrak{g}_i$ and $[\mathfrak{g}_i,\mathfrak{g}_j]\subseteq\mathfrak{g}_{i+j}$; a graded Lie algebra of the second kind allows also brackets shifted by one in the degree. The loop algebra $\mathfrak{g}\otimes k[t,t^{-1}]$ with $[x\otimes t^m,y\otimes t^n] = [x,y]\otimes t^{m+n}$ is the universal $\mathbb{Z}$-graded example, its central extension is the affine algebra used in *Vertex Algebras*, and the cyclic gradings of a simple Lie algebra are given by the Kac coordinates, a sequence of integers on the simple roots with the degree of a root vector the corresponding weighted sum; the three-graded algebras are equivalent to the Jordan pairs by the Tits–Kantor–Koecher construction and the five-graded ones to the Kantor triple systems, the constructions that build the exceptional Lie algebras from the exceptional Jordan algebras. A **Lie superalgebra** is the parity-graded case with the Koszul sign rule; the superalgebraic background — the super Jacobi identity, the supertrace, $\mathfrak{gl}(m|n)$, $\mathfrak{psl}(n|n)$, $\mathfrak{osp}(m|n)$ and the classification of the simple ones by Kac — is that of the written *Superalgebras and Graded Structures*. Its **enveloping algebra** has the super Poincaré–Birkhoff–Witt theorem, with the associated graded the super-symmetric algebra $\operatorname{Sym}(\mathfrak{g}_{\bar0})\otimes\Lambda(\mathfrak{g}_{\bar1})$, of Poincaré series $(1-t)^{-p}(1+t)^q$, and with zero divisors as soon as an odd element has $[x,x] = 0$; the super-Killing form $\langle x,y\rangle = \operatorname{str}(\rho(x)\rho(y))$ is invariant and supersymmetric but can be degenerate, the degeneracy measuring the defect of the algebra and forcing the Casimir to be non-central, and the **Kac modules** $K(\lambda) = U(\mathfrak{g})\otimes_{U(\mathfrak{g}_{\geq0})}L_0(\lambda)$ classify the simple finite-dimensional modules up to the distinction between the **typical** and the **atypical** weights, with the Berezin–Kac character formula in the typical case and the Kazhdan–Lusztig-type theory of Brundan–Kazhdan in the atypical one; the finite-dimensional module category is not semisimple except in the exceptional orthosymplectic cases. The **cohomology** of a Lie superalgebra is computed by the Chevalley–Eilenberg complex on the super-symmetric powers, with the same identifications and interpretations as in the ungraded theory, and the invariant super-forms compute the cohomology with trivial coefficients. The analytic theory of the affine and Kac–Moody algebras, and the geometry of the supermanifolds and the supergroups, are deferred to Parts III and II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{g} = \bigoplus_{i\in\Gamma}\mathfrak{g}_i$ | graded Lie algebra |
| $\mathfrak{g}_{\bar0}\oplus\mathfrak{g}_{\bar1}$, $\lvert x\rvert$ | parity decomposition and parity of a homogeneous element |
| $[x,y] = -(-1)^{\lvert x\rvert\lvert y\rvert}[y,x]$ | super anticommutativity (from *Superalgebras and Graded Structures*) |
| $\mathfrak{g}\otimes k[t,t^{-1}]$ | loop algebra |
| $(m_1,\dots,m_r)$, $n = \sum a_im_i$ | Kac coordinates and order of a cyclic grading |
| $\mathfrak{g}_{-1}\oplus\mathfrak{g}_0\oplus\mathfrak{g}_1$ | three-graded Lie algebra, Tits–Kantor–Koecher |
| $U(\mathfrak{g})$ | enveloping algebra of a Lie superalgebra |
| $\operatorname{Sym}(\mathfrak{g}_{\bar0})\otimes\Lambda(\mathfrak{g}_{\bar1})$ | super-symmetric algebra, associated graded |
| $\operatorname{str}$ | supertrace |
| $\langle x,y\rangle = \operatorname{str}(\rho(x)\rho(y))$ | super-Killing form |
| $\Omega = \sum_ix_iy_i$ | Casimir element of a defective or non-degenerate case |
| $\mathfrak{n}^-\oplus\mathfrak{h}\oplus\mathfrak{n}^+$ | triangular decomposition |
| $K(\lambda) = U(\mathfrak{g})\otimes_{U(\mathfrak{g}_{\geq0})}L_0(\lambda)$ | Kac module |
| typical, atypical | simplicity of the Kac module, hyperplane condition |
| $\operatorname{ch}V$ | supercharacter |
| $C^n(\mathfrak{g};M) = \operatorname{Hom}(S^n\mathfrak{g},M)$ | Chevalley–Eilenberg complex, super case |

## Further Reading

- Victor G. Kac, "Lie superalgebras", *Advances in Mathematics* **26** (1977), 8–96, for the classification of simple Lie superalgebras, the Kac modules and the character formula.
- Victor G. Kac, "Representations of classical Lie superalgebras", in *Differential Geometrical Methods in Mathematical Physics II* (Springer Lecture Notes in Mathematics 676, 1978), for the typical and atypical representations.
- Vera Serganova, "Kazhdan–Lusztig polynomials and character formula for the Lie superalgebra $\mathfrak{gl}(m|n)$", *Selecta Mathematica* **2** (1996), 607–651, for the characters of the atypical representations and the Hecke-algebraic methods.
- Manfred Scheunert, *The Theory of Lie Superalgebras* (Springer Lecture Notes in Mathematics 716, 1979), for the enveloping algebra, the super Poincaré–Birkhoff–Witt theorem and the invariant forms.
- Victor G. Kac, *Infinite Dimensional Lie Algebras* (Cambridge University Press, 3rd ed. 1990), for the loop algebras, the gradings of the simple Lie algebras and the Kac coordinates.
- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), and Erhard Neher, "Lie algebras graded by $3$-gradings and the Tits–Kantor–Koecher construction", for the three-graded algebras and their Jordan structures.
- Max Koecher, "Imbedding of Jordan algebras into Lie algebras", *American Journal of Mathematics* **89** (1967), 787–816, for the Tits–Kantor–Koecher construction.
