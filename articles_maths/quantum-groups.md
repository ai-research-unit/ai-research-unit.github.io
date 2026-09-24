
# __Quantum Groups__

## Introduction

A quantum group, in the algebraic sense used here, is a Hopf algebra obtained by deforming the algebra of functions on a group, or the enveloping algebra of a Lie algebra, by a parameter $q$ in such a way that at $q = 1$ the undeformed object is recovered. The deformation is a change of the multiplication, not of the underlying space: the quantised enveloping algebra $U_q(\mathfrak{g})$ has the same basis of ordered monomials in the Chevalley generators as $U(\mathfrak{g})$, but the relations between the generators acquire coefficients that are rational functions of $q$, and the deformation of the Hopf algebra of a group produces non-commutative coordinate algebras such as the quantum plane.

This article is the sixth of the category. It follows *Hopf Algebras*, whose definitions of coalgebra, antipode and integral it assumes, and it precedeswhich is the general theory of which quantisation by a parameter is the algebraic model. It is the algebraic theory: the quantised enveloping algebras, the quantised coordinate algebras, the quasitriangular structure and the universal $\mathcal{R}$-matrix, the ribbon and modular structures, and the special behaviour at roots of unity. The locally compact quantum groups of operator algebra theory, with their Haar weights and their norms, are a different subject and belong to a later Part; they are named once, at the point where the two notions are closest, and deferred.

The article does not assume the classification of Lie algebras or root data beyond what is written: the semisimple Lie algebra $\mathfrak{g}$, its Cartan decomposition, its simple roots and its Cartan matrix are used, and they are the constructions andwhich are read as standard background for the definition. Where the deformation needs the Weyl group or the invariant pairing on the weight lattice, the algebra is stated and the form-theoretic statement is deferred to Part II.

Throughout, $k$ is a field, $q \in k^\times$ is the deformation parameter, and we write

$$
\{n\}_q = \frac{q^n - q^{-n}}{q - q^{-1}}, \qquad [n]_q = \frac{q^n - 1}{q - 1}, \qquad [n]_q! = \prod_{m=1}^{n}[m]_q
$$

for the Gaussian integers and factorial. These are elements of $k$; when $q$ is a root of unity the elements $[n]_q$ may vanish, and the corresponding degeneracies are the subject of the theory at roots of unity.

## Deformation of the Enveloping Algebra

### The quantised enveloping algebra

**Definition.** Let $\mathfrak{g}$ be a semisimple Lie algebra over $k$ with Cartan matrix $A = (a_{ij})$, simple roots $\alpha_1,\dots,\alpha_r$, Chevalley generators $e_i, f_i, h_i$ and $d_i = \langle\alpha_i,\alpha_i\rangle/2$. Assume that $q$ is not a root of unity and that $k$ contains the elements $q^{d_i}$. The **quantised enveloping algebra** $U_q(\mathfrak{g})$ is the associative $k$-algebra with generators

$$
E_i,\ F_i,\ K_i^{\pm 1} \qquad (i = 1,\dots,r)
$$

and relations

$$
K_iK_j = K_jK_i, \qquad K_i K_i^{-1} = 1, \qquad K_iE_jK_i^{-1} = q^{d_i a_{ij}}E_j, \qquad K_iF_jK_i^{-1} = q^{-d_ia_{ij}}F_j ,
$$

$$
E_iF_j - F_jE_i = \delta_{ij}\,\frac{K_i - K_i^{-1}}{q^{d_i} - q^{-d_i}} ,
$$

together with the **quantum Serre relations**

$$
\sum_{s=0}^{1-a_{ij}} (-1)^s \begin{bmatrix} 1-a_{ij} \\ s\end{bmatrix}_{q^{d_i}} E_i^{\,1-a_{ij}-s}E_jE_i^{\,s} = 0 \qquad (i \neq j),
$$

and the same relations with $E$ replaced by $F$. Here $\begin{bmatrix} n \\ s\end{bmatrix}_{q}$ is the Gaussian binomial coefficient

$$
\begin{bmatrix} n \\ s\end{bmatrix}_{q} = \frac{[n]_q!}{[s]_q!\,[n-s]_q!} .
$$

**Theorem (standard).** The algebra $U_q(\mathfrak{g})$ is a Hopf algebra with

$$
\Delta(K_i) = K_i\otimes K_i, \quad \Delta(E_i) = E_i\otimes K_i + 1\otimes E_i, \quad \Delta(F_i) = F_i\otimes 1 + K_i^{-1}\otimes F_i,
$$

$$
\varepsilon(K_i) = 1, \quad \varepsilon(E_i) = \varepsilon(F_i) = 0, \qquad S(K_i) = K_i^{-1}, \quad S(E_i) = -E_iK_i^{-1}, \quad S(F_i) = -K_iF_i .
$$

When $q = 1$ the algebra $U_q(\mathfrak{g})$ degenerates to the enveloping algebra $U(\mathfrak{g})$, with $K_i = 1$ and $E_i, F_i$ the Chevalley generators; the Hopf structure degenerates to the primitive coproduct of *Hopf Algebras*.

*Proof (outline).* The coproduct is checked on the defining relations: for the $E$-$F$ relation, $\Delta(E_i)\Delta(F_i) - \Delta(F_i)\Delta(E_i)$ computes to $K_i\otimes K_i - K_i^{-1}\otimes K_i^{-1}$ divided by $q^{d_i}-q^{-d_i}$ using $\Delta(K_i^{\pm1}) = K_i^{\pm1}\otimes K_i^{\pm1}$ and the commutation of $K_i^{\pm 1}$ with the corresponding $F_i$, which is exactly $\Delta$ of the right-hand side. The Serre relations are preserved by the coproduct because it is an algebra homomorphism and the quantum binomial coefficients satisfy the $q$-Pascal identity. The antipode axioms are verified directly on the generators. $\square$

### Triangular decomposition and the PBW theorem

**Theorem (PBW for $U_q(\mathfrak{g})$, standard).** The monomials

$$
F_1^{a_1}\cdots F_r^{a_r}\,K_1^{b_1}\cdots K_r^{b_r}\,E_1^{c_1}\cdots E_r^{c_r} \qquad (a_i,c_i \in \mathbb{Z}_{\geq 0},\ b_i \in \mathbb{Z})
$$

form a $k$-basis of $U_q(\mathfrak{g})$ when $q$ is not a root of unity. Hence $U_q(\mathfrak{g}) \cong U_q(\mathfrak{n}^-)\otimes_k k[K_1^{\pm1},\dots,K_r^{\pm1}]\otimes_k U_q(\mathfrak{n}^+)$ as vector spaces, where $U_q(\mathfrak{n}^\pm)$ are the subalgebras generated by the $F_i$ and by the $E_i$.

The theorem is due to Drinfeld and Jimbo, and it is the $q$-analogue of the Poincaré–Birkhoff–Witt theorem. The basis statement is what makes $U_q(\mathfrak{g})$ finite-dimensional in each weight space and lets representation theory proceed as in the classical case.

**Example ($\mathfrak{g} = \mathfrak{sl}_2$).** Here $r = 1$, $A = (2)$, and $U_q(\mathfrak{sl}_2)$ is generated by $E, F, K^{\pm1}$ with

$$
KEK^{-1} = q^2E, \qquad KFK^{-1} = q^{-2}F, \qquad EF - FE = \frac{K - K^{-1}}{q - q^{-1}} .
$$

The coproduct is $\Delta(E) = E\otimes K + 1\otimes E$, $\Delta(F) = F\otimes 1 + K^{-1}\otimes F$, and the Serre relations are vacuous. Writing $K = q^H$, the relations read $[H,E] = 2E$, $[H,F] = -2F$, $[E,F] = [H]_{q}$, where $[H]_q = (q^H - q^{-H})/(q-q^{-1})$; as $q\to1$ these become the relations of $\mathfrak{sl}_2$. The **finite-dimensional irreducible representations** are the modules $V_n$ of dimension $n+1$ spanned by $v_0,\dots,v_n$ with

$$
K\cdot v_m = q^{n-2m}v_m, \qquad F\cdot v_m = v_{m+1}, \qquad E\cdot v_m = [n-m+1]_q[m]_q\, v_{m-1} ,
$$

the $q$-analogue of the $(n+1)$-dimensional representation of $\mathfrak{sl}_2$; the factor $[n-m+1]_q[m]_q$ is the $q$-integer replacing the classical $m(n-m+1)$.

## Quasitriangularity and the Universal $\mathcal{R}$-Matrix

### The $\mathcal{R}$-matrix

**Definition.** A Hopf algebra $H$ is **quasitriangular** if there is an invertible element $\mathcal{R} = \sum_i s_i\otimes t_i \in H\otimes_k H$ such that

$$
\Delta^{\mathrm{op}}(h) = \mathcal{R}\,\Delta(h)\,\mathcal{R}^{-1} \quad \text{for all } h \in H, \qquad (\Delta\otimes\mathrm{id})(\mathcal{R}) = \mathcal{R}_{13}\mathcal{R}_{23}, \qquad (\mathrm{id}\otimes\Delta)(\mathcal{R}) = \mathcal{R}_{13}\mathcal{R}_{12},
$$

where $\Delta^{\mathrm{op}} = \tau\circ\Delta$ and $\mathcal{R}_{12} = \sum_i s_i\otimes t_i\otimes 1$, $\mathcal{R}_{13} = \sum_i s_i\otimes1\otimes t_i$, $\mathcal{R}_{23} = \sum_i 1\otimes s_i\otimes t_i$. The element $\mathcal{R}$ is the **universal $\mathcal{R}$-matrix**. A quasitriangular Hopf algebra is **triangular** if in addition $\mathcal{R}^{-1} = \mathcal{R}_{21}$, where $\mathcal{R}_{21} = \tau(\mathcal{R})$.

**Theorem (Drinfeld, standard).** $U_q(\mathfrak{g})$ is quasitriangular; the $\mathcal{R}$-matrix is

$$
\mathcal{R} = q^{\sum_{i,j} (A^{-1})_{ij}\,H_i\otimes H_j}\ \prod_{\beta > 0} \exp_{q_\beta}\!\bigl((q_\beta - q_\beta^{-1})E_\beta\otimes F_\beta\bigr),
$$

where $H_i = d_i^{-1}\log_q K_i$, the product runs over the positive roots $\beta$ in a fixed order, $E_\beta, F_\beta$ are the root vectors, $q_\beta = q^{d_\beta}$, and $\exp_{q}(x) = \sum_{n\geq0} q^{n(n-1)/2}x^n/[n]_q!$ is the $q$-exponential.

The theorem is the deepest structural result of the undeformed theory at generic $q$; the existence of $\mathcal{R}$ is what makes $U_q(\mathfrak{g})$ an algebraic analogue of a compact group with a Haar integral and gives its representation category the structure of a braided monoidal category.

### The braiding and the Yang–Baxter equation

**Proposition.** Let $H$ be quasitriangular with $\mathcal{R}$-matrix $\mathcal{R}$. For left $H$-modules $M, N$, the map

$$
c_{M,N} : M\otimes_k N \to N\otimes_k M, \qquad c_{M,N}(m\otimes n) = \tau\bigl(\mathcal{R}\cdot(m\otimes n)\bigr),
$$

is a natural isomorphism of $H$-modules, and it satisfies the **Yang–Baxter equation**

$$
(c_{N,P}\otimes\mathrm{id}_M)(\mathrm{id}_N\otimes c_{M,P})(c_{M,N}\otimes\mathrm{id}_P) = (\mathrm{id}_P\otimes c_{M,N})(c_{M,P}\otimes\mathrm{id}_N)(\mathrm{id}_M\otimes c_{N,P})
$$

on $M\otimes_k N\otimes_k P$. Moreover $c_{N,M}\circ c_{M,N} = \mathrm{id}$ exactly when $H$ is triangular.

*Proof.* The naturality and $H$-linearity of $c_{M,N}$ are the content of the first quasitriangularity axiom: $\mathcal{R}\Delta(h) = \Delta^{\mathrm{op}}(h)\mathcal{R}$ means that moving $\mathcal{R}$ past the action of $h$ is the same as applying the coproduct with the factors transposed. The Yang–Baxter equation is the second and third axioms read on a triple tensor product: both sides are the two ways of applying $\mathcal{R}_{12}\mathcal{R}_{13}\mathcal{R}_{23}$. The stated criterion for the inverse is the computation $c_{N,M}\circ c_{M,N} = \tau(\mathcal{R}_{21}\mathcal{R})$ and the triangularity condition $\mathcal{R}_{21} = \mathcal{R}^{-1}$. $\square$

The map $c$ makes the category of $H$-modules **braided monoidal**, and the Yang–Baxter equation is what allows the construction of knot invariants from representations, the classical application of quantum groups to low-dimensional topology, which belongs to Part II's *Algebraic Topology*.

### Ribbon elements and twists

**Definition.** A quasitriangular Hopf algebra $H$ has a **ribbon element** if there is a central element $\theta$ with $S(\theta) = \theta$, $\varepsilon(\theta)=1$ and $\Delta(\theta) = (\mathcal{R}_{21}\mathcal{R})^{-1}(\theta\otimes\theta)$; a **modular** Hopf algebra is a ribbon Hopf algebra with a **twist** $v$ satisfying $v^2 = \theta^{-1}u$ where $u = \sum_i S(t_i)s_i$.

The modular structure is the algebraic input of the Reshetikhin–Turaev invariants and of the modular tensor categories; the topological constructions belong to Part II and the category-theoretic ones to *Monoidal Categories*, while the Hopf-algebraic data is what is produced here.

## Quantised Coordinate Algebras

**Definition.** The **quantum group** $\operatorname{SL}_q(2)$ is the algebra $k_q[\operatorname{SL}_2]$ with generators $a, b, c, d$ and relations

$$
ab = q\,ba, \qquad ac = q\,ca, \qquad bd = q\,db, \qquad cd = q\,dc, \qquad bc = cb, \qquad ad - da = (q - q^{-1})bc,
$$

together with $ad - q\,bc = 1$. It is a Hopf algebra with

$$
\Delta\begin{pmatrix} a & b \\ c & d\end{pmatrix} = \begin{pmatrix} a & b\\ c & d\end{pmatrix}\dot\otimes \begin{pmatrix} a & b\\ c & d\end{pmatrix}, \qquad \varepsilon\begin{pmatrix}a&b\\c&d\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix},
$$

where the matrix product uses the tensor product of the entries, and with $S$ given by

$$
S\begin{pmatrix}a&b\\c&d\end{pmatrix} = \begin{pmatrix} d & -q^{-1}b \\ -qc & a\end{pmatrix},
$$

so that the product of the matrix with its antipode image is the identity. This is the deformation of the coordinate Hopf algebra of the preceding article, and it is a flat deformation: at $q=1$ the relations become the commutative relations of the polynomial ring $k[a,b,c,d]/(ad-bc-1)$.

**Definition.** The **quantum plane** is the algebra $k_q[x,y]$ with the single relation

$$
yx = q\,xy ,
$$

with the comultiplication declaring $x,y$ primitive-like under the group-like element $K$ of the preceding article; it is the simplest deformation of a polynomial algebra and the basic example of a **module algebra** over a Hopf algebra.

**Definition (Drinfeld double).** Let $\mathfrak{b}$ be a finite-dimensional Hopf algebra with dual $\mathfrak{b}^*$, and let $\mathfrak{b}^*$ act on $\mathfrak{b}$ and $\mathfrak{b}$ act on $\mathfrak{b}^*$ by the transposed coadjoint actions. The **Drinfeld double** $D(\mathfrak{b})$ is the vector space $\mathfrak{b}^*\otimes_k \mathfrak{b}$ with the multiplication determined by those mutual actions, and it is a quasitriangular Hopf algebra; the $\mathcal{R}$-matrix is $\sum_i f_i\otimes e_i$ for dual bases $\{f_i\}$ of $\mathfrak{b}^*$ and $\{e_i\}$ of $\mathfrak{b}$. The double gives a systematic source of quasitriangular quantum groups, and the Borel subalgebra of $U_q(\mathfrak{sl}_2)$ is the standard example from which $U_q(\mathfrak{sl}_2)$ is recovered as a quotient of a Drinfeld double.

## Representations and the Crystal Limit

**Definition.** Let $q$ be not a root of unity. The category $\operatorname{Rep}(U_q(\mathfrak{g}))$ of finite-dimensional $U_q(\mathfrak{g})$-modules of **type 1** — those on which $K_i$ acts with eigenvalues in $q^{\mathbb{Z}}$ — is a braided monoidal category, and for $\mathfrak{g}$ semisimple it is semisimple with the same simple objects as $\operatorname{Rep}(\mathfrak{g})$: the irreducible modules $V_\lambda$ are parametrised by dominant integral weights $\lambda$, and the Weyl character formula has a $q$-analogue.

**Theorem (standard).** For $q$ not a root of unity, every finite-dimensional $U_q(\mathfrak{g})$-module is completely reducible, and the multiplicity of the irreducible module $V_\lambda$ in the tensor product $V_\mu\otimes_k V_\nu$ is the same Littlewood–Richardson coefficient as in the classical case. Hence $U_q(\mathfrak{g})$ is a flat deformation of the enveloping algebra as far as its representation theory is concerned.

**Theorem (Lusztig, standard).** There is a $\mathbb{Z}[q,q^{-1}]$-form of $U_q(\mathfrak{g})$, the **integral form** $U_{\mathbb{Z}}(\mathfrak{g})$, and a **crystal basis** $\mathcal{B}$ of each integrable module, such that the structure constants of the basis are in $\mathbb{Z}_{\geq0}[q,q^{-1}]$ and specialise at $q = 0$ to the combinatorics of **crystals**, the algebraic model of the Young tableaux and the Weyl group action. The crystal limit $q\to0$ replaces the braiding by a combinatorial rule and is the mechanism by which the representation theory of quantum groups recovers the combinatorics and of the symmetric group.

The crystal and canonical basis theory is the source of the Kazhdan–Lusztig theory that appears and of the Macdonald polynomial theory; the present article records only that the crystal basis exists and that its structure constants are integral.

## Roots of Unity and Small Quantum Groups

**Definition.** If $q$ is a primitive $\ell$-th root of unity, then $q^d = 1$ for some $d$, and the elements $E_i^{d}, F_i^{d}, K_i^{d}$ become central in $U_q(\mathfrak{g})$; the **small quantum group** $u_q(\mathfrak{g})$ is the finite-dimensional Hopf algebra obtained as the quotient of $U_q(\mathfrak{g})$ by the ideal generated by those central elements, with $E_i^{d} = F_i^d = 0$ and $K_i^{d} = 1$.

**Theorem (standard, Lusztig).** For $\ell$ odd and coprime to the Coxeter number, the small quantum group $u_q(\mathfrak{g})$ is a finite-dimensional Hopf algebra with a one-dimensional space of integrals in the sense of *Hopf Algebras*, it is a **modular** Hopf algebra, and its representation category is a modular tensor category whose fusion rules are the Verlinde formula applied to the affine Lie algebra $\widehat{\mathfrak{g}}$ at level $\ell - h^\vee$.

At a root of unity the deformation fails to be flat in the naive sense: $U_q(\mathfrak{g})$ acquires a large centre, its category of finite-dimensional modules is no longer semisimple, and the representation theory has a block decomposition analogous to the modular representation theory of finite groups, which is the subject andin the last category of this Part. This is the point of contact between the quantum groups and the modular representation theory; it is the Frobenius twist and the Steinberg tensor product theorem that make the analogy precise in the classical case.

## Formal Deformations and the Link with Quantisation

**Definition.** Let $A$ be a $k$-algebra. A **formal deformation** of $A$ is a $k[[h]]$-algebra $A_h$, topologically free with $A_h/hA_h \cong A$, together with an isomorphism of $k[[h]]$-modules $A_h \cong A[[h]]$; equivalently, $A_h$ is the $k[[h]]$-module $A[[h]]$ equipped with a multiplication

$$
a * b = ab + h\,\mu_1(a,b) + h^2\mu_2(a,b) + \cdots
$$

whose coefficients $\mu_n : A\times A \to A$ are $k$-bilinear and which is associative on the nose. Writing $h$ for the deformation parameter and $q = \exp h = 1 + h + h^2/2 + \cdots$ recovers the quantum groups of this article: $U_h(\mathfrak{g})$ is a formal deformation of $U(\mathfrak{g})$ by a Hopf algebra over $k[[h]]$, and its specialisation at $q$ is $U_q(\mathfrak{g})$.

**Theorem (standard).** Let $A$ be an associative $k$-algebra. Formal deformations of $A$ are classified, to first order, by the second Hochschild cohomology group $H^2(A,A)$: the associativity of $*$ forces the class of the first-order term $\mu_1$ to be a $2$-cocycle, and a change of the identification $A_h \cong A[[h]]$ changes its class by a coboundary. The first-order term of the deformation $U_h(\mathfrak{g})$ of $U(\mathfrak{g})$ is the class of the **Poisson bracket** obtained by symmetrising the Lie bracket, and its vanishing is what makes $U_h(\mathfrak{g})$ a genuine deformation and not a mere change of generators.

The general theory of formal deformations, of the **star product** $f*g$ on the algebra of functions with $\mu_n$ built from a Poisson bracket, and of the Gerstenhaber bracket that controls the higher obstructions, is the subject, which follows this article. The Hochschild cohomology that classifies the deformations is the cohomology of the enveloping algebra $A^{\mathrm{e}}$ of *Separable Algebras*, and it is the subject of the homological articles of a later category of this Part.

**Example (the Moyal-type deformation of the polynomial algebra).** Let $A = k[x_1,\dots,x_n]$ and let $\{\cdot,\cdot\}$ be the constant bracket $\{x_i,x_j\} = \omega_{ij}$ with $\omega$ a skew-symmetric constant matrix. The **Moyal star product**

$$
f * g = \sum_{r\geq0}\frac{1}{r!}\Bigl(\frac{h}{2}\Bigr)^r \sum_{i_1,\dots,i_r,j_1,\dots,j_r}\omega_{i_1j_1}\cdots\omega_{i_rj_r}\ \partial_{i_1}\cdots\partial_{i_r}f\ \partial_{j_1}\cdots\partial_{j_r}g
$$

is an associative deformation of $k[x_1,\dots,x_n]$ whose first-order term is the constant bracket $\{\cdot,\cdot\}$; in the case $n = 2$, $\omega_{12} = 1$ the deformed generators satisfy

$$
x_1 * x_2 - x_2 * x_1 = h ,
$$

the formal form of the canonical commutation relation. This deformation must be distinguished from the quantum plane: for $q = 1 + h$ the relation $yx = q\,xy$ has first-order term $yx - xy = h\,xy$, whose bracket $\{y,x\} = xy$ is the Poisson bracket $xy(\partial_xf\partial_yg - \partial_yf\partial_xg)$ and is therefore not constant. The two deformations of $k[x,y]$ are different, and this is the standard illustration that the first-order term of a formal deformation, not the deformed algebra alone, determines the Poisson structure that is being quantised.

## The Boundary with Operator-Algebraic Quantum Groups

The word *quantum group* is used in a second sense in operator algebra theory. A **compact quantum group** is a unital $C^*$-algebra $A$ with a coassociative unital $*$-homomorphism $\Delta : A \to A\otimes_{\min}A$ satisfying the cancellation conditions, together with a **Haar state**; a **locally compact quantum group** is a von Neumann algebra with a comultiplication and left and right Haar weights. Both notions require the norm, the operator topology and the completion, none of which is available in this Part. The relation between the two theories is that the finite-dimensional and the algebraic quantum groups of this article include the coordinate algebras of the classical groups and their $q$-deformations at the algebraic level, and the operator-algebraic theory adds the analytic completion and the measure-theoretic content. The analytic theory is treated in another Part.

## Summary

A **quantum group**, algebraically, is a Hopf algebra obtained by deforming the enveloping algebra of a semisimple Lie algebra or the coordinate algebra of a group. The **quantised enveloping algebra** $U_q(\mathfrak{g})$ has generators $E_i, F_i, K_i^{\pm1}$ with the relations $K_iE_jK_i^{-1} = q^{d_ia_{ij}}E_j$, $K_iF_jK_i^{-1} = q^{-d_ia_{ij}}F_j$, $E_iF_j - F_jE_i = \delta_{ij}(K_i - K_i^{-1})/(q^{d_i}-q^{-d_i})$ and the quantum Serre relations; it is a Hopf algebra with $\Delta(K_i) = K_i\otimes K_i$, $\Delta(E_i) = E_i\otimes K_i + 1\otimes E_i$, $\Delta(F_i) = F_i\otimes 1 + K_i^{-1}\otimes F_i$, and it has a Poincaré–Birkhoff–Witt basis of ordered monomials when $q$ is not a root of unity, degenerating at $q=1$ to $U(\mathfrak{g})$. For $\mathfrak{sl}_2$ the finite-dimensional irreducibles $V_n$ have basis $v_0,\dots,v_n$ with $Kv_m = q^{n-2m}v_m$ and $Ev_m = [n-m+1]_q[m]_qv_{m-1}$.

$U_q(\mathfrak{g})$ is **quasitriangular**: the universal $\mathcal{R}$-matrix $\mathcal{R} \in H\otimes_k H$ satisfies $\Delta^{\mathrm{op}}(h) = \mathcal{R}\Delta(h)\mathcal{R}^{-1}$ and the two quasitriangularity axioms, and it produces a braiding $c_{M,N}(m\otimes n) = \tau(\mathcal{R}\cdot(m\otimes n))$ on the category of modules that satisfies the **Yang–Baxter equation** and makes the category braided monoidal, triangular exactly when $\mathcal{R}_{21} = \mathcal{R}^{-1}$. Ribbon and modular elements add the data of the Reshetikhin–Turaev theory, whose topological part belongs to Part II. The **quantised coordinate algebras** $\operatorname{SL}_q(2)$ and the **quantum plane** $k_q[x,y]$ with $yx = qxy$ are the deformed function algebras, and the Drinfeld double is the systematic source of quasitriangular quantum groups. For $q$ not a root of unity $U_q(\mathfrak{g})$ is semisimple as a Hopf algebra with the same irreducible modules and the same tensor product multiplicities as $\mathfrak{g}$, and the **crystal basis** at $q=0$ recovers the combinatorial representation theory; for $q$ a root of unity the **small quantum group** $u_q(\mathfrak{g})$ is finite-dimensional and modular, and its non-semisimple representation theory is the quantum analogue of the modular representation theory of finite groups. The operator-algebraic notion of a locally compact quantum group, with its Haar weights and its norms, is a different subject belonging to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | ground field |
| $q$ | deformation parameter, $q \in k^\times$ |
| $[n]_q$, $[n]_q!$ | Gaussian integer and factorial |
| $\begin{bmatrix} n\\ s\end{bmatrix}_q$ | Gaussian binomial coefficient |
| $\mathfrak{g}$ | semisimple Lie algebra, Cartan matrix $A = (a_{ij})$ |
| $e_i, f_i, h_i$ | Chevalley generators of $\mathfrak{g}$ |
| $E_i, F_i, K_i^{\pm1}$ | generators of $U_q(\mathfrak{g})$ |
| $d_i$ | $\langle\alpha_i,\alpha_i\rangle/2$ |
| $U_q(\mathfrak{g})$ | quantised enveloping algebra; Hopf algebra |
| $V_n$ | $(n+1)$-dimensional irreducible $U_q(\mathfrak{sl}_2)$-module |
| $\mathcal{R}$ | universal $\mathcal{R}$-matrix, $H\otimes_k H$ |
| $\mathcal{R}_{12}, \mathcal{R}_{13}, \mathcal{R}_{23}$ | leg notations for $\mathcal{R}$ in $H^{\otimes3}$ |
| $c_{M,N}$ | braiding of the module category |
| $u, \theta, v$ | Drinfeld element, ribbon element, twist |
| $D(\mathfrak{b})$ | Drinfeld double of a Hopf algebra |
| $\operatorname{SL}_q(2)$, $k_q[x,y]$ | quantised coordinate algebra, quantum plane |
| $U_{\mathbb{Z}}(\mathfrak{g})$, $\mathcal{B}$ | integral form, crystal basis |
| $u_q(\mathfrak{g})$ | small quantum group at a root of unity |
| $k[[h]]$, $A_h$, $U_h(\mathfrak{g})$ | formal deformation and its deformation parameter |
| $a*b = ab + \sum_{n\geq1}h^n\mu_n(a,b)$ | deformed product, first-order term $\mu_1$ |
| $\{f,g\}$ | Poisson bracket, the first-order term of $*$ |
| $H^2(A,A)$ | Hochschild cohomology classifying first-order deformations |





## Further Reading

- Vladimir G. Drinfeld, "Quantum groups", *Proceedings of the International Congress of Mathematicians* (Berkeley, 1986), 798–820, for the definition, the $\mathcal{R}$-matrix and the Yang–Baxter equation.
- Michio Jimbo, "A $q$-difference analogue of $U(\mathfrak{g})$ and the Yang–Baxter equation", *Letters in Mathematical Physics* **10** (1985), 63–69, for the quantised enveloping algebras and their representations.
- Christian Kassel, *Quantum Groups* (Springer, 1995), for a systematic Hopf-algebraic treatment.
- Vyjayanthi Chari and Andrew Pressley, *A Guide to Quantum Groups* (Cambridge, 1994), for the representation theory, the braided category and the small quantum groups.
- George Lusztig, *Introduction to Quantum Groups* (Birkhäuser, 1993), for the integral form, the canonical and crystal bases.
- Nicolai Reshetikhin and Vladimir Turaev, "Invariants of 3-manifolds via link polynomials and quantum groups", *Inventiones Mathematicae* **103** (1991), 547–597, for the modular structure and its topological invariants, which are the subject of Part II.
- Jens Carsten Jantzen, *Lectures on Quantum Groups* (American Mathematical Society, 1996), for the theory at roots of unity and the small quantum groups.
