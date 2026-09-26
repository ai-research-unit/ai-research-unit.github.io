
# __Deformation Theory__

## Introduction

A deformation of an algebraic object is a family of objects over a parameter, all specialising to the given one, and the algebraic theory of deformations studies these families when the parameter ring is local and the fibre over the closed point is the object deformed. The leading example is the deformation of an associative $k$-algebra $A$ over the dual numbers $\mathbb{D}'=k[\varepsilon]/(\varepsilon^2)$: a multiplication on $A\otimes_k\mathbb{D}'$ reducing to the multiplication of $A$ modulo $\varepsilon$ is a first-order deformation, and the set of such deformations, up to the isomorphisms that are the identity modulo $\varepsilon$, is described by a cohomology group, $HH^2(A,A)$ in the associative case and $\operatorname{Ext}^1_A(M,M)$ in the case of a module. When one asks instead for deformations over a thicker parameter ring the obstruction to extending a first-order deformation is a class in the next cohomology group, $HH^3(A,A)$ or $\operatorname{Ext}^2_A(M,M)$, and this is the whole content of the theory in the associative case: deformations are the Maurer–Cartan solutions of a differential graded Lie algebra, gauge equivalence is the action of the degree-zero part, and the obstructions are the brackets.

This article develops the deformation functor of an algebra and of a module, first-order deformations and their cohomological description, the Maurer–Cartan equation and the differential graded Lie algebra of Hochschild cochains, gauge equivalence and the versal deformation, the obstruction calculus in degrees two and three, the deformation of a module over a deformed algebra, the rigidity criterion and the examples of the polynomial ring, the matrix algebra and the dual numbers. It follows *Hochschild Homology*, *Cyclic Homology*, *Ext and Tor*, *Derived Categories*, and it prepares the representation-theoretic articles of the category.

Throughout, $k$ is a commutative ring with $1\neq0$ containing a field if a division by $2$ or by factorials is needed, $A$ is an associative $k$-algebra, $M$ an $A$-bimodule, and $HH^{\bullet}(A,M)$ and $\operatorname{Ext}^{\bullet}_A(M,M)$ are those of *Hochschild Homology* and *Ext and Tor*. The parameter rings are the Artinian local $k$-algebras, and their maximal ideals are nilpotent; the word *formal* refers to the inverse limit of the Artinian quotients, an algebraic construction. No topology, distance, norm or completion in the analytic sense occurs. Deformations of algebraic varieties and of sheaves, and the geometric versal deformation, belong to Part II, where they are treated in *Sheaves and Cohomology* and in the articles on algebraic geometry; only the algebra of the deformation functor is developed here.

## Deformations of Algebras

### First-Order Deformations

**Definition.** A **deformation** of $A$ over an Artinian local $k$-algebra $(S,\mathfrak{m})$ with $S/\mathfrak{m}\cong k$ is a flat $S$-algebra $A_S$ with an isomorphism $A_S\otimes_Sk\cong A$ of $k$-algebras. Two deformations are **equivalent** if there is an isomorphism of $S$-algebras inducing the identity on $A$ modulo $\mathfrak{m}$. The **deformation functor** is

$$
\operatorname{Def}_A:R\longmapsto\frac{\{\text{deformations of }A\text{ over }R\}}{\text{equivalence}},
$$

on the category of Artinian local $k$-algebras $R$.

**Definition.** For the **dual numbers** $R=k[\varepsilon]/(\varepsilon^2)$ a deformation over $R$ is an associative $R$-algebra $A_\varepsilon$ with $A_\varepsilon/\varepsilon A_\varepsilon\cong A$, equivalently a bilinear product

$$
a*b=ab+\varepsilon f(a,b)
$$

on $A\otimes_k\mathbb{D}'$ that is associative and reduces to the given product modulo $\varepsilon$. The bilinear form $f:A\times A\to A$ is a **first-order deformation cocycle**, and $f$ satisfies
$$
af(b,c)-f(ab,c)+f(a,bc)-f(a,b)c=0,
$$
which is the cocycle condition for $HH^2(A,A)$ up to sign, and the associativity of $*$ is exactly this condition.

**Theorem.** The first-order deformations of $A$ up to equivalence are in natural bijection with $HH^2(A,A)$, the equivalence being the difference by a Hochschild coboundary. The trivial deformation $a*b=ab$ corresponds to the class $0$.

*Proof.* For each $f$, the associativity of $*$ on $A\otimes\mathbb{D}'$ is equivalent to the cocycle condition on $f$ once the products of the three elements are expanded and the $\varepsilon$-linear terms collected. An equivalence between the deformation given by $f$ and the deformation given by $f'$ is an isomorphism of $\mathbb{D}'$-algebras that is the identity modulo $\varepsilon$, hence of the form $a+\varepsilon g(a)$ for a $k$-linear $g:A\to A$; conjugating the product by it changes $f$ to $f+\partial g$, where $\partial g(a,b)=ag(b)-g(ab)+g(a)b$ is the Hochschild coboundary. Hence the deformations modulo equivalence are the classes in $HH^2(A,A)$. $\square$

**Example.** For the polynomial algebra $A=k[x_1,\dots,x_m]$ the second Hochschild cohomology is, by the Hochschild–Kostant–Rosenberg theorem, the direct sum $HH^2(A,A)\cong\bigoplus_{p+q=2}\Lambda^p\operatorname{Der}_k(A)\otimes_A\Omega^q_{A/k}=\Lambda^2\operatorname{Der}\oplus(\operatorname{Der}\otimes_A\Omega^1)\oplus\Omega^2$ of the bivectors, the derivations twisted by the one-forms, and the two-forms; every bivector $\sum_{i<j}c_{ij}\partial_i\wedge\partial_j$ with $c_{ij}\in A$ gives a first-order deformation by the product
$$
a*b=ab+\varepsilon\sum_{i<j}c_{ij}(\partial_ia\,\partial_jb-\partial_ja\,\partial_ib),
$$
which is the deformation of the polynomial algebra by a Poisson bracket; this is the algebraic form of the deformation quantisation of a Poisson structure, and the associativity of $*$ is the Jacobi identity for the bracket. The summand $\operatorname{Der}\otimes_A\Omega^1$ carries the deformations that change the differential calculus rather than the Poisson structure, and $\Omega^2$ the deformations of the two-forms; only the summand of bivectors gives the Poisson family displayed.

**Example.** For the matrix algebra $A=M_n(k)$ the deformations of $A$ are all trivial: $HH^2(M_n(k),M_n(k))=0$ because Hochschild cohomology is Morita invariant and $M_n(k)$ is Morita equivalent to $k$, whose Hochschild cohomology is $k$ in degree zero. So the matrix algebra is rigid.

### Higher Order and the Maurer–Cartan Equation

**Theorem (Gerstenhaber).** Let $A$ be an associative $k$-algebra with a $k$ of characteristic zero, and let $C^{\bullet}(A,A)$ be the Hochschild cochain complex with the Gerstenhaber bracket and the cup product. A formal deformation of $A$ over $k[[t]]$, that is a $k[[t]]$-algebra structure on $A[[t]]$ reducing to $A$ modulo $t$, is the same as a solution

$$
m_t=m_0+t m_1+t^2m_2+\cdots \in C^2(A,A)[[t]]
$$

of the **Maurer–Cartan equation**

$$
\partial m_t+\tfrac{1}{2}[m_t,m_t]=0,
$$

where $m_0$ is the multiplication of $A$ and $\partial=[m_0,-]$ is the Hochschild coboundary, and where two solutions are equivalent when they differ by the gauge action of the degree-zero part of the differential graded Lie algebra. The first-order coefficient $m_1$ is a $2$-cocycle, the obstruction to extending a partial deformation to the next order is the class of $\tfrac{1}{2}[m_t,m_t]$ in $HH^3(A,A)$, and the deformation is unobstructed when this class vanishes at every stage.

*Proof (in outline).* The associativity of $m_t$ is equivalent to the single equation $\tfrac{1}{2}[m_t,m_t]=0$ in the convolution algebra of cochains, where the bracket is the Gerstenhaber bracket of *Hochschild Homology*; the homotopy invariance of the bracket under the differential gives $\partial m_t+\tfrac12[m_t,m_t]=0$ once the linear term is separated. Expanding in powers of $t$, the coefficient of $t^n$ expresses $2\partial m_n$ in terms of the lower coefficients and their brackets; a partial deformation to order $n$ extends to order $n+1$ exactly when a certain $3$-cocycle is a coboundary, and this cocycle is $\sum_{i+j=n}[m_i,m_j]$. The gauge action is the action of the degree-zero cochains by the inner automorphisms of the differential graded Lie algebra, and it implements the change of variable $a\mapsto a+tg(a)+\cdots$ that leaves the multiplication equivalent. $\square$

**Corollary (unobstructedness).** If $HH^3(A,A)=0$ then every first-order deformation of $A$ extends over $k[[t]]$, and the formal moduli space is smooth of dimension $\dim_kHH^2(A,A)$ in the sense of the algebraic tangent space.

**Example.** For the polynomial algebra $A=k[x_1,\dots,x_m]$ with $k$ a field, the third Hochschild cohomology is $HH^3(A,A)\cong\bigoplus_{p+q=3}\Lambda^p\operatorname{Der}\otimes_A\Omega^q=\Lambda^3\operatorname{Der}\oplus(\Lambda^2\operatorname{Der}\otimes_A\Omega^1)\oplus(\operatorname{Der}\otimes_A\Omega^2)\oplus\Omega^3$; it is nonzero in general, so the Poisson deformations have obstructions, and the obstruction class of a bivector is the Schouten bracket with itself, which is the classical statement that the obstruction to a quantisation is the failure of the bivector to be Poisson.

**Example.** For $A=k$ the Hochschild cohomology is $k$ in degree zero and zero in positive degrees, so $HH^2(k,k)=0$ and $k$ has no nontrivial deformations: every associative multiplication on $k[[t]]$ reducing to that of $k$ modulo $t$ is the standard one, and $k$ is rigid.

## Deformations of Modules

### First-Order Module Deformations

**Definition.** Let $A$ be a $k$-algebra and $M$ a finite-dimensional $A$-module (over a field $k$). A **deformation** of $M$ over $R=k[\varepsilon]/(\varepsilon^2)$ is an $A\otimes_kR$-module $M_R$, flat over $R$, with $M_R\otimes_Rk\cong M$; equivalently an $A$-module structure on $M\otimes_k\mathbb{D}'$ of the form

$$
a\cdot_\varepsilon m=a m+\varepsilon\varphi(a,m),
$$

with $\varphi:A\times M\to M$ satisfying $a\varphi(b,m)-\varphi(ab,m)+\varphi(a,bm)=0$, which is the condition that $\varphi \in \operatorname{Hom}_k(A\otimes M,M)$ be a $1$-cocycle.

**Theorem.** The first-order deformations of $M$ up to equivalence are in natural bijection with $\operatorname{Ext}^1_A(M,M)$, and the obstruction to extending a deformation of $M$ to the second order lies in $\operatorname{Ext}^2_A(M,M)$.

*Proof.* The set of extensions $0\to M\to M_\varepsilon\to M\to0$ of $A_\varepsilon$-modules with $\varepsilon$ acting by the two-step filtration is the usual description of the deformations, and two deformations are equivalent when the corresponding extensions are isomorphic as $A$-module extensions of $M$ by $M$; the Yoneda description of $\operatorname{Ext}^1_A(M,M)$ as the classes of such extensions of *Ext and Tor* gives the bijection. The obstruction to lifting an extension across a square-zero extension of the parameter ring is the Yoneda product with the class of the extension, which lies in $\operatorname{Ext}^2_A(M,M)$. $\square$

**Example.** For $A=k[x]$ and $M=k[x]/(x)$ the module $M$ is simple and $\operatorname{Ext}^1_A(M,M)\cong k$: the resolution $0\to A\xrightarrow{\,x\,}A\to M\to0$ gives $\operatorname{Ext}^1\cong A/(x)\cong k$. The corresponding deformation is the $A\otimes_k\mathbb{D}'$-module $k[x]/(x-\varepsilon)\otimes_k\mathbb{D}'\cong\mathbb{D}'$ on which $x$ acts as multiplication by $\varepsilon$.

**Example.** For the same $A=k[x]$ and $M=A$ the module $A$ is free, hence projective, so $\operatorname{Ext}^1_A(A,A)=0$ and the free module of rank one is rigid as a module. This must not be confused with the deformations of $A$ as an **algebra**, which are governed by the Hochschild group $HH^2(A,A)$ of the previous section and do not vanish; the two functors are different, one taken over $A$ and the other over the enveloping algebra $A^{\mathrm{e}}$.

### Deformations of a Module over a Deformed Algebra

**Proposition.** Let $A_\varepsilon$ be a first-order deformation of $A$ with class $\alpha \in HH^2(A,A)$ and let $M_\varepsilon$ be a first-order deformation of an $A$-module $M$. Then $M$ admits a deformation over $A_\varepsilon$ if and only if the class $\alpha$ acts on $M$ and the resulting class in $\operatorname{Ext}^2_A(M,M)$ vanishes; the set of such deformations is a torsor under $\operatorname{Ext}^1_A(M,M)$ when it is nonempty.

*Proof.* A deformation of $M$ over $A_\varepsilon$ is a module over $A_\varepsilon$ whose reduction modulo $\varepsilon$ is $M$; the action of the deformed multiplication on $M$ is an element of $\operatorname{Hom}_k(A\otimes M,M)$ whose failure to be a module structure is the product of the class of $\alpha$ with the class of the identity of $M$ in the Ext algebra; the exactness is the long exact sequence of the deformation. The torsor action is the addition of a $1$-cocycle to the action. $\square$

## The Formal Moduli and Versal Deformations

### The Formal Moduli Space

**Definition.** The **formal moduli space** of $A$ is the functor $\operatorname{Def}_A$ of the first definition; when it is represented by a complete local $k$-algebra $\widehat{\mathcal{O}}$ in the sense that $\operatorname{Def}_A(R)=\operatorname{Hom}_{\mathrm{loc}}(\widehat{\mathcal{O}},R)$ for every Artinian local $R$, the algebra $\widehat{\mathcal{O}}$ is the **versal base** of the deformations.

**Theorem.** If the deformation functor is unobstructed and $HH^2(A,A)$ is finite-dimensional over $k$ then the formal moduli space is the formal spectrum of the power series ring $k[[t_1,\dots,t_d]]$ with $d=\dim_kHH^2(A,A)$, and the **Kuranishi map**

$$
\kappa:HH^2(A,A)\longrightarrow HH^3(A,A)
$$

given by the quadratic obstruction $\kappa(\alpha)=\tfrac12[\alpha,\alpha]$ is the only data needed to present the versal deformation as the zero locus of the Maurer–Cartan equation.

*Proof (in outline).* Unobstructedness makes the deformation functor isomorphic to the functor of points of the power series ring on the dual of $HH^2$, by the theorem of the Maurer–Cartan equation; the Kuranishi map is the quadratic form induced by the bracket, and its vanishing locus is the image of the deformation functor in the tangent space. $\square$

**Remark.** This is the algebraic statement of the deformation-theoretic method: the moduli problem is linear in the tangent space and quadratic in the first obstruction. The corresponding geometric statement, in which the versal deformation is a family of varieties and the Kuranishi map is computed from a cotangent complex, requires the scheme-theoretic language of Part II and is not used here.

### Rigidity

**Definition.** The algebra $A$ is **rigid** if $\operatorname{Def}_A(R)$ is a single point for every Artinian local $k$-algebra $R$, equivalently if every formal deformation is trivial and every first-order deformation is a coboundary.

**Theorem (rigidity criterion).** If $HH^2(A,A)=0$ then $A$ is rigid; if in addition $HH^1(A,A)=0$ then every automorphism of a deformation is inner, and the deformation functor is a single point with trivial automorphisms. Conversely, if $A$ is rigid and $HH^2$ is finite-dimensional, then $HH^2(A,A)=0$.

*Proof.* The first-order deformations are $HH^2$; if that group vanishes there are no nontrivial first-order deformations, and the Maurer–Cartan equation forces every formal deformation to be trivial by induction on the order. The converse follows by taking the first-order part. $\square$

**Example.** A finite-dimensional semisimple $k$-algebra over a field $k$ of characteristic zero has $HH^n(A,A)=0$ for every $n\ge1$, so it is rigid; this covers the matrix algebras $M_n(k)$ and the split complex algebra $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$, and it is the algebraic form of the fact that a semisimple algebra admits no nontrivial formal deformations. The polynomial algebra $k[x_1,\dots,x_m]$ with $m\ge2$ is not rigid, its deformations being the Poisson brackets computed above.

## The Differential Graded Lie Algebra of Deformations

### The Cochain Complex

**Definition.** The **Hochschild cochain complex** of $A$ with coefficients in $A$ is the differential graded Lie algebra $C^{\bullet}(A,A)$ with the composition product of *Hochschild Homology*, whose associated graded Lie bracket is the Gerstenhaber bracket $[,]$ and whose differential is $\partial=[m,-]$ with $m$ the multiplication; the bracket satisfies the graded Jacobi identity and the Leibniz rule with respect to $\partial$, so $(C^{\bullet}(A,A),\partial,[,])$ is a differential graded Lie algebra.

**Theorem (Deligne, as formulated in the associative case).** The deformation functor $\operatorname{Def}_A$ is the **Maurer–Cartan functor** of the differential graded Lie algebra $C^{\bullet}(A,A)$:

$$
\operatorname{Def}_A(R)=\operatorname{MC}\bigl(C^{\bullet}(A,A)\otimes_k\mathfrak{m}_R\bigr)/\text{gauge},
$$

where $\operatorname{MC}(\mathfrak{g}\otimes\mathfrak{m})=\{x \in \mathfrak{g}^1\otimes\mathfrak{m}:\partial x+\tfrac12[x,x]=0\}$ is the set of Maurer–Cartan elements and the gauge group is the degree-zero part of the differential graded Lie algebra acting by the exponential. In particular the tangent space of the deformation functor is $HH^2(A,A)$, the obstruction space is $HH^3(A,A)$, and the automorphism group of a deformation is computed by $HH^1$ and $HH^0$.

*Proof (in outline).* The identification of the Maurer–Cartan elements with the associative products is the theorem of the Maurer–Cartan equation above; the gauge action is the action of the degree-zero cochains by conjugating the product, and its orbits are the equivalence classes. The tangent space of the functor at the trivial deformation is the space of $1$-cocycles modulo coboundaries by the standard computation in the differential graded Lie algebra, and the obstruction space is the next cohomology. $\square$

**Example.** For $A=k[x_1,\dots,x_m]$ the differential graded Lie algebra is the Hochschild cochain complex, whose cohomology is $\Lambda^{\bullet}\operatorname{Der}_k(A,A)\otimes_A\Omega^{\bullet}_{A/k}$ by the Hochschild–Kostant–Rosenberg theorem; the Maurer–Cartan elements are the solutions of the Schouten equation, and the first-order part is $HH^2=\Lambda^2\operatorname{Der}\oplus(\operatorname{Der}\otimes_A\Omega^1)\oplus\Omega^2$.

### The Cotangent Complex, Named Only

**Remark.** The differential graded Lie algebra $C^{\bullet}(A,A)$ is the algebraic model for the deformations of $A$; its linearisation is the **cotangent complex** $\mathbb{L}_{A/k}$, an object of the derived category of *Derived Categories*, whose cohomology in degree $i$ is the Andr\'e–Quillen cohomology $D^i(A/k,A)$. The identification $HH^2(A,A)\cong\operatorname{Ext}^1_A(\mathbb{L}_{A/k},A)$ and the corresponding description of the higher obstructions are standard; the cotangent complex has a geometric theory for schemes, with the cotangent complex of a morphism and the deformation to the normal cone, and that theory belongs to Part II, where it is treated in *Sheaves and Cohomology* and the articles on algebraic geometry. Here the complex is named only.

## Summary

A deformation of an associative $k$-algebra $A$ over an Artinian local parameter ring is a flat algebra specialising to $A$; over the dual numbers it is a bilinear product $a*b=ab+\varepsilon f(a,b)$ whose associativity is the Hochschild $2$-cocycle condition, so the first-order deformations up to equivalence are $HH^2(A,A)$ and the trivial product corresponds to the zero class. Higher-order deformations are the Maurer–Cartan solutions of the Hochschild cochain complex, a differential graded Lie algebra under the Gerstenhaber bracket and the Hochschild differential, and the obstruction to extending a deformation one order lies in $HH^3(A,A)$; when that group vanishes the deformation is unobstructed and the formal moduli space is smooth of dimension $\dim HH^2$.

For a module $M$ over $A$ the same picture holds with $\operatorname{Ext}$ in place of Hochschild cohomology: first-order deformations are $\operatorname{Ext}^1_A(M,M)$, the obstruction to the second order is $\operatorname{Ext}^2_A(M,M)$, and the deformations of $M$ over a deformed algebra are controlled by the action of the class of the algebra deformation on the Ext algebra of $M$. The matrix algebra and the field are rigid; the polynomial algebra has deformations by Poisson bivectors whose obstruction is the Schouten bracket; and the versal deformation is presented by the Kuranishi map. The cotangent complex, whose cohomology computes the same groups in the derived setting, is named and its geometric theory deferred to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | commutative ground ring with $1\neq0$ |
| $\mathbb{D}'=k[\varepsilon]/(\varepsilon^2)$ | dual numbers, the first-order parameter ring |
| $A$, $A_S$, $A_\varepsilon$ | algebra, deformation over $S$, over the dual numbers |
| $\operatorname{Def}_A(R)$ | deformation functor on Artinian local $k$-algebras |
| $f(a,b)$, $m_t$ | deformation cocycle, formal multiplication |
| $\partial=[m,-]$ | Hochschild coboundary in the dg Lie algebra |
| $[,]$ | Gerstenhaber bracket |
| $\operatorname{MC}(\mathfrak{g})$ | Maurer–Cartan elements of a differential graded Lie algebra |
| $HH^n(A,A)$ | Hochschild cohomology of $A$ |
| $\operatorname{Ext}^n_A(M,M)$ | Ext of a module with itself |
| $\kappa$ | Kuranishi map |
| $\mathbb{L}_{A/k}$ | cotangent complex, named only |
| $M_R$, $M_\varepsilon$ | deformation of a module over $R$ and over the dual numbers |



## Further Reading

- Murray Gerstenhaber, "On the deformation of rings and algebras", *Annals of Mathematics* 79 (1964), 59–103, for the deformation functor, the cup product and the obstruction calculus.
- Murray Gerstenhaber and Samuel D. Schack, "On the deformation of algebra morphisms and diagrams", *Transactions of the American Mathematical Society* 279 (1983), 1–50, for the diagrammatic and functorial refinements.
- Vladimir Hinich, "Descent of Deligne groupoids", *International Mathematics Research Notices* 1997, 223–239, for the differential graded Lie algebra control of deformations.
- Maxim Kontsevich, "Deformation quantization of Poisson manifolds", *Letters in Mathematical Physics* 66 (2003), 157–216, for the Maurer–Cartan equation and the quantisation of Poisson brackets.
- Marco Manetti, "Deformation theory via differential graded Lie algebras", in *Seminari di Geometria Algebrica* (Scuola Normale Superiore, 1999), for the Maurer–Cartan and gauge formalism.
- Daniel Quillen, "On the (co-)homology of commutative rings", in *Applications of Categorical Algebra* (American Mathematical Society, 1970), for the cotangent complex and the Andr\'e–Quillen cohomology.
- Michael Schlessinger, "Functors of Artin rings", *Transactions of the American Mathematical Society* 130 (1968), 208–222, for the formal moduli functors and the versal deformation.
- Robin Hartshorne, *Deformation Theory* (Springer, 2010), for the algebraic development of the deformation functor and its geometric counterpart.
