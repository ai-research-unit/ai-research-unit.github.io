
# __Deformation Quantization__

## Introduction

A **deformation** of an algebra is a family of multiplications on the same underlying module, parameterised by a formal variable, whose value at the origin is the given multiplication. **Deformation quantization** is the deformation theory of the commutative algebra of functions or of the symmetric algebra, in which the first-order term of the deformation is required to be a Poisson bracket: the deformed algebra is then a quantisation of the Poisson structure, and the two structures determine each other up to the appropriate notion of equivalence.

The article is the seventh of the category. It follows *Quantum Groups*, whose quantised enveloping algebras and quantum plane are the motivating examples, and *Hopf Algebras*, whose framework supplies the compatible deformations of a Hopf algebra; it uses the Hochschild cohomology and the deformation theory of the category's homological layer, which is introduced above it in the menu, and it is the article in which the algebra-level statements that the other articles on $A_\infty$-algebras and on Poisson and Gerstenhaber algebras generalise are collected. Its subject is the algebraic theory of the star product.

The article is algebraic. A **Poisson structure** here is a bilinear bracket on an algebra satisfying the Leibniz rule and the Jacobi identity; the geometric Poisson structure on a manifold, the symplectic form, the Hamiltonian vector field and the Poisson tensor in coordinates are objects of Part II, where the notion of a manifold and of a form is available, and they are deferred. Likewise the analytic questions of convergence of a star product belong to a later Part; here a star product is a formal series in a parameter and no question of convergence is raised. The operadic machinery used by the formality theorem is the algebra of operads, which is introduced in the menu above this article; the model-category and higher-category formulations are Part II's and are not used.

Throughout, $k$ is a field of characteristic $0$ unless stated otherwise, $A$ is an associative $k$-algebra, $A^{\mathrm{e}} = A\otimes_k A^{\mathrm{op}}$ is the enveloping algebra of *Separable Algebras*, and $k[[h]]$ is the algebra of formal power series in one variable, the completion of the polynomial algebra. All tensor products are over $k$.

## Formal Deformations of an Algebra

### Definitions

**Definition.** Let $A$ be a $k$-algebra. A **formal deformation** of $A$ is a $k[[h]]$-algebra $A_h$ with an isomorphism of $k[[h]]$-modules $A_h \cong A[[h]]$ such that $A_h/hA_h \cong A$ as $k$-algebras. Equivalently, $A_h$ is the module $A[[h]]$ with a multiplication

$$
a *_h b = ab + \sum_{n\geq1} h^n\,\mu_n(a,b), \qquad \mu_n : A\times A \to A \ \text{bilinear},
$$

which is associative and has unit $1$. Two deformations $*_h$ and $*'_h$ are **equivalent** if there is a $k[[h]]$-linear algebra isomorphism $\Phi = \mathrm{id} + \sum_{n\geq1}h^n\varphi_n$ between them.

**Definition.** The deformation is **trivial** if it is equivalent to the constant deformation $\mu_n = 0$ for $n\geq1$, and **infinitesimal** if it is truncated at first order, that is, if it is given by a single bilinear map $\mu_1$ on $A$.

The equivalence relation is the correct one: an equivalence with $\varphi_1 \neq 0$ changes the multiplication at first order by the **coboundary** $\mu_1 \mapsto \mu_1 + \delta\varphi_1$, where $\delta$ is the Hochschild differential. This is why the classification of infinitesimal deformations is a cohomological statement.

### The Hochschild complex

**Definition.** The **Hochschild cochain complex** of $A$ with coefficients in $A$ is

$$
C^n(A,A) = \operatorname{Hom}_k(A^{\otimes n}, A), \qquad (\delta f)(a_1,\dots,a_{n+1}) = a_1f(a_2,\dots,a_{n+1}) + \sum_{i=1}^{n}(-1)^if(a_1,\dots,a_ia_{i+1},\dots,a_{n+1}) + (-1)^{n+1}f(a_1,\dots,a_n)a_{n+1},
$$

with cohomology $HH^n(A,A) = \ker\delta/\operatorname{im}\delta$. The complex is the standard complex computing $\operatorname{Ext}^\bullet_{A^{\mathrm{e}}}(A,A)$, where $A$ is regarded as an $A^{\mathrm{e}}$-module; the systematic theory is the subject of *Hochschild Homology*, above this article in the menu.

**Proposition.** $HH^0(A,A) = Z(A)$ is the centre of $A$, and $HH^1(A,A)$ is the space of derivations modulo the inner derivations, which is the quotient of the derivations of *Automorphisms and Derivations of Algebras* by the inner ones.

*Proof.* A $0$-cochain is an element $f \in A$, and $\delta f(a) = af - fa$, so $\ker\delta = Z(A)$. A $1$-cochain is a linear map $f : A \to A$, and $(\delta f)(a,b) = af(b) - f(ab) + f(a)b$, so $\ker\delta$ is the space of derivations $\operatorname{Der}(A)$; the image of $\delta$ on $0$-cochains consists of the maps $a \mapsto af - fa$, that is, the inner derivations. $\square$

### The classification theorem

**Theorem (Gerstenhaber, standard).** Let $A$ be a $k$-algebra and consider deformations of $A$ over $k[[h]]$.

1. The first-order term $\mu_1$ of an associative deformation is a $2$-cocycle, $\delta\mu_1 = 0$; hence it defines a class $[\mu_1] \in HH^2(A,A)$.
2. Two deformations are equivalent to first order exactly when their classes in $HH^2(A,A)$ coincide. Hence infinitesimal deformations of $A$ are parametrised by $HH^2(A,A)$.
3. The class $[\mu_1]$ extends to a full associative deformation only if a sequence of obstructions in $HH^3(A,A), HH^4(A,A),\dots$ vanishes; the first obstruction is the **Gerstenhaber bracket** $[\mu_1,\mu_1] \in HH^3(A,A)$, which is the obstruction to extending to second order.

The proof of the second statement is the computation of the associativity of $*_h$ modulo $h^2$, which is exactly $\delta\mu_1 = 0$; the equivalence statement is the coboundary change of the preceding section. The obstruction theory is the general theory of *Deformation Theory*, above this article in the menu, and the bracket that computes the obstruction is introduced in the next section.

## The Gerstenhaber Bracket and the Operadic Structure

### The graded Lie bracket

**Definition.** For $f \in C^m(A,A)$ and $g \in C^n(A,A)$, the **Gerstenhaber bracket** (the circle product, alternatively the insertion operation) is defined on a tensor argument $a_1\otimes\cdots\otimes a_{m+n-1}$ by inserting $g$ in the $i$-th slot of $f$, $f \circ_i g$, as

$$
(f\circ_i g)(a_1,\dots,a_{m+n-1}) = f\bigl(a_1,\dots,a_{i-1}, g(a_i,\dots,a_{i+n-1}), a_{i+n},\dots,a_{m+n-1}\bigr),
$$

and the bracket is

$$
[f,g] = \sum_{i=1}^{m}(-1)^{(n-1)(i-1)}f\circ_i g \;-\; (-1)^{(m-1)(n-1)}\sum_{j=1}^{n}(-1)^{(m-1)(j-1)}g\circ_j f .
$$

**Theorem (Gerstenhaber, standard).** With the bracket and the **cup product**

$$
(f\smile g)(a_1,\dots,a_{m+n}) = f(a_1,\dots,a_m)\,g(a_{m+1},\dots,a_{m+n}),
$$

the cochain complex $C^{\bullet+1}(A,A)$ is a graded Lie algebra of degree $1$ and $HH^{\bullet+1}(A,A)$ is a graded Lie algebra; the cup product descends to cohomology and makes $HH^\bullet(A,A)$ a **Gerstenhaber algebra**:

$$
[f\smile g] = [f]\smile g + (-1)^{\lvert f\rvert}\,f\smile[g] \qquad \text{(graded Leibniz)}, \qquad [f,f] = 0 \ \text{for } \lvert f\rvert \ \text{odd},
$$

so the bracket is graded antisymmetric with $[f,g] = (-1)^{(\lvert f\rvert-1)(\lvert g\rvert-1)}[g,f]$ and satisfies the graded Jacobi identity, and the bracket has degree $-1$ in the shifted grading.

The Gerstenhaber bracket is the algebraic structure that controls deformations: an element $\mu$ of degree $2$ is an associative multiplication modulo a coboundary exactly when $[\mu,\mu] = 0$, that is, when $[\mu,\mu]$ is a coboundary; the Maurer–Cartan equation $[\mu,\mu]=0$ appears aga, where it is the defining equation of an $A_\infty$-structure. The Gerstenhaber algebra structure itself is the subject in the anti-symmetric category, where the Leibniz and Jacobi identities of the bracket are stated in full.

### The operadic formulation

**Definition.** An **operad** $\mathcal{O}$ in $k$-modules consists of a collection $\mathcal{O}(n)$ of $k$-modules for $n \geq 0$ with an action of the symmetric group $\Sigma_n$ on $\mathcal{O}(n)$, a composition law

$$
\circ : \mathcal{O}(m)\otimes_k \mathcal{O}(n_1)\otimes_k\cdots\otimes_k\mathcal{O}(n_m) \to \mathcal{O}(n_1 + \cdots + n_m),
$$

and a unit in $\mathcal{O}(1)$, satisfying the associativity, unitality and equivariance axioms. An **algebra over** $\mathcal{O}$ is a $k$-module $V$ with maps $\mathcal{O}(n)\otimes_k V^{\otimes n} \to V$ compatible with the operad structure.

**Proposition.** The Hochschild cochains of $A$ form an operad; more precisely, the collection $\{\operatorname{Hom}_k(A^{\otimes n}, A)\}_{n\geq1}$ with the substitution operations $\circ_i$ of the preceding definition is an operad, and the operad structure is what makes the Gerstenhaber bracket natural.

**Proposition (the little disks operad).** Let $D_2(n)$ be the space of configurations of $n$ disjoint disks inside the unit disk, with the compositions given by rescaled insertions. Then the homology $H_\bullet(D_2(n);k)$ is the operad $\mathcal{E}_2$ whose algebras are exactly the algebras with an associative multiplication and a compatible Lie bracket of degree $1$, that is, the Gerstenhaber algebras. The chain-level statement that $D_2$ is formal — its chains are quasi-isomorphic to its homology as an operad — is the **Kontsevich formality theorem** for the operad of little disks, and it is the technical heart of the formality theorem for the Hochschild complex.

The correspondence between the Hochschild operad and the little disks operad is the content of the statement that an associative algebra is an $\mathcal{E}_1$-algebra and that a Gerstenhaber algebra is an $\mathcal{E}_2$-algebra; the operadic formalism is introduced in *Operads*, above this article, and the homotopy-theoretic and cobordism-theoretic uses of the little disks operad belong to Part II.

## Poisson Structures and Star Products

### Poisson algebras

**Definition.** A **Poisson algebra** over $k$ is a commutative associative $k$-algebra $A$ with a $k$-bilinear map $\{\cdot,\cdot\} : A\times A \to A$ that is a **Lie bracket** — antisymmetric and satisfying the Jacobi identity — and a **derivation** in each variable:

$$
\{f,gh\} = \{f,g\}h + g\{f,h\} .
$$

The bracket is the **Poisson bracket**, and the axiom relating it to the product is the **Leibniz rule**. A Poisson algebra is thus a commutative algebra and a Lie algebra in a compatible way, and the two structures are precisely the data of a Gerstenhaber algebra concentrated in degrees $0$ and $1$ with the bracket of degree $-1$.

**Example.** For $A = k[x_1,\dots,x_n]$ and a skew-symmetric matrix $\omega = (\omega_{ij})$ of constants, the bracket

$$
\{f,g\} = \sum_{i,j}\omega_{ij}\,\partial_if\,\partial_jg
$$

is a Poisson bracket: antisymmetry and the Jacobi identity follow because $\omega$ is constant and skew, and the Leibniz rule is the product rule for the formal derivatives. This is the **constant** or **linear** case, and it is the Poisson structure whose quantisation is the Moyal product. When $\omega$ is invertible the bracket is called **symplectic**, and the geometric content of that case belongs to Part II.

**Example.** On $A = k[x,y]$ the bracket defined by $\{y,x\} = xy$ and extended by the Leibniz rule,

$$
\{f,g\} = xy\,(\partial_xf\,\partial_yg - \partial_yf\,\partial_xg),
$$

is a Poisson bracket; it is not constant, and it is the Poisson structure quantised by the quantum plane.

### Star products

**Definition.** A **star product** on a Poisson algebra $A$ is an associative deformation $*$ of $A$ over $k[[h]]$,

$$
f * g = fg + \sum_{n\geq1}h^nC_n(f,g),
$$

such that $C_1(f,g) - C_1(g,f) = \{f,g\}$, and every $C_n$ is a bidifferential operator, meaning a $k$-linear combination of compositions of the formal derivations $\partial_i$. The condition on $C_1$ says that the antisymmetrisation of the leading term is the given Poisson bracket, and it is what makes the deformation a *quantisation* of the bracket rather than an arbitrary deformation.

**Proposition.** The antisymmetrised part of $C_1$ is forced to be a Poisson bracket by the associativity of $*$: the identity $(f*g)*h = f*(g*h)$ modulo $h^2$ gives

$$
C_1(fg,h) - C_1(f,gh) + C_1(f,g)h - fC_1(g,h) = 0 ,
$$

which says that the bilinear map $\{f,g\} = C_1(f,g) - C_1(g,f)$ satisfies the Leibniz rule and the Jacobi identity. Hence the first-order term of any associative deformation of a commutative algebra whose leading term is antisymmetric is a Poisson structure, and the classification of *first-order* quantisations is the classification of Poisson structures up to the appropriate equivalence.

*Proof.* Expand the associativity identity and collect the coefficient of $h^2$; the three terms of the expansion give the displayed identity, which is the cocycle condition $\delta C_1 = 0$; antisymmetrising it in the three arguments gives the Jacobi identity for the antisymmetrisation, and the Leibniz rule follows from the same identity by taking $g = 1$. $\square$

### The Moyal star product

**Example (Moyal).** Let $A = k[x_1,\dots,x_n]$ with the constant Poisson bracket $\omega$. The **Moyal star product**

$$
f * g = \sum_{r\geq0}\frac{1}{r!}\Bigl(\frac{h}{2}\Bigr)^r\sum_{i_1,\dots,i_r,j_1,\dots,j_r}\omega_{i_1j_1}\cdots\omega_{i_rj_r}\,\partial_{i_1}\cdots\partial_{i_r}f\ \partial_{j_1}\cdots\partial_{j_r}g
$$

is associative and has $C_1(f,g) = \tfrac12\sum_{i,j}\omega_{ij}\partial_if\partial_jg$, so its antisymmetrisation is the Poisson bracket $\{f,g\} = \sum_{i,j}\omega_{ij}\partial_if\partial_jg$ of the constant case and it is a star product quantising $\omega$. For $n = 2$ and $\omega_{12} = 1$ the deformed generators satisfy

$$
x_1*x_2 - x_2*x_1 = h,
$$

which is the formal form of the canonical commutation relation. The algebra $(k[x_1,x_2],*)$ is the Weyl algebra in its completed form, and it is the basic example in which the star product can be written by a closed formula.

*Proof of associativity (sketch).* Writing $f*g = m\circ e^{\frac h2\omega(\partial,\partial')}(f\otimes g)$ with $m$ the multiplication, associativity follows from the fact that the exponential of a constant-coefficient bidifferential operator is the exponential of a derivation of the tensor algebra, and exponentials of commuting derivations compose by addition of their exponents. $\square$

**Example (quantum plane as a quantisation).** For $A = k[x,y]$ with the Poisson bracket $\{y,x\} = xy$, the algebra $k_q[x,y]$ with $yx = qxy$ and $q = 1 + h$ is a star product to first order: the antisymmetrisation of $C_1$ is $\{y,x\} = xy$. The two deformations of $k[x,y]$ — the Moyal deformation by a constant bracket and the $q$-commuting deformation by $\{y,x\} = xy$ — are inequivalent as deformations, because their first-order terms are inequivalent Poisson structures. This is the standard illustration that the first-order term, and not the deformed algebra alone, is the invariant that the deformation quantisation records.

## Formality and the Classification of Quantisations

### $L_\infty$-algebras and the formality statement

**Definition.** An **$L_\infty$-algebra** structure on a graded $k$-module $V$ is a collection of graded antisymmetric multilinear maps $\ell_n : V^{\otimes n} \to V$ of degree $2-n$ satisfying the higher Jacobi identities

$$
\sum_{i+j=n+1}\ \sum_{\sigma}(-1)^{\sigma}\varepsilon(\sigma)\,\ell_j\bigl(\ell_i(v_{\sigma(1)},\dots,v_{\sigma(i)}),v_{\sigma(i+1)},\dots,v_{\sigma(n)}\bigr) = 0 ;
$$

the case $n = 2$ with $\ell_3 = 0$ is an ordinary Lie algebra, and the general structure is the homotopy-coherent version of a Lie algebra. The notion and its morphisms are developed in the menu.

**Theorem (Kontsevich formality, standard).** Let $A = k[x_1,\dots,x_n]$ be a polynomial algebra, let $T_{\mathrm{poly}}(A)$ be the graded module of polynomial multivectors, with the **Schouten–Nijenhuis bracket**, and let $C^\bullet(A,A)$ be the Hochschild complex with the Gerstenhaber bracket. Then there is an $L_\infty$-quasi-isomorphism

$$
\mathcal{U} : \bigl(T_{\mathrm{poly}}(A),\ \text{Schouten bracket},\ 0,\ 0,\dots\bigr) \longrightarrow \bigl(C^{\bullet}(A,A),\ \text{Gerstenhaber bracket},\ \text{cup product},\ \dots\bigr)
$$

from the $L_\infty$-algebra of multivectors, which is the abelian structure with only $\ell_2$ the Schouten bracket and all higher brackets zero, to the Hochschild complex with its full $L_\infty$-structure. The quasi-isomorphism is constructed by an explicit sum over graphs, whose weights are integrals over configuration spaces of points in the upper half-plane.

**Theorem (Kontsevich, standard).** The formality theorem has two consequences.

1. Every formal Poisson structure on a polynomial algebra $A = k[x_1,\dots,x_n]$, with $k$ a field of characteristic $0$, admits a star product: the Maurer–Cartan element $\pi$ of the multivector $L_\infty$-algebra with $[\pi,\pi] = 0$ transfers along $\mathcal{U}$ to a Maurer–Cartan element of the Hochschild complex, and such an element is exactly an associative deformation whose first-order term is the bracket of $\pi$. The resulting star product has the explicit graph-sum expansion

    $$
    f * g = \sum_{n\geq0}\frac{h^n}{n!}\sum_{\Gamma\in G_n}w_\Gamma\,B_\Gamma(f,g),
    $$

    where $G_n$ is the set of admissible graphs with $n$ internal vertices, $w_\Gamma$ is a weight obtained by integrating a form over a configuration space of points in the upper half-plane, and $B_\Gamma$ is the bidifferential operator determined by the edges of $\Gamma$ decorated by the Poisson tensor.
2. The quasi-isomorphism $\mathcal{U}$ induces a bijection between Maurer–Cartan elements modulo gauge equivalence in the two $L_\infty$-algebras, hence a bijection between equivalence classes of formal Poisson structures and equivalence classes of star products. In particular the quantisation of a formal Poisson structure exists and is unique up to equivalence, and the two equivalence relations — of Poisson structures and of associative deformations — correspond exactly.

*Proof (outline).* A quasi-isomorphism of $L_\infty$-algebras induces a bijection on Maurer–Cartan sets modulo the respective gauge actions; this is the standard homotopy-transfer statement for $L_\infty$-algebras, and it is the algebraic content of the theorem. The Jacobi identity for a Poisson bivector $\pi$ is the equation $[\pi,\pi] = 0$ in the Schouten–Nijenhuis bracket, so $\pi$ is a Maurer–Cartan element, and its image under $\mathcal{U}$ is a Maurer–Cartan element of the Hochschild complex with the Gerstenhaber bracket; unwinding that condition gives the associativity of the deformation. $\square$

The theorem is the structure theorem of the subject, and its proof is operadic and topological: it uses the configuration space of $n$ points in the upper half-plane, the formality of the operad of little $2$-disks, and the relation between the Hochschild complex and the operad $\mathcal{E}_2$. The operadic part is introduced in *Operads*, above this article; the topological and model-categorical formulations belong to Part II.

### Deformations of the enveloping and of the Hopf structures

The same formality machinery applies to the deformations of the enveloping algebra and to the Hopf-algebraic deformations of *Quantum Groups*. The relevant statements are:

- the enveloping algebra $U(\mathfrak{g})$ of a Lie algebra is the quotient of a deformation of $\operatorname{Sym}(\mathfrak{g})$ by the linear Poisson bracket determined by the Lie bracket, by the symmetrisation map;
- the deformation of $\operatorname{Sym}(\mathfrak{g})$ by that bracket, with the **campbell–Hausdorff**-type star product, gives a deformation whose associated graded is the symmetric algebra;
- a deformation of a Hopf algebra is a deformation of the underlying algebra together with deformed coproduct and antipode, and the first-order term of the coproduct deformation is a **coboundary Poisson structure** on the Hopf algebra; Drinfeld's classification of deformations of $U(\mathfrak{g})$ and the theory of quantum groups at generic $q$ are the resulting statements, and they are treated in *Quantum Groups*.

**Theorem (Drinfeld, standard).** The formal deformations of $U(\mathfrak{g})$ as a Hopf algebra over $k[[h]]$ are classified by the second cohomology of $\mathfrak{g}$ with coefficients in $\wedge^2\mathfrak{g}$, equivalently by the **quasi-Lie bialgebra** structures on $\mathfrak{g}$; for $\mathfrak{g}$ semisimple there is a unique nontrivial deformation up to equivalence and up to the choice of the symmetric invariant element used in the normalisation, and it is $U_h(\mathfrak{g})$.

The cohomology that appears here is that of the **Chevalley--Eilenberg complex** of $\mathfrak{g}$. For a $\mathfrak{g}$-module $M$ the degree-$n$ cochains are the alternating multilinear maps $f:\mathfrak{g}^n\to M$, with differential

$$
(df)(x_1,\dots,x_{n+1}) = \sum_{i=1}^{n+1}(-1)^{i+1}x_i\cdot f(x_1,\dots,\widehat{x_i},\dots,x_{n+1}) + \sum_{i<j}(-1)^{i+j}f\bigl([x_i,x_j],x_1,\dots,\widehat{x_i},\dots,\widehat{x_j},\dots,x_{n+1}\bigr),
$$

the hats marking omitted arguments, and the coefficient module of the theorem is $\wedge^2\mathfrak{g}$ with the adjoint action $x\cdot(u\wedge v) = [x,u]\wedge v + u\wedge[x,v]$. The differential is built from the bracket and the action alone, so the cohomology is available here without a general theory of Lie algebra cohomology; the structure of the quasi-Lie bialgebra is the infinitesimal object that the quantum group deforms.

## Summary

A **formal deformation** of a $k$-algebra $A$ is a $k[[h]]$-algebra $A_h$ with $A_h \cong A[[h]]$ as a module and $A_h/hA_h \cong A$; two deformations are **equivalent** when they differ by an algebra isomorphism of the form $\mathrm{id} + h\varphi_1 + \cdots$. The first-order term of an associative deformation is a $2$-cocycle for the **Hochschild complex**, so infinitesimal deformations of $A$ are parametrised by $HH^2(A,A)$, with obstructions in $HH^3(A,A)$ and beyond computed by the **Gerstenhaber bracket** $[\mu_1,\mu_1]$; the Gerstenhaber bracket and the cup product make $HH^{\bullet+1}(A,A)$ a graded Lie algebra and $HH^\bullet(A,A)$ a **Gerstenhaber algebra**, which is an algebra over the homology of the little disks operad $\mathcal{E}_2$, and the operad of Hochschild cochains is formal.

A **Poisson algebra** is a commutative associative algebra with a Lie bracket that is a derivation in each variable, and a **star product** on a Poisson algebra is an associative deformation $f*g = fg + \sum_{n\geq1}h^nC_n(f,g)$ whose first-order antisymmetrisation is the Poisson bracket; the associativity forces that antisymmetrisation to be a Poisson bracket. The **Moyal product** on $k[x_1,\dots,x_n]$ with a constant bracket $\omega$ is the closed-form example, with $x_1*x_2 - x_2*x_1 = h$ in the two-variable case, and the quantum plane $k_q[x,y]$ with $q = 1+h$ is the quantisation of the bracket $\{y,x\} = xy$; the two deformations are inequivalent because their first-order terms are. The **Kontsevich formality theorem** asserts an $L_\infty$-quasi-isomorphism from the multivector fields with the Schouten–Nijenhuis bracket to the Hochschild complex with the Gerstenhaber bracket, and it implies that every Poisson structure on a polynomial algebra admits a star product and that the correspondence between Poisson brackets and equivalence classes of star products is a bijection. Drinfeld's classification of the Hopf-algebraic deformations of $U(\mathfrak{g})$ is the same circle of ideas in the quantum-group setting. The geometric Poisson and symplectic structures, the manifold theory and the convergence of star products belong to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $h$ | field of characteristic $0$, deformation parameter |
| $A$, $A_h$ | algebra and its formal deformation over $k[[h]]$ |
| $k[[h]]$ | algebra of formal power series in $h$ |
| $a*_h b = ab + \sum_{n\geq1}h^n\mu_n(a,b)$ | deformed multiplication |
| $\mu_n$ | $n$-th order term of the deformation |
| $A^{\mathrm{e}} = A\otimes_k A^{\mathrm{op}}$ | enveloping algebra |
| $C^n(A,A) = \operatorname{Hom}_k(A^{\otimes n},A)$ | Hochschild cochains |
| $\delta$ | Hochschild differential |
| $HH^n(A,A)$ | Hochschild cohomology |
| $[f,g]$ | Gerstenhaber bracket (degree $-1$ in shifted grading) |
| $f\smile g$ | cup product of cochains |
| $\{f,g\}$ | Poisson bracket, first-order term of $*$ |
| $\omega_{ij}$ | constant Poisson tensor; $\{f,g\} = \sum\omega_{ij}\partial_if\partial_jg$ |
| $C_n(f,g)$ | coefficients of the star product |
| $\mathcal{O}$, $\mathcal{E}_2$, $D_2$ | operad, little disks homology operad, little disks operad |
| $\ell_n$ | higher brackets of an $L_\infty$-algebra |
| $T_{\mathrm{poly}}(A)$ | polynomial multivectors, Schouten–Nijenhuis bracket |
| $\mathcal{U}$ | Kontsevich $L_\infty$-quasi-isomorphism |
| $U_h(\mathfrak{g})$ | Hopf-algebraic deformation of $U(\mathfrak{g})$ |





## Further Reading

- Murray Gerstenhaber, "On the deformation of rings and algebras", *Annals of Mathematics* **79** (1964), 59–103, for the Hochschild classification of deformations and the graded Lie bracket.
- Murray Gerstenhaber, "The cohomology structure of an associative ring", *Annals of Mathematics* **78** (1963), 267–288, for the graded algebra structure on Hochschild cohomology.
- Maxim Kontsevich, "Deformation quantization of Poisson manifolds", *Letters in Mathematical Physics* **66** (2003), 157–216, for the formality theorem and the classification of star products.
- Frank Bayen, Moshe Flato, Christian Fronsdal, André Lichnerowicz and Daniel Sternheimer, "Deformation theory and quantization I, II", *Annals of Physics* **111** (1978), 61–151, for the star product formalism and the Moyal product.
- James D. Stasheff, "Homotopy associativity of $H$-spaces I, II", *Transactions of the American Mathematical Society* **108** (1963), 275–312, for the $A_\infty$-structures that arise from the deformation complex.
- Tom Lada and James Stasheff, "Introduction to sh Lie algebras for physicists", *International Journal of Theoretical Physics* **32** (1993), 1087–1103, for $L_\infty$-algebras and the Maurer–Cartan equation.
- Martin Markl, Steve Shnider and Jim Stasheff, *Operads in Algebra, Topology and Physics* (American Mathematical Society, 2002), for the operadic formulation of the formality theorem.
- Vladimir G. Drinfeld, "Quantum groups", *Proceedings of the International Congress of Mathematicians* (Berkeley, 1986), 798–820, for the classification of Hopf-algebraic deformations.
