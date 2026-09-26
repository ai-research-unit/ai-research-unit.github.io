
# __Linear Algebraic Groups__

## Introduction

A **linear algebraic group** over a field $k$ is a subgroup of the general linear group $GL_n$ cut out by polynomial equations with coefficients in $k$. It is at once a group and an algebraic variety, and the interplay of the two structures is the whole subject: the group operations are polynomial, hence continuous for the **Zariski topology**, and the translations of the group make that weak topology rigid enough to classify the groups by combinatorial data. The object is the meeting point of the two lines that run through this Part — the topological group of *Topological Groups*.

Three structures are used from above and are not rebuilt here. The abstract root system, its Dynkin diagram and the classification of the irreducible reduced root systems are those of *Root Systems and Classification* of Part I; the Lie algebra, its universal enveloping algebra and the structure theory of semisimple Lie algebras are those of *Lie Algebras* and *Structure of Lie Algebras* of Part I; the Coxeter system, its length function and its parabolic subgroups are those of *Coxeter Groups* of Part I. The Zariski topology of the spectrum of a ring is that of *Commutative Algebras* of Part I, and the concrete topology of polynomial zero sets, its failure of Hausdorffness and its non-metrisability are the ones named in *Metrisation and Separation Axioms* of this category. Dimension is the Krull dimension of the coordinate ring of *Integral Extensions and Krull Dimension* and *Primary Decomposition* of Part I.

Two structures are **deferred**, and neither is used in any proof below. First, the scheme-theoretic treatment: this article states the Zariski topology concretely, as the topology of the zero sets of polynomials, and treats a linear algebraic group as a reduced affine variety; the general theory of varieties, the structure sheaf, the group scheme and the cohomology that classifies the $k$-forms are the subject , below this category in the menu andwhere the variety, the sheaf and the group cohomology become available. That is the one forward reference this article makes, and everything it states is stated in the concrete terms available here. Second, the passage to the Lie algebra: for $k = \mathbb{R}$ or $\mathbb{C}$ the group is a Lie group, and *Lie Groups* and *The Lie Algebra and the Exponential Map*, earlier entries of this category, attach to it a Lie algebra; but the correspondence requires the manifold and the exponential map, neither of which exists in the algebraic category over a general field, and no argument below uses the exponential map. The roots are therefore defined through the subgroups of $G$ on which a torus acts by a character, not through the adjoint action on a Lie algebra.

Throughout, $k$ is a field, $\bar k$ an algebraic closure of $k$ and $k^s$ the separable closure of $k$ in $\bar k$, $G$ a linear algebraic group over $k$, $T$ a torus, $B$ a Borel subgroup and $W$ the Weyl group; $\mathbb{G}_a$ and $\mathbb{G}_m$ are the additive and multiplicative groups, and $GL_n(k)$ is the group of $k$-points of $GL_n$. Where a result needs $k$ algebraically closed, of characteristic zero, or perfect, this is flagged at the statement. The classical matrix groups, with their forms and their real and complex topologies, are treated in this category; only the algebraic-group structure is developed here.

## Linear Algebraic Groups and the Zariski Topology

### The Zariski Topology on Affine Space

**Definition.** Affine $n$-space over $k$ is the set $\mathbb{A}^n_k = k^n$ with coordinate ring $k[x_1,\ldots,x_n]$. For an ideal $\mathfrak{a} \subseteq k[x_1,\ldots,x_n]$ the **zero set** is

$$
V(\mathfrak{a}) = \{a \in \mathbb{A}^n_k : f(a) = 0 \text{ for all } f \in \mathfrak{a}\},
$$

and the **Zariski topology** on $\mathbb{A}^n_k$ has these sets as its closed sets; equivalently, a set is closed if it is the zero set of an arbitrary family of polynomials, since $\bigcap_i V(\mathfrak{a}_i) = V(\sum_i\mathfrak{a}_i)$ and $V(\mathfrak{a})\cup V(\mathfrak{b}) = V(\mathfrak{ab})$. A **principal open set** is $D(f) = \mathbb{A}^n_k \setminus V(f)$ for $f \neq 0$, and these form a basis of the topology. The Zariski topology is the topology of the prime spectrum of *Commutative Algebras*, read on the maximal ideals $k[x_1,\ldots,x_n]/\mathfrak{m} \cong k$ when $k$ is algebraically closed.

**Proposition.** The Zariski topology on $\mathbb{A}^n_k$ is Noetherian: every descending chain of closed sets stabilises, every closed set is a finite union of irreducible closed sets, and the irreducible components are unique. In particular $\mathbb{A}^n_k$ is quasicompact. For infinite $k$ the space is $T_1$ but not Hausdorff, and it is not metrisable.

*Proof.* The polynomial ring is Noetherian by *Noetherian and Artinian Rings* of Part I, so a descending chain $V(\mathfrak{a}_1) \supseteq V(\mathfrak{a}_2) \supseteq \cdots$ corresponds to an ascending chain of radical ideals, which stabilises; the decomposition into irreducibles follows from the descending chain condition on closed sets, and uniqueness from the definition of an irreducible component. The space is $T_1$ because points are closed, $V(x-a) = \{a\}$; it is not Hausdorff because for infinite $k$ any two nonempty open sets meet, so two distinct points have no disjoint neighbourhoods. The failure of metrisability is the example of *Metrisation and Separation Axioms*. $\square$

**Definition.** A subset $X \subseteq \mathbb{A}^n_k$ is **irreducible** if it is nonempty and cannot be written as the union of two proper closed subsets; a closed irreducible subset is an **affine variety**, and its **coordinate ring** is $k[X] = k[x_1,\ldots,x_n]/I(X)$ with $I(X)$ the ideal of polynomials vanishing on $X$. The **dimension** of $X$ is the Krull dimension of its coordinate ring, and $X$ is **reduced** because $I(X)$ is a radical ideal.

**Remark (connectedness and irreducibility).** An irreducible space is connected, and for an affine variety the two notions are governed by the same algebra: the components of the variety are the maximal irreducible closed subsets, and the variety is connected exactly when its coordinate ring has no idempotent other than $0$ and $1$, that is, when the ring is not a product of two nonzero rings. Only connectedness is used in this article; irreducibility is used in the classification of the components of an algebraic group below.

### The General Linear Group as an Algebraic Group

**Definition.** The general linear group is the principal open subset of affine $n^2$-space,

$$
GL_n = \{A \in \mathbb{A}^{n^2}_k : \det A \neq 0\} = D(\det),
$$

with coordinate ring $k[GL_n] = k[x_{ij}, d^{-1}]$ where $d = \det(x_{ij})$ is the determinant polynomial in the indeterminates $x_{ij}$. The matrix $A$ is invertible exactly when $d(A) \neq 0$, and the group law is matrix multiplication.

**Theorem.** $GL_n$ is a linear algebraic group: $k[GL_n]$ is a reduced finitely generated $k$-algebra of dimension $n^2$, the multiplication $GL_n \times GL_n \to GL_n$ and the inversion $GL_n \to GL_n$ are polynomial maps, hence morphisms of affine varieties, and therefore the group operations are continuous for the Zariski topology.

*Proof.* The coordinate ring is a localisation of the polynomial ring, hence reduced and finitely generated; its dimension is $n^2$ because a localisation of a domain by a nonzero element has the same fraction field and the same dimension as the domain, by the dimension theory of *Integral Extensions and Krull Dimension*. The entries of a product $AB$ are the polynomials $\sum_r x_{ir}y_{rj}$ in the entries of $A$ and $B$, so multiplication is polynomial. Inversion is given by Cramer's rule, $A^{-1} = d(A)^{-1}\operatorname{adj}(A)$, whose entries are polynomials in the $x_{ij}$ and in $d^{-1}$, so inversion is polynomial on $D(\det)$. Continuity of the operations for a topology whose closed sets are polynomial zero sets is then immediate: the preimage of a closed set under a polynomial map is closed. $\square$

**Remark.** The last sentence is the reason the Zariski topology is the right one: it is defined by the polynomials, and the group law is polynomial, so the group is a **topological group** in the sense of *Topological Groups*. This is the only property of the operations used in this article, and it is the sense in which a linear algebraic group is a topological group whose topology happens to be determined by a ring of functions.

### Linear Algebraic Groups and their Morphisms

**Definition.** A **linear algebraic group over $k$** is a closed subgroup $G \subseteq GL_n$ over $k$ for some $n$: a subgroup that is the zero set of a family of polynomial functions on $GL_n$ with coefficients in $k$. The subspace topology on $G$ is the **Zariski topology** of $G$, and $G$ is a reduced affine variety with a group structure for which the operations are morphisms. The group of **$k$-points** is $G(k) = G \cap GL_n(k)$. A **morphism** $\varphi : G \to H$ of linear algebraic groups over $k$ is a group homomorphism that is a polynomial map with coefficients in $k$; it is an **isomorphism** if it is bijective with polynomial inverse, and an **isogeny** if it is surjective with finite kernel.

**Example (the basic list).** The following closed subgroups of $GL_n$ are the standard examples, defined over any field containing the coefficients of the equations:

| Group | Defining equations | Dimension |
|---|---|---|
| $\mathbb{G}_a$ | $\left\{\begin{pmatrix}1&t\\0&1\end{pmatrix}\right\}$ in $GL_2$ | $1$ |
| $\mathbb{G}_m$ | $GL_1$ | $1$ |
| $SL_n$ | $\det A = 1$ | $n^2-1$ |
| $T_n$ | invertible diagonal | $n$ |
| $B_n$ | invertible upper triangular | $n(n+1)/2$ |
| $U_n$ | upper unitriangular | $n(n-1)/2$ |
| $O(q)$ | $A^{\mathsf{T}} J A = J$, $q$ a form | $n(n-1)/2$ |
| $Sp_{2n}$ | $A^{\mathsf{T}} J A = J$, $J$ symplectic | $2n^2+n$ |

The dimensions follow from the definitions in the sections below: $GL_n$ has dimension $n^2$, the diagonal torus $T_n$ has dimension $n$, the Borel $B_n$ has dimension $n(n+1)/2$, and its unipotent radical $U_n$ has dimension $n(n-1)/2$, so that $n(n+1)/2 = n + n(n-1)/2$ in agreement with the decomposition $B_n = T_n \ltimes U_n$.

### Dimension, and the Deferred Scheme Theory

**Definition.** The **dimension** $\dim G$ of a linear algebraic group is the Krull dimension of its coordinate ring; it is also the dimension of $G$ as a variety over $\bar k$. Because $G$ acts transitively on itself by left translation, which is an isomorphism of varieties, the dimension is the same at every point and $G$ is **equidimensional**.

**Theorem.** For a connected linear algebraic group $G$ and a closed subgroup $H$, $\dim G = \dim H + \dim G/H$; in particular a closed subgroup of the same dimension as a connected $G$ equals $G$.

*Proof sketch.* The quotient $G/H$ is a homogeneous variety of dimension $\dim G - \dim H$, and the fibres of $G \to G/H$ are the cosets of $H$, all translates of $H$; the dimension formula is the standard one for a morphism whose fibres all have the same dimension, quoted from the dimension theory of Part I together with the construction of the quotient. If $\dim H = \dim G$ then $G/H$ has dimension zero, hence is finite or a point for connected $G$, and a closed subgroup of finite index in a connected group is the whole group. $\square$

**Remark (the deferral).** The quotient $G/H$ and the structure of a variety are used here only through the dimension formula and through the topological facts stated above. The intrinsic construction of the variety, the structure sheaf, the group scheme and the cohomology with coefficients in a $G$-module are the subject , below this category in the menu andand this article does not reason with them. In particular the $k$-forms of a group — the groups over $k$ that become isomorphic to a given group over $\bar k$ — are classified by a cohomology set whose construction belongs to those articles, and only the resulting vocabulary of split and anisotropic forms is used below, with the classification quoted as standard.

## Connectedness and the Component Group

### The Components of an Algebraic Group

**Theorem.** Let $G$ be a linear algebraic group. The identity component $G^\circ$ — the connected component of $G$ containing the identity — is a closed, connected, normal subgroup of finite index, the connected components of $G$ are the cosets $gG^\circ$, and the **component group** $G/G^\circ$ is finite. Moreover $G$ is connected if and only if $G$ is irreducible.

*Proof.* The components are finite in number because $G$ is a Noetherian topological space, and each is clopen, so a component is both closed and open. For $g \in G$ the left translation $x \mapsto gx$ is a homeomorphism carrying $G^\circ$ to the component of $g$, so the components are the cosets $gG^\circ$ and there are finitely many of them. If $x, y \in G^\circ$ then $xyG^\circ = x(yG^\circ) = xG^\circ = G^\circ$, so $G^\circ$ is closed under multiplication, and $xG^\circ = G^\circ$ gives $G^\circ = x^{-1}G^\circ$, so $x^{-1} \in G^\circ$. For normality, $x \mapsto gxg^{-1}$ is a homeomorphism fixing the identity, so it preserves $G^\circ$. Finally, a linear algebraic group is a disjoint union of finitely many irreducible closed sets, and the group acts transitively on the set of these irreducible components by translation, exactly as for the connected components; hence there is one irreducible component exactly when there is one connected component, and $G$ is irreducible if and only if it is connected. $\square$

**Corollary.** A linear algebraic group is connected if and only if it has exactly one irreducible component, and then its coordinate ring is a domain. The component group $G/G^\circ$ is a finite group, and $G$ is the disjoint union of the cosets of $G^\circ$.

**Remark.** The group $G/G^\circ$ can be any finite group: every finite group $\Gamma$ embeds in $GL_{|\Gamma|}$ as its regular representation, and a finite subgroup is a closed $0$-dimensional subgroup with $G^\circ = \{1\}$, so $G/G^\circ = \Gamma$. The finiteness of the component group is therefore the only restriction at this level.

### Examples of Component Groups

**Example.** $GL_n$ and $SL_n$ are connected. The determinant exhibits $GL_n$ as an extension of $\mathbb{G}_m$ by $SL_n$, and the map $\mathbb{G}_m \times SL_n \to GL_n$, $(t,A) \mapsto \mathrm{diag}(t,1,\ldots,1)A$, is an isomorphism of varieties, since every $g$ is $\mathrm{diag}(\det g,1,\ldots,1)\cdot A$ with $A$ of determinant one; a product of connected varieties is connected. $SL_n$ is generated by the elementary matrices $I + aE_{ij}$ for $i \neq j$, each lying in the image of a morphism $\mathbb{G}_a \to SL_n$ sending $0$ to the identity, so $SL_n$ is connected as it is generated by connected subgroups containing the identity.

**Example.** For a nondegenerate quadratic form $q$ of dimension $n$ over a field of characteristic not two, the orthogonal group $O(q)$ has two connected components whenever $q$ is nondegenerate and $n \geq 1$: the special orthogonal group $SO(q) = \ker(\det|_{O(q)})$ is connected, and a reflection $\tau$ with $\tau^2 = 1$ has $\det \tau = -1$, so $O(q) = SO(q) \sqcup \tau\,SO(q)$ and $G/G^\circ \cong \mathbb{Z}/2\mathbb{Z}$. The description of these groups as matrix groups with a metric is .

**Example (a connected group whose points are not connected).** Let $k = \mathbb{R}$ and $G = GL_n$. The algebraic group $GL_n$ is connected in the Zariski topology, but its real points $GL_n(\mathbb{R})$ with the real topology have two components, the matrices of positive and of negative determinant. There is no contradiction: the sign of the determinant is not a polynomial condition, so the Zariski topology on $GL_n(\mathbb{R})$ cannot separate the two real components. Statements in this article about connectedness are statements about the algebraic group; for the topological components of the real or complex points one must pass to the finer topology of *Lie Groups*.

## The Basic Examples

### The Additive and Multiplicative Groups

**Definition.** The **additive group** $\mathbb{G}_a$ has coordinate ring $k[t]$ and group law $t \cdot t' = t + t'$, realised as the closed subgroup of upper unitriangular matrices in $GL_2$. The **multiplicative group** $\mathbb{G}_m$ is $GL_1$, with coordinate ring $k[t,t^{-1}]$ and group law $t\cdot t' = tt'$. Both are connected of dimension one. A **torus** is a linear algebraic group $T$ with $T(\bar k) \cong (\bar k^\times)^r$; it is **split** over $k$ if $T \cong \mathbb{G}_m^r$ over $k$, and $r = \dim T$ is its rank.

**Theorem.** Every one-dimensional connected linear algebraic group is isomorphic to $\mathbb{G}_a$ or to $\mathbb{G}_m$.

*Proof sketch.* A connected one-dimensional algebraic group is either unipotent or a torus: the unipotent part is normal and connected, and if it is trivial the group is diagonalisable by the structure theorem for diagonalisable groups below. A connected unipotent group of dimension one is $\mathbb{G}_a$ by the classification of unipotent groups, and a one-dimensional torus over $\bar k$ is $\mathbb{G}_m$. $\square$

**Remark.** The dichotomy is the algebraic shadow of the two one-dimensional real Lie groups $\mathbb{R}$ and $SO(2)$: $\mathbb{G}_a(\mathbb{R}) = \mathbb{R}$ and the anisotropic torus of the next paragraph has real points the circle. The two are not isomorphic over any field, and their characters and cocharacters are as different as the two group laws.

### The Classical Groups

**Definition.** The **special linear group** $SL_n$ is the kernel of $\det : GL_n \to \mathbb{G}_m$, of dimension $n^2-1$. For a nondegenerate bilinear form $g$ on $k^n$, the **isometry group** is $O(g) = \{A : g(Ax,Ay) = g(x,y)\}$, of dimension $n(n-1)/2$, and $SO(g)$ is its determinant-one subgroup; for an alternating form the **symplectic group** $Sp_{2n}$ is the isometry group, of dimension $2n^2+n$; for a Hermitian form over a quadratic extension the **unitary group** $U(g)$ is the isometry group, of dimension $n^2$. These are the classical groups, and each is linear algebraic, defined over the field generated by the coefficients of its form.

**Example (the orthogonal group as the unit group of a form).** The unit group of the algebra of $2\times 2$ matrices is $GL_2$, and the elements preserving the quadratic form $N(x) = x_1^2 + x_2^2$ form $O(2)$; the algebraic group $SO(2)$ is a one-dimensional torus, anisotropic over $\mathbb{R}$ because $x_1^2 + x_2^2$ has no nontrivial real zero, while $SO(1,1)$ for the form $x_1^2 - x_2^2$ is split and isomorphic to $\mathbb{G}_m$. The two forms give non-isomorphic groups over $\mathbb{R}$ and isomorphic groups over $\mathbb{C}$, which is the simplest instance of the $k$-form phenomenon of the last section. The quadratic forms themselves are those of Part I.

### Triangular and Unipotent Subgroups

**Definition.** Fix an ordered basis of $k^n$. The **diagonal torus** $T_n$ is the group of invertible diagonal matrices, isomorphic to $\mathbb{G}_m^n$; the **Borel subgroup** $B_n$ is the group of invertible upper triangular matrices; and the **unipotent radical** $U_n$ of $B_n$ is the group of upper unitriangular matrices, those with all diagonal entries equal to one.

**Theorem.** $B_n = T_n \ltimes U_n$, with $\dim T_n = n$, $\dim B_n = n(n+1)/2$ and $\dim U_n = n(n-1)/2$. The group $T_n$ is a torus, $U_n$ is a connected unipotent group, and $B_n$ is connected solvable.

*Proof.* Every invertible upper triangular matrix factors uniquely as a diagonal matrix times an upper unitriangular one, and the diagonal part is normalised by $U_n$, so the product is semidirect. The dimensions are the numbers of free matrix entries: $n$ on the diagonal, $n(n+1)/2$ in the upper triangle, and $n(n-1)/2$ strictly above the diagonal. The group $U_n$ is generated by the elementary matrices $I + aE_{ij}$ with $i<j$, each of which is unipotent and lies in the image of a morphism from $\mathbb{G}_a$, so $U_n$ is connected unipotent; the solvable series of $B_n$ is the one by the diagonals of increasing distance from the main diagonal. $\square$

## Unipotent and Solvable Groups

### Unipotent Elements and Unipotent Groups

**Definition.** An element $g \in GL_n(k)$ is **unipotent** if $g - 1$ is nilpotent, and **semisimple** if it is diagonalisable over $\bar k$. A linear algebraic group is **unipotent** if every one of its elements is unipotent, and $G$ is **solvable** if its derived series, defined as in *Solvable and Nilpotent Groups* of Part I, terminates at the trivial group. The **unipotent radical** $R_u(G)$ is the largest connected closed normal unipotent subgroup, and the **radical** $R(G)$ is the largest connected closed normal solvable subgroup; both exist, because the product of two connected closed normal unipotent subgroups is one.

**Theorem (Kolchin).** Let $k$ be algebraically closed. Every unipotent subgroup of $GL_n(k)$ is conjugate to a subgroup of $U_n$; consequently every unipotent linear algebraic group is nilpotent, and a connected unipotent group is a successive extension of copies of $\mathbb{G}_a$.

*Proof sketch.* The two statements are proved together, by induction on $n$ and on the dimension of the group. A connected unipotent group $G$ has a central series $1 = G_0 \triangleleft \cdots \triangleleft G_m = G$ with successive quotients isomorphic to $\mathbb{G}_a$, and each quotient acts on the nonzero fixed space of its predecessor by a unipotent operator; over the algebraically closed field $k$ such an operator has the eigenvalue $1$, so the fixed space grows at each stage and there is a nonzero vector fixed by all of $G$. Induction on the quotient of $k^n$ by the line spanned by that vector then exhibits $G$ as conjugate to a subgroup of $U_n$. An arbitrary unipotent subgroup is an extension of a connected unipotent group by a finite unipotent group, and a finite unipotent group acting on a nonzero space over $k$ has a nonzero fixed vector, since its operators are unipotent; the same induction therefore applies to it. A subgroup of $U_n$ is nilpotent because $U_n$ is, and the subgroups generated by the $E_{ij}$ with $j-i \geq d$ exhibit $U_n$ as a successive extension of copies of $\mathbb{G}_a$. $\square$

**Example.** $\mathbb{G}_a \cong U_2$ is unipotent; $U_n$ has dimension $n(n-1)/2$ and its centre consists of the matrices $1 + aE_{1n}$, so for $n \geq 3$ it is a non-abelian nilpotent group. The additive group is the only one-dimensional connected unipotent group.

### Solvable Groups and Lie–Kolchin

**Theorem (Lie–Kolchin).** Let $k$ be algebraically closed. Every connected solvable subgroup of $GL_n(k)$ is conjugate to a subgroup of $B_n$; equivalently, it fixes a complete flag of subspaces, and it has a common eigenvector.

*Proof sketch.* Induct on $\dim G$ and on $n$. If $G \neq 1$ then the derived subgroup $[G,G]$ is a connected solvable group of smaller dimension, because a nontrivial solvable group is not perfect: the last nontrivial term of its derived series would otherwise equal its own derived subgroup. By induction $[G,G]$ fixes a nonzero vector, and its fixed space $V$ is nonzero and $G$-stable because $[G,G]$ is normal. The quotient $G/[G,G]$ is connected abelian, hence a product of a torus and a unipotent group: the torus is diagonalisable, so $V$ decomposes into weight spaces for it, and on each weight space the connected unipotent part acts by unipotent operators, so Kolchin gives a common nonzero fixed vector. A nonzero vector fixed by $G$ therefore exists, and induction on the quotient of $k^n$ by the line it spans produces a complete $G$-stable flag, so that $G$ is conjugate to a subgroup of $B_n$. $\square$

**Corollary.** A connected solvable linear algebraic group is the semidirect product of a torus and a connected unipotent group.

*Proof sketch.* Take a maximal torus $T$ of $G$, which is connected, and the unipotent radical $R_u(G)$; the product $T \cdot R_u(G)$ is a connected solvable subgroup, and by Lie–Kolchin and the conjugacy of maximal tori it is all of $G$. The intersection is trivial, since $T$ contains no nonidentity unipotent element, and $R_u(G)$ is normal. $\square$

**Definition.** A **Borel subgroup** of $G$ is a maximal connected solvable subgroup, and a **parabolic subgroup** is a closed subgroup containing a Borel subgroup. Over an algebraically closed field a closed subgroup is parabolic exactly when it contains a Borel.

**Theorem.** Let $k$ be algebraically closed and $G$ connected. Every Borel subgroup of $G$ is connected and solvable and is the semidirect product $T \ltimes R_u(B)$ of a maximal torus and a maximal connected unipotent subgroup, and every connected solvable subgroup of $G$ lies in a Borel subgroup.

*Proof sketch.* The factorisation $B = T \ltimes R_u(B)$ is the corollary above. The containment of a connected solvable subgroup in a Borel subgroup is Borel's theorem, and it is proved from the fixed point theorem in the section on Borel subgroups below, where the conjugacy of the Borel subgroups and of the maximal tori is stated as well. $\square$

## Tori, Characters and Cocharacters

### Diagonalisable Groups and Tori

**Definition.** A linear algebraic group is **diagonalisable** if it is isomorphic to a closed subgroup of a torus, equivalently if every representation of it is a direct sum of one-dimensional ones. A **torus** is a connected diagonalisable group.

**Theorem.** A diagonalisable group over an algebraically closed field is a direct product $\mathbb{G}_m^r \times A$ with $A$ a finite abelian group whose order is coprime to $\operatorname{char} k$; consequently $r = \dim T$ for the connected ones, and $T \cong \mathbb{G}_m^r$ with $r = \dim T$.

*Proof sketch.* Diagonalisable groups are classified by their character group, which is a finitely generated abelian group; the free part of rank $r$ gives the torus factor and the torsion part gives the finite factor, and the condition on the order is what makes the corresponding equations separable. $\square$

### Characters, Cocharacters, and the Duality

**Definition.** Let $T$ be a torus. The **character group** is $X^*(T) = \operatorname{Hom}(T,\mathbb{G}_m)$ and the **cocharacter group** is $X_*(T) = \operatorname{Hom}(\mathbb{G}_m,T)$, both under pointwise multiplication, hence written additively.

**Theorem.** For a torus of dimension $r$ over $k$, the groups $X^*(T)$ and $X_*(T)$ are free abelian of rank $r$, and there is a $\mathbb{Z}$-bilinear pairing

$$
\langle\,\cdot\,,\,\cdot\,\rangle : X^*(T) \times X_*(T) \longrightarrow \mathbb{Z}, \qquad
\langle\chi,\lambda\rangle = m \quad \text{when } \chi(\lambda(t)) = t^m \text{ for all } t,
$$

which is perfect when $T$ is split over $k$; for a general $k$ the induced map $X_*(T) \to \operatorname{Hom}_{\mathbb{Z}}(X^*(T),\mathbb{Z})$ is injective with finite cokernel, and is an isomorphism after tensoring with $\mathbb{Q}$.

*Proof.* A split torus is $\mathbb{G}_m^r$, and a homomorphism $\mathbb{G}_m \to \mathbb{G}_m$ is $t \mapsto t^m$ for a unique $m \in \mathbb{Z}$; hence $X^*(\mathbb{G}_m^r) \cong \mathbb{Z}^r$ and $X_*(\mathbb{G}_m^r) \cong \mathbb{Z}^r$ with the standard dual bases, and the pairing is the standard duality. Over a general $k$ a torus becomes split over a finite separable extension, and the character and cocharacter lattices are the Galois-invariant parts of the corresponding lattices over that extension; the pairing between them is then the standard one, and the cokernel of the comparison map with the dual is finite by the theory of diagonalisable groups, quoted from the literature. $\square$

### Weights

**Definition.** Let $G$ be a linear algebraic group, $T \subseteq G$ a torus and $V$ a rational representation of $G$ — a homomorphism $G \to GL(V)$ that is a morphism. The action of $T$ preserves the eigenspace decomposition and

$$
V = \bigoplus_{\chi \in X^*(T)} V_\chi, \qquad V_\chi = \{v \in V : t\cdot v = \chi(t)v \text{ for all } t \in T\},
$$

the nonzero $V_\chi$ being the **weight spaces** and the characters $\chi$ that occur the **weights** of $V$. Because $T$ is diagonalisable, the sum is a direct sum, and the weights are the characters through which $T$ acts.

**Example.** For $T = T_n$ the diagonal torus of $GL_n$ acting on $k^n$, the weight spaces are the coordinate lines and the weights are $\chi_1, \ldots, \chi_n$ with $\chi_i(\mathrm{diag}(t_1,\ldots,t_n)) = t_i$; on the dual space the weights are $-\chi_1,\ldots,-\chi_n$. The character lattice is $X^*(T_n) = \bigoplus_i \mathbb{Z}\chi_i \cong \mathbb{Z}^n$.

## Root Data

### Root Subgroups and Roots

**Definition.** Let $T$ be a maximal torus of a connected reductive group $G$. A closed connected one-dimensional unipotent subgroup $U \subseteq G$ normalised by $T$ is a **root subgroup** if $T$ acts on it by a nontrivial character, so that for a unique $\alpha \in X^*(T) \setminus \{0\}$,

$$
t u t^{-1} = \alpha(t)\, u \qquad \text{for all } t \in T,\ u \in U.
$$

A nonzero character $\alpha \in X^*(T)$ is a **root** of $(G,T)$ if a root subgroup $U_\alpha$ with this character exists, and $\Phi = \Phi(G,T) \subseteq X^*(T)$ is the set of roots. For each root the subgroup generated by $U_\alpha$ and $U_{-\alpha}$ is a copy of $SL_2$ or of $PGL_2$, and the **coroot** $\alpha^\vee \in X_*(T)$ is the cocharacter through which the torus of that copy sits in $T$.

**Theorem.** Let $G$ be a connected reductive group over an algebraically closed field and $T$ a maximal torus. Then $\Phi(G,T)$ is a root system in $X^*(T) \otimes \mathbb{R}$, reduced and finite, and its abstract type does not depend on the choice of $T$; $\Phi$ together with $\Phi^\vee = \{\alpha^\vee\}$ forms a root datum. The Weyl group $W = N_G(T)/T$ is a finite group generated by the reflections

$$
s_\alpha(\chi) = \chi - \langle\chi, \alpha^\vee\rangle\, \alpha,
$$

and it acts faithfully on $X^*(T)$ preserving $\Phi$.

*Proof sketch.* The finite-dimensionality and the axioms of a root system are proved by transporting the root-space decomposition of the reductive Lie algebra, but they can also be read off directly from the commutator relations of the root subgroups: the classification input is that the $\mathbb{Z}$-span of the roots and coroots carries the axioms of a reduced root system, which is the content of the theory of *Root Systems and Classification*, and it is quoted from there. The group generated by the $s_\alpha$ is independent of the choices and equals $N_G(T)/T$ by the conjugacy of maximal tori and the Bruhat decomposition below. $\square$

### The Root Datum and the Weyl Group

**Definition.** A **root datum** is a quadruple $(X^*, \Phi, X_*, \Phi^\vee)$ consisting of free abelian groups $X^*$, $X_*$ of the same finite rank with a perfect $\mathbb{Z}$-bilinear pairing $\langle\,\cdot\,,\,\cdot\,\rangle : X^* \times X_* \to \mathbb{Z}$, finite subsets $\Phi \subseteq X^*$ and $\Phi^\vee \subseteq X_*$ with a bijection $\alpha \leftrightarrow \alpha^\vee$ satisfying $\langle\alpha,\alpha^\vee\rangle = 2$, such that the reflections $s_\alpha(\chi) = \chi - \langle\chi,\alpha^\vee\rangle\alpha$ permute $\Phi$ and the dual reflections permute $\Phi^\vee$. The root datum is **reduced** if no root is a multiple of another and the only multiples of $\alpha$ in $\Phi$ are $\pm\alpha$.

**Theorem (classification by root data; Chevalley).** Over an algebraically closed field, the map sending a connected reductive group with a chosen maximal torus to its root datum is a bijection between isomorphism classes of connected reductive groups and isomorphism classes of reduced root data. A connected reductive group is semisimple exactly when the root datum is **semisimple**, that is, when $\Phi$ spans $X^* \otimes \mathbb{Q}$; it is a torus exactly when $\Phi$ is empty.

*Proof sketch.* The construction in one direction is the theorem above. In the other, the root datum determines the root system $\Phi$, hence a Dynkin diagram, and Chevalley's construction produces the group by generators and relations from the root datum, with the commutator relations of the root subgroups as the relations; the isogeny classification is the comparison of the lattices $X^*$ and $X_*$ for a fixed root system. The theorem is quoted from the literature of *Root Systems and Classification* and of Borel's and Springer's treatments. $\square$

### The Worked Cases of $GL_n$ and $SL_n$

**Example.** For $G = GL_n$ with the diagonal torus $T_n$, the character lattice is $X^*(T_n) = \bigoplus_{i=1}^n\mathbb{Z}\chi_i$ and the cocharacter lattice is $X_*(T_n) = \bigoplus_i\mathbb{Z}\chi_i^\vee$ with $\langle\chi_i,\chi_j^\vee\rangle = \delta_{ij}$. The roots are

$$
\Phi = \{\chi_i - \chi_j : i \neq j\},
$$

one for each ordered pair of distinct indices, so $|\Phi| = n(n-1)$; a positive system is $\{\chi_i - \chi_j : i < j\}$, of size $n(n-1)/2$, and the coroots are $\alpha_{ij}^\vee = \chi_i^\vee - \chi_j^\vee$. The Weyl group is $W \cong S_n$, acting by permuting the coordinates, of order $n!$. The dimension check is

$$
\dim GL_n = \dim T_n + |\Phi| = n + n(n-1) = n^2,
$$

which is the dimension of $GL_n$ computed above, and the sum of the dimensions of the two opposite maximal unipotent subgroups is $|\Phi| = n(n-1)$, so each has dimension $n(n-1)/2$. For $SL_n$ the character lattice is the quotient $X^*(T) = \mathbb{Z}^n/\mathbb{Z}(1,\ldots,1)$ of rank $n-1$, the roots are the images of the $\chi_i - \chi_j$, the Weyl group is still $S_n$, and $\dim SL_n = (n-1) + n(n-1) = n^2-1$. For $n = 2$ the group $GL_2$ has roots $\pm(\chi_1-\chi_2)$, one positive root, and $\dim = 2 + 2 = 4$; for $n = 3$, $|\Phi| = 6$, three positive roots, and $\dim = 3 + 6 = 9$.

**Example.** For $Sp_{2n}$ the root system is of type $C_n$ and for $SO_{2n+1}$ of type $B_n$, with $|\Phi| = 2n^2$ and $2n^2$ respectively, and the dimension formula gives $\dim Sp_{2n} = n + 2n^2 = 2n^2+n$ and $\dim SO_{2n+1} = n + 2n^2 = n(2n+1)$, in agreement with the table; these are the identifications of the classical root systems with the classical groups of *Root Systems and Classification*.

## Borel and Parabolic Subgroups

### Borel Subgroups and the Fixed Point Theorem

**Theorem (Borel fixed point theorem).** Let $k$ be algebraically closed and let a connected solvable linear algebraic group $G$ act on a nonempty complete variety $X$. Then $G$ has a fixed point.

*Proof sketch.* This is the standard theorem of Borel, quoted from the structure theory. The case $G = \mathbb{G}_m$ is read off from the weight decomposition of a torus action, and the case $G = \mathbb{G}_a$ is the statement that an orbit of $\mathbb{G}_a$ in a complete variety is a point, since the orbit is the image of an affine line; the general connected solvable group is built from these two by successive extensions, so induction on $\dim G$ gives the theorem. Completeness is the one property of the variety theory that is used, and it is part of the theory named in the deferral in the Introduction. $\square$

**Corollary (conjugacy theorems; Borel).** Let $k$ be algebraically closed and $G$ connected. All Borel subgroups of $G$ are conjugate, all maximal tori of $G$ are conjugate, every maximal torus lies in a Borel subgroup, and every connected solvable subgroup of $G$ lies in a Borel subgroup.

*Proof sketch.* Apply the fixed point theorem to the action of a connected solvable subgroup $S$ of $G$ on the complete flag variety $G/B$: a fixed point is a coset $gB$ with $S \subseteq gBg^{-1}$. For $S = B'$ a Borel subgroup this is the conjugacy of the Borel subgroups; for $S$ a maximal torus $T$ it produces a Borel containing $T$. Every Borel contains a maximal torus, by the factorisation $B = T \ltimes R_u(B)$, and any two maximal tori of a fixed Borel $B$ are conjugate, being complements to the unipotent radical; the three statements are the conjugacy theorems of the structure theory and are quoted as standard. $\square$

### Parabolic Subgroups and the Levi Decomposition

**Definition.** A closed subgroup $P \subseteq G$ is **parabolic** if it contains a Borel subgroup. Over an algebraically closed field this is equivalent to $G/P$ being complete, and the equivalence is the standard one; the concrete definition is used here.

**Theorem (Levi decomposition).** Let $G$ be a connected linear algebraic group over a field $k$ of characteristic zero (more generally, over a perfect field, for reduced groups). Then $G$ is the semidirect product

$$
G = R_u(G) \rtimes L
$$

of its unipotent radical $R_u(G)$ and a maximal reductive subgroup $L$, called a **Levi factor**; the Levi factor is unique up to conjugacy by an element of $R_u(G)$, and $G/R_u(G) \cong L$ is reductive. For a parabolic subgroup $P$, the same statement reads $P = R_u(P) \rtimes L$ with $L$ reductive.

*Proof sketch.* The quotient $G/R_u(G)$ is reductive because the unipotent radical is the largest connected normal unipotent subgroup. The existence of a complement is Levi's theorem, Mostow's in characteristic zero: the rational representations of a reductive group are completely reducible, which produces an $R_u(G)$-stable complement to the extension, and the conjugacy of the complements is the standard uniqueness statement. In characteristic $p$ the splitting requires the separability of the quotient, which holds over a perfect field for reduced groups. $\square$

**Theorem.** For a connected reductive group $G$ over an algebraically closed field, the parabolic subgroups containing a fixed Borel $B$ correspond bijectively to the subsets of the set of simple roots: the parabolic $P_J$ attached to $J$ is generated by $B$ and the root subgroups $U_{-\alpha}$ with $\alpha \in J$, and $P_J$ is a proper subgroup exactly when $J \neq S$. The maximal proper parabolics are the $P_{S \setminus \{\alpha\}}$, one for each simple root.

*Proof sketch.* A parabolic contains $B$, hence is determined by the root subgroups it contains together with $B$; the closed subgroups containing $B$ are exactly the $P_J$, by the classification of the subgroups containing a Borel and the generation of $G$ by the $U_{\pm\alpha}$, and the correspondence with the subsets of the simple roots is the standard one. $\square$

### The Bruhat Decomposition

**Theorem (Bruhat decomposition).** Let $G$ be a connected reductive group over an algebraically closed field, $B$ a Borel subgroup and $T \subseteq B$ a maximal torus with Weyl group $W = N_G(T)/T$. Then

$$
G = \bigsqcup_{w \in W} B w B,
$$

the union is disjoint, each $BwB$ is a locally closed subvariety of dimension $\ell(w) + \dim B$ with $\ell$ the length function of *Coxeter Groups*, and the closure is

$$
\overline{B w B} = \bigsqcup_{v \leq w} B v B,
$$

where $\leq$ is the Bruhat order on $W$ determined by the length and the reflections.

*Proof sketch.* The inclusion $BwB \subseteq BWB$ and the double coset decomposition follow from the generation of $G$ by $B$ and the root subgroups $U_\alpha$: every element is a product of elements of $B$ and the $U_\alpha$, and the relations of the rank-one subgroups $SL_2$ move the resulting word into a normal form indexed by $W$, which is the content of the exchange condition for Coxeter groups quoted from *Coxeter Groups*. The dimension statement is computed from the root subgroups not in $B$ together with the one-dimensional groups $U_\alpha$ with $\alpha$ a negative root not in the stabiliser of $w$; the count of these is exactly $\ell(w)$, and the closure statement is the standard cell closure for the resulting cell decomposition. $\square$

**Corollary.** The quotient $G/B$ is the disjoint union of the cells $BwB/B$ of dimension $\ell(w)$, so it has a cell decomposition with one cell for each element of $W$, and $\sum_{w\in W} t^{\ell(w)}$ is its Poincaré polynomial in the sense of the count of cells by dimension. The number of cells is $|W|$, which for $G = GL_n$ is $n!$.

**Example.** For $G = GL_n$ with $B = B_n$ and $T = T_n$, $W = S_n$ and the length $\ell(w)$ is the number of inversions of the permutation $w$. The cell $BwB$ has dimension $\ell(w) + n(n+1)/2$, and the cells of $G/B$ have dimensions the inversion numbers; for $n = 3$ the multiplicities of the inversion numbers $0,1,2,3$ are $1,2,2,1$, and for $n = 4$ the multiplicities of $0,\ldots,6$ are $1,3,5,6,5,3,1$. These are the Mahonian numbers, they sum to $n!$, and the verification for $n \leq 5$ gives the totals $1,2,6,24,120$ recorded above.

## Reductive and Semisimple Groups

### Definitions and the Structure Theorem

**Definition.** A linear algebraic group $G$ is **reductive** if $R_u(G) = 1$, that is, if it has no nontrivial connected closed normal unipotent subgroup; a connected group is **semisimple** if in addition $R(G) = 1$, that is, if in addition it has no nontrivial connected closed normal solvable subgroup. By convention a semisimple group is connected, and then it equals its derived subgroup and has finite centre.

**Theorem.** Let $G$ be a connected reductive group. Then its centre $Z(G)$ is a diagonalisable group, of the form $S \times A$ with $S$ a torus and $A$ finite, and the derived subgroup $[G,G]$ is semisimple; moreover

$$
G = Z(G)^\circ \cdot [G,G]
$$

with $Z(G)^\circ \cap [G,G]$ finite, and $\dim G = \dim Z(G)^\circ + \dim [G,G]$.

*Proof sketch.* The centre of a reductive group is diagonalisable because its action on the faithful representation is a direct sum of characters; the derived subgroup is semisimple because it is connected and reductive with finite centre, and the product statement is the standard decomposition of a reductive group into its central torus and its semisimple part. $\square$

**Example.** $GL_n$ is reductive with centre $\mathbb{G}_m$ (scalar matrices), derived subgroup $SL_n$, and $\dim GL_n = 1 + (n^2-1) = n^2$. The group $B_n$ is not reductive for $n \geq 2$ because $U_n$ is a nontrivial connected normal unipotent subgroup. A finite group is reductive, with trivial unipotent radical and trivial radical; it is not semisimple when it is nontrivial, because a semisimple group is connected by convention and the identity component of a nontrivial finite group is trivial.

### Classification by Root Data

**Theorem (classification of reductive groups).** Over an algebraically closed field, connected reductive groups are classified up to isomorphism by their reduced root data; the semisimple ones correspond to the semisimple root data, that is, to the root systems of *Root Systems and Classification*, and the simple ones to the connected Dynkin diagrams $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$. For a fixed root system, the simply connected group and the adjoint group are the two extreme members of the isogeny class, and the intermediate members correspond to the subgroups of the centre of the simply connected group containing the kernel of the simply connected to adjoint isogeny.

*Proof sketch.* The classification is Chevalley's theorem quoted above; the determination of the isogeny class by the lattices $X^* \supseteq \mathbb{Z}\Phi$ and $X_* \supseteq \mathbb{Z}\Phi^\vee$ is the lattice-theoretic part, and the correspondence with the subgroups of the centre is the standard computation of the fundamental group of a semisimple group. $\square$

**Example.** For the root system $A_{n-1}$ the simply connected group is $SL_n$ and the adjoint group is $PGL_n = GL_n/\mathbb{G}_m$, with centre $\mathbb{Z}/n\mathbb{Z}$ in the simply connected case; the intermediate groups are $SL_n/\mu_d$ for divisors $d$ of $n$, one for each subgroup of $\mathbb{Z}/n\mathbb{Z}$. This is the combinatorial origin of the finite groups of Lie type, whose abstract-group theory is that of *Finite Simple Groups of Lie Type* of Part I.

## Forms over a General Field

### Split, Quasisplit and Anisotropic Groups

**Definition.** Let $G$ be a linear algebraic group over $k$ and let $T$ be a maximal torus of $G$ over $k$. Write $T_{\mathrm{split}}$ for the largest split subtorus of $T$, that is, the largest subtorus isomorphic over $k$ to a product of copies of $\mathbb{G}_m$, and let $k\text{-rank}(G) = \dim T_{\mathrm{split}}$; this is the **$k$-rank** of $G$ and is independent of the choices. The group $G$ is **split** over $k$ if some maximal torus is split over $k$, **quasisplit** if it has a Borel subgroup defined over $k$, and **anisotropic** if its $k$-rank is zero, equivalently if it has no nontrivial split torus and no nontrivial $k$-character.

**Example.** $\mathbb{G}_a$ and $\mathbb{G}_m$ are split over every field; a split torus $\mathbb{G}_m^r$ has $k$-rank $r$. The norm-one torus

$$
T = \{z \in \mathbb{C}^\times : z\bar z = 1\},
$$

with $\bar z$ the complex conjugate, is a one-dimensional torus over $\mathbb{R}$ with $T(\mathbb{R}) = U(1)$ the circle group; its complexification is $\mathbb{G}_m$ over $\mathbb{C}$, so $T$ becomes split after a quadratic extension, but $T$ contains no nontrivial split subtorus over $\mathbb{R}$, because its real points are compact and a split torus over $\mathbb{R}$ has real points $\mathbb{R}^\times$ and is non-compact. Thus $T$ is anisotropic of $\mathbb{R}$-rank zero, and its character lattice is $X^*(T) \cong \mathbb{Z}$ with the nontrivial Galois action multiplying the generator by $-1$. The analogous group $SO(q)$ for a positive definite quadratic form over $\mathbb{R}$ is anisotropic, while $SO(q)$ for an indefinite form of signature $(p,q)$ has $\mathbb{R}$-rank $\min(p,q)$.

**Theorem (Weyl).** A connected reductive group over $\mathbb{R}$ is anisotropic if and only if its group of real points is compact.

*Proof sketch.* If $G(\mathbb{R})$ is compact then it contains no subgroup isomorphic to $\mathbb{R}^\times$, which is the group of real points of a split torus, so the $\mathbb{R}$-rank is zero. Conversely, an anisotropic reductive group has a compact real form, by the classification of the real forms of a complex reductive group; the statement is quoted as standard. $\square$

### The Galois Action on the Root Datum

**Definition.** Let $G$ be a connected reductive group over $k$ and choose a maximal torus $T$ of $G$ that is split over a separable closure $k^s$. The absolute Galois group $\Gamma_k = \operatorname{Gal}(k^s/k)$ acts on $X^*(T)$ and on $X_*(T)$ through its action on $k^s$-points, preserving the pairing, and it permutes the root system: $\gamma(\Phi) = \Phi$ and $\gamma(\Phi^\vee) = \Phi^\vee$ for every $\gamma \in \Gamma_k$. The resulting action is the **Galois action on the root datum**, and the pair (root datum, $\Gamma_k$-action) is the arithmetic invariant of the group.

**Theorem (Tits).** Over $k$, connected reductive groups with a given geometric root datum are classified up to isomorphism by the continuous actions of $\Gamma_k$ on that root datum, together with the splitting data of the isogeny type; a group is **split** exactly when the action is trivial, and **quasisplit** exactly when the action fixes a Borel subgroup. The $k$-forms of a fixed split group are classified by a Galois cohomology set $H^1$, whose construction is the subject, below this category.

*Proof sketch.* The action of $\Gamma_k$ on the root datum is functorial, and the reconstruction of the group from the action is the Galois descent of the split form: the group over $k^s$ with its $\Gamma_k$-equivariant structure descends to $k$, and the descent data are the action. The classification statement is Tits' theorem, quoted from the literature; the cohomological interpretation of the forms is the standard identification of descent data with a cocycle class. $\square$

### The $k$-Rank and the $k$-Parabolics

**Definition.** A **$k$-parabolic subgroup** of $G$ is a parabolic subgroup defined over $k$; a **$k$-Borel** is a Borel subgroup defined over $k$.

**Theorem.** Let $G$ be a connected reductive group over $k$. Then $G$ has a $k$-Borel if and only if $G$ is quasisplit, and $G$ has a proper $k$-parabolic subgroup if and only if $k\text{-rank}(G) > 0$, equivalently if and only if $G$ is not anisotropic.

*Proof sketch.* A $k$-parabolic contains a maximal $k$-split torus, and a nontrivial $k$-split torus produces a proper $k$-parabolic by the standard construction from the root system: the subgroup generated by the centraliser of the split torus and the root subgroups with positive value of some character is defined over $k$ and proper. Conversely, if $G$ is anisotropic it has no nontrivial split torus, and a proper $k$-parabolic would produce one, since the unipotent radical direction is acted on nontrivially by a split torus. The statement is the theorem of Borel and Tits, quoted as standard. $\square$

**Example.** For $k = \mathbb{R}$ the group $SL_2(\mathbb{R})$ is split with $\mathbb{R}$-rank one and has the upper triangular subgroup as a proper $\mathbb{R}$-parabolic; the anisotropic torus $U(1)$ has rank zero and no proper $\mathbb{R}$-parabolic. For $k = \mathbb{Q}$ the group $SU(q)$ of a positive definite Hermitian form over an imaginary quadratic field is anisotropic and has no proper $\mathbb{Q}$-parabolic; the $\mathbb{Q}$-rank is the parameter that measures the cusps of the arithmetic quotients.

## Summary

A linear algebraic group over $k$ is a closed subgroup of $GL_n$ defined by polynomial equations; the Zariski topology has the polynomial zero sets as closed sets, is Noetherian and quasicompact, and is not Hausdorff or metrisable. The group operations are polynomial and hence continuous, so a linear algebraic group is a topological group, and $GL_n$ has coordinate ring $k[x_{ij}, d^{-1}]$ of dimension $n^2$. The identity component $G^\circ$ is a closed normal subgroup of finite index, the components are its cosets, the component group $G/G^\circ$ is finite and can be any finite group, and connectedness coincides with irreducibility. The basic groups are $\mathbb{G}_a$ and $\mathbb{G}_m$, the classical groups and the triangular groups; a unipotent group is nilpotent and a connected solvable group is triangularisable by Lie–Kolch, so a Borel subgroup is a maximal connected solvable subgroup, all Borels are conjugate, and a parabolic is a closed subgroup containing a Borel. A torus is a product of copies of $\mathbb{G}_m$ over $\bar k$, its characters $X^*(T)$ and cocharacters $X_*(T)$ are dual lattices, and the weights of a representation are the characters that occur. The roots of a reductive group are the nontrivial characters occurring on the root subgroups, the root datum $(X^*,\Phi,X_*,\Phi^\vee)$ classifies the group over an algebraically closed field by Chevalley's theorem, the Weyl group acts by the reflections $s_\alpha$, and the Bruhat decomposition $G = \bigsqcup_{w\in W} BwB$ exhibits the cells of $G/B$ with dimensions the length function. Over a general field the Galois group acts on the root datum, and split, quasisplit and anisotropic groups are separated by the $k$-rank and the existence of $k$-parabolics. The scheme-theoretic and cohomological refinements are the subject , below this category .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $\bar k$, $k^s$ | Base field, its algebraic closure, its separable closure |
| $\mathbb{A}^n_k$ | Affine $n$-space over $k$ |
| $V(\mathfrak{a})$, $D(f)$ | Zero set of an ideal, principal open set |
| $k[X]$ | Coordinate ring of an affine variety $X$ |
| $GL_n(k)$, $SL_n(k)$ | General and special linear groups over $k$ |
| $\mathbb{G}_a$, $\mathbb{G}_m$ | Additive group $(k,+)$ and multiplicative group $(k^\times,\cdot)$ |
| $T_n$, $B_n$, $U_n$ | Diagonal, upper triangular and upper unitriangular subgroups of $GL_n$ |
| $G^\circ$, $G/G^\circ$ | Identity component; finite component group |
| $R(G)$, $R_u(G)$ | Radical and unipotent radical |
| $Z(G)$ | Centre of $G$ |
| $T$, $X^*(T)$, $X_*(T)$ | Torus, character group, cocharacter group |
| $\langle\chi,\lambda\rangle$ | Pairing $X^*(T)\times X_*(T)\to\mathbb{Z}$, perfect when $T$ is split |
| $V_\chi$ | Weight space of a representation |
| $\Phi$, $\Phi^\vee$ | Root system and coroot system of $(G,T)$ |
| $U_\alpha$, $\alpha^\vee$ | Root subgroup and coroot of a root $\alpha$ |
| $W = N_G(T)/T$ | Weyl group |
| $s_\alpha$, $\ell(w)$ | Reflection associated to $\alpha$; length on $W$ |
| $(X^*,\Phi,X_*,\Phi^\vee)$ | Root datum |
| $B$, $P$, $R_u(P)$ | Borel subgroup, parabolic subgroup, its unipotent radical |
| $k\text{-rank}(G)$ | Dimension of a maximal $k$-split torus |
| $\Gamma_k$ | Absolute Galois group of $k$ |



## Further Reading

- Armand Borel, *Linear Algebraic Groups* (2nd edition, Springer, 1991), for the Zariski topology, the structure theory, Borel and parabolic subgroups and the classification.
- Tonny A. Springer, *Linear Algebraic Groups* (2nd edition, Birkhäuser, 1998), for the root datum, the classification by root data and the structure of reductive groups.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the foundational treatment of connectedness, unipotent and solvable groups and the Borel fixed point theorem.
- Michel Demazure and Pierre Gabriel, *Groupes algébriques* (Masson, 1970), for the root datum and the classification of reductive groups.
- Armand Borel and Jacques Tits, "Groupes réductifs", *Publications mathématiques de l'IHÉS* 27 (1965), 55–150, for the Galois action on the root datum, the $k$-rank and the existence of $k$-parabolics.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (3rd edition, Springer, 2013), for affine varieties, the Zariski topology and dimension.
