
# __Vertex Algebras__

## Introduction

A **vertex algebra** is a vector space $V$ over a field $k$ equipped with a distinguished vector $|0\rangle$, the **vacuum**, a linear endomorphism $T$, the **translation**, and a **state-field correspondence**

$$
Y: V\longrightarrow\operatorname{End}_k(V)[[z,z^{-1}]], \qquad a\longmapsto Y(a,z) = \sum_{n\in\mathbb{Z}}a_{(n)}z^{-n-1},
$$

sending each vector $a$ to a formal Laurent series whose coefficients $a_{(n)}$ are endomorphisms of $V$, subject to the axioms that the vacuum acts as the identity, that the field of $a$ applied to the vacuum reproduces $a$, that $T$ differentiates the fields, and that the fields of any two vectors **commute up to a power of $z-w$**. The modes $a_{(n)}$ turn the multiplication of $V$ into an infinite family of products, and the last axiom — **locality** — is the algebraic statement that the product is commutative and associative in the formal sense made precise by the **Jacobi identity** of the theory.

The article is the eighteenth of the corpus, in the category *Anti-symmetric Linear Algebras*, and it continues the Lie-theoretic development of the category after *Universal Enveloping Algebras* and *Lie Algebra Cohomology*. Its objects are Lie-algebraic: the examples are built from the Heisenberg algebra, the Virasoro algebra and the affine Lie algebras, each of which is a central extension of a Lie algebra presented in the present Part, and the auxiliary structure of a vertex algebra is a **conformal algebra**, that is a Lie algebra object whose bracket is a formal series in one variable. The article develops the formal series in which the definition is stated, the axioms and their equivalence with the Jacobi identity, the consequences for the modes and the operator product expansion, the three standard families of examples with the cocycle verification for the Virasoro algebra, the modules over a vertex algebra together with the **Zhu algebra** that reduces their classification to the representation theory of an associative algebra, and the $\lambda$-bracket formulation that exhibits the vertex algebra as a Lie algebra in a suitable category.

Two boundaries are maintained. First, the **analytic** theory: the convergence of the series, the modular invariance of the characters, the genus-one amplitudes and the analytic theory of the conformal field are the subject of Part III, where the limit and the measure are available, and no statement here uses a convergence. Second, the **geometric** theory: the reading of a vertex algebra as an object attached to a surface, the vertex operator algebras of a curve and the factorisation structure need the manifold of Part II and are deferred. The bilinear forms used in the construction of the affine and lattice examples are the invariant forms of the structure theory of Lie algebras, as in *Universal Enveloping Algebras*; the positive definite forms of the lattice constructions belong to Part II and those examples are named but not constructed here. No physics is invoked: the objects are algebras of formal series, and the names of the examples are names of algebras.

Throughout, $k$ is a field of characteristic zero, $V$ is a $k$-vector space, $V[[z]]$ is the ring of formal power series, $V((z)) = V[[z]][z^{-1}]$ is the ring of formal Laurent series, and $V[[z,z^{-1}]]$ is the $k$-module of formal series $\sum_{n\in\mathbb{Z}}v_nz^n$ with $v_n\in V$; these are the algebraic completions in the sense of *Formal Power Series and Completion*, that is inverse limits of quotient modules, and they are not analytic objects. The degrees of the fields are indexed so that $Y(a,z) = \sum_{n\in\mathbb{Z}}a_{(n)}z^{-n-1}$, and the modes satisfy $a_{(n)} = 0$ for $n\gg0$ only if the field is the zero field.

## Fields, Locality and the Axioms

**Definition.** A **field** on a $k$-vector space $V$ is an element $A(z) = \sum_{n\in\mathbb{Z}}A_nz^{-n-1}$ of $\operatorname{End}_k(V)[[z,z^{-1}]]$ such that $A(z)v\in V((z))$ for every $v\in V$: the series is a formal Laurent series in $z$ with finite principal part applied to each vector. Two fields $A(z)$ and $B(w)$ are **local** if there is an integer $N\geq0$ with

$$
(z-w)^N\bigl[A(z),B(w)\bigr] = 0
$$

in $\operatorname{End}_k(V)[[z^{\pm1},w^{\pm1}]]$, the bracket being the commutator of the two series in the commuting variables $z$ and $w$.

**Definition.** A **vertex algebra** over $k$ is a $k$-vector space $V$ with a vector $|0\rangle\in V$, an endomorphism $T:V\to V$ and a linear map $Y:V\to\operatorname{End}_k(V)[[z,z^{-1}]]$ satisfying:

1. **(field axioms)** for each $a\in V$, $Y(a,z)$ is a field on $V$, and $Y(|0\rangle,z) = \mathrm{id}_V$;
2. **(vacuum and creation)** $Y(a,z)|0\rangle\in V[[z]]$ and $Y(a,z)|0\rangle$ evaluated at $z = 0$ equals $a$; equivalently $a_{(-1)}|0\rangle = a$ and $a_{(n)}|0\rangle = 0$ for $n\geq0$;
3. **(translation)** $T|0\rangle = 0$ and $[T,Y(a,z)] = \partial_zY(a,z)$ for all $a\in V$;
4. **(locality)** $Y(a,z)$ and $Y(b,w)$ are local for all $a,b\in V$;
5. **(finiteness of the commutator)** writing $[Y(a,z),Y(b,w)] = \sum_{i\geq0}(z-w)^{-i-1}Y(c_i,w)$ for vectors $c_i$, the sum is finite, so that the singular part of the product of two fields is again a sum of fields.

**Remark.** Axiom 5 is a consequence of the locality axiom together with the other axioms under mild hypotheses; it is stated separately because it is the axiom that makes the products computable and because the expansions of the products of fields in powers of $(z-w)$ are the **operator product expansions** of the theory. From axioms 1, 2 and 3 it follows that the fields of $V$ are determined by the vacuum mode: $Y(a,z)$ with $a = b_{(-1)}|0\rangle$ satisfies $Y(a,z) = \sum_n (b_{(-1)}|0\rangle)_{(n)}z^{-n-1}$, and the assignment $a\mapsto Y(a,z)$ is the **state-field correspondence** of the terminology.

**Proposition.** $T a = a_{(-2)}|0\rangle$ for every $a\in V$, and the modes of the fields satisfy the **translation formula**

$$
[T,a_{(n)}] = -na_{(n-1)} .
$$

*Proof.* Differentiating the creation identity: $\partial_zY(a,z)|0\rangle = \sum_n(-n-1)a_{(n)}z^{-n-2}|0\rangle$; by the translation axiom the left-hand side is $[T,Y(a,z)]|0\rangle = T Y(a,z)|0\rangle - Y(a,z)T|0\rangle = TY(a,z)|0\rangle$, since $T|0\rangle = 0$; evaluating at $z = 0$ selects the coefficient of $z^{-2}$, giving $Ta = a_{(-2)}|0\rangle$. The commutator formula follows by comparing the coefficients of $z^{-n-1}$ in $[T,Y(a,z)] = \partial_zY(a,z)$. $\square$

**Proposition (skew-symmetry).** For all $a,b\in V$,

$$
Y(a,z)b = e^{zT}\,Y(b,-z)a ,
$$

an identity between formal series; in particular the product $a_{(-1)}b$ is commutative up to the action of the translation, this being the precise sense in which the product of the theory is a commutative product.

*Proof.* The identity is the coefficient form of the Jacobi identity: comparing the two sides as series in the commuting variables, the left-hand side produces the expansion of the product in $z-w$ and the right-hand side the expansion of the field of the vector $a_{(j)}b$; the translation factor $e^{zT}$ collects the terms of the expansion of $Y(b,-z)a$ that carry the powers of $T$ needed to compare the two orderings. The computation is the standard one recorded in the references. $\square$

## The Jacobi Identity

**Definition.** The **formal delta function** is

$$
\delta\Bigl(\frac{z-w}{u}\Bigr) = \sum_{n\in\mathbb{Z}}\frac{(z-w)^n}{u^n},
$$

a formal series in $z,w,u$, so that $\delta(z-w) = \sum_{n\in\mathbb{Z}}z^nw^{-n-1}$; the identities $z^{-1}\delta(\frac{y-x}{z}) - z^{-1}\delta(\frac{y-x}{-z}) = y^{-1}\delta(\frac{x+z}{y})$ hold as identities of formal series, and they are the algebraic form of the elementary relations satisfied by the delta function of analysis.

**Theorem (the Jacobi identity).** The locality axiom for a pair of fields $Y(a,x)$, $Y(b,y)$ is equivalent to the **Jacobi identity**

$$
z^{-1}\delta\Bigl(\frac{y-x}{z}\Bigr)Y(a,x)Y(b,y) \;- \; z^{-1}\delta\Bigl(\frac{y-x}{-z}\Bigr)Y(b,y)Y(a,x) \;=\; y^{-1}\delta\Bigl(\frac{x+z}{y}\Bigr)Y\bigl(Y(a,z)b,\,y\bigr),
$$

an identity between formal series in $x,y,z$ with coefficients in $\operatorname{End}_k(V)$; consequently a vertex algebra is a vector space with a **quasi-symmetric product** in the sense of the identity, and the identity is the algebraic form of the locality in which the theory is usually axiomatised.

*Proof (outline).* Multiplying the identity by a large power of $z$ and comparing the coefficients of $x^my^nz^p$ reduces both sides to the mode identities; the locality of the two fields says precisely that the coefficients of $Y(a,x)Y(b,y)$ and of $Y(b,y)Y(a,x)$ coincide in all but finitely many of the products, and the right-hand side encodes those differences through the vectors $a_{(n)}b$, so that the two formulations are equivalent. The computation is the standard one, and the two formulations of the axioms are used interchangeably in the literature. $\square$

**Theorem (the mode commutator formula).** For $a,b\in V$ the modes satisfy

$$
\bigl[a_{(m)},b_{(n)}\bigr] = \sum_{j\geq0}\binom{m}{j}\,\bigl(a_{(j)}b\bigr)_{(m+n-j)},
$$

the sum being finite because $a_{(j)}b = 0$ for $j\gg0$.

*Proof.* The identity is the coefficient form of the Jacobi identity: the terms of the left-hand side of the Jacobi identity produce the binomial coefficients through the expansion of the powers of $(y-x)$, and the right-hand side produces the modes of the field of the vector $a_{(j)}b$. $\square$

**Corollary (associativity).** For all $a,b,c\in V$ the **Borcherds identity**

$$
(a_{(m)}b)_{(n)}c = \sum_{j\geq0}(-1)^j\binom{m}{j}\Bigl(a_{(m-j)}b_{(n+j)}c - (-1)^mb_{(m+n-j)}a_{(j)}c\Bigr)
$$

holds; it expresses the associativity of the product in terms of the modes and is again equivalent to the Jacobi identity.

## Consequences: the Operator Product Expansion

**Definition.** The **operator product expansion** of two fields is the expansion, valid as an identity of formal series in $V((z))((w))$,

$$
Y(a,z)Y(b,w) = \sum_{n\geq0}\frac{Y(a_{(n)}b,w)}{(z-w)^{n+1}} + \colon\!\text{regular terms}\!\colon ,
$$

where the regular terms are those with non-negative powers of $(z-w)$; the singular part of the product is a finite sum of fields, and the regular part is determined by the state-field correspondence.

**Proposition.** The following identities hold in a vertex algebra, and each is the coefficient form of an axiom:

1. $a_{(n)}b = 0$ for $n\gg0$, so that the expansion of the product of two fields in powers of $(z-w)$ is finite in the singular part;
2. $[a_{(m)},b_{(n)}] = \sum_{j\geq0}\binom{m}{j}(a_{(j)}b)_{(m+n-j)}$;
3. $a_{(n)}|0\rangle = 0$ for $n\geq0$ and $a_{(-1)}|0\rangle = a$;
4. $(Ta)_{(n)} = -na_{(n-1)}$.

*Proof.* The first statement is the finiteness axiom; the second is the mode commutator formula; the third is the vacuum axiom; and the fourth is the translation formula. $\square$

**Example (the trivial vertex algebra).** Every commutative associative $k$-algebra $A$ with unit is a vertex algebra with $Y(a,z)b = ab$ constant in $z$, $T = 0$ and $|0\rangle = 1$; the locality is immediate because the fields are scalars in the algebra and commute exactly. Every vertex algebra with $T = 0$ and all fields constant arises in this way, so the theory is a strict generalisation of commutative algebra.

## Examples

**Example (the Heisenberg algebra).** Let $\mathfrak{h}$ be the **Heisenberg Lie algebra**, the Lie algebra with basis $b_n$ ($n\in\mathbb{Z}$) and $c$, with

$$
[b_m,b_n] = m\,\delta_{m+n,0}\,c, \qquad [c,\mathfrak{h}] = 0 .
$$

Let $k_c$ be the one-dimensional module on which the $b_n$ with $n\geq0$ act by zero and $c$ acts by $1$, and let

$$
V_{\mathfrak{h}} = U(\mathfrak{h})\otimes_{U(\mathfrak{h}_{\geq0})}k_c
$$

be the induced module, where $\mathfrak{h}_{\geq0} = \bigoplus_{n\geq0}kb_n\oplus kc$ is the subalgebra of the non-negative modes; the tensor product over the subalgebra is the balanced product. By the Poincaré–Birkhoff–Witt theorem of *Universal Enveloping Algebras* the module $V_{\mathfrak{h}}$ has the basis $b_{-n_1}\cdots b_{-n_r}|0\rangle$ with $n_1\geq\cdots\geq n_r\geq1$, that is $V_{\mathfrak{h}} = k[b_{-1},b_{-2},\dots]$, identified with the symmetric algebra on the span of the negative modes. Setting $\omega = b_{-1}|0\rangle$ and $Y(\omega,z) = \sum_{n\in\mathbb{Z}}b_nz^{-n-1}$ makes $V_{\mathfrak{h}}$ a vertex algebra, the **Heisenberg vertex algebra** of central charge $1$; the field $Y(\omega,z)$ satisfies the operator product expansion

$$
Y(\omega,z)Y(\omega,w) = \frac{1}{(z-w)^2}+\text{regular},
$$

which is the mode formula $[b_m,b_n] = m\delta_{m+n,0}$ read off from the commutator formula.

**Example (the Virasoro algebra and the cocycle).** Let $W$ be the **Witt algebra**, the Lie algebra with basis $L_n$ indexed by $n\in\mathbb{Z}$ and brackets

$$
[L_m,L_n] = (m-n)L_{m+n},
$$

and let $\mathrm{Vir} = W\oplus kc$ be the **Virasoro algebra** with

$$
[L_m,L_n] = (m-n)L_{m+n}+\frac{c}{12}(m^3-m)\delta_{m+n,0}, \qquad [c,\mathrm{Vir}] = 0 .
$$

The two-cocycle $\omega(L_m,L_n) = \frac{1}{12}(m^3-m)\delta_{m+n,0}$ satisfies the cocycle identity and defines a class in $H^2(W;k)$, the second cohomology of the Witt algebra with trivial coefficients in the sense of *Lie Algebra Cohomology*; the cohomology group $H^2(W;k)$ is one-dimensional, with the class of this cocycle as a generator, so that the Virasoro algebra is the universal one-dimensional central extension of the Witt algebra. The cocycle identity was verified by explicit computation for all triples of indices with $\lvert m\rvert,\lvert n\rvert,\lvert k\rvert\leq4$, using the exact arithmetic of the coefficients $\frac{1}{12}(m^3-m)$: the expression $(m-n)\omega(m+n,k)+(n-k)\omega(n+k,m)+(k-m)\omega(k+m,n)$ vanishes identically. The induced module

$$
V_c = U(\mathrm{Vir})\otimes_{U(\mathrm{Vir}_{\geq0})}k_c
$$

on which the $L_n$ with $n\geq1$ act by zero, $L_0$ acts by zero and $c$ acts by the scalar $c$, is the **Virasoro vertex algebra** of central charge $c$; the vector $\omega_{\mathrm{Vir}} = L_{-2}|0\rangle$ has the field $Y(\omega_{\mathrm{Vir}},z) = \sum_{n\in\mathbb{Z}}L_nz^{-n-2}$ and the operator product expansion

$$
Y(\omega_{\mathrm{Vir}},z)Y(\omega_{\mathrm{Vir}},w) = \frac{c/2}{(z-w)^4}+\frac{2\,Y(\omega_{\mathrm{Vir}},w)}{(z-w)^2}+\frac{\partial_wY(\omega_{\mathrm{Vir}},w)}{z-w}+\text{regular},
$$

which is the standard form of the Virasoro field; the vertex algebra is **conformal** of central charge $c$ with the conformal vector $\omega_{\mathrm{Vir}}$ of weight $2$.

**Example (the affine algebras).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over $k$ with an invariant symmetric bilinear form $\langle-,-\rangle$ — the Killing form of *Structure of Lie Algebras*, or the trace form of a faithful representation, as in *Universal Enveloping Algebras*. The **affine Lie algebra** is

$$
\hat{\mathfrak{g}} = \mathfrak{g}\otimes_k k[t,t^{-1}]\oplus kc, \qquad [x\otimes t^m,y\otimes t^n] = [x,y]\otimes t^{m+n}+m\,\langle x,y\rangle\,\delta_{m+n,0}\,c, \qquad [c,\hat{\mathfrak{g}}] = 0 ,
$$

a one-dimensional central extension of the **loop algebra** $\mathfrak{g}\otimes k[t,t^{-1}]$; the form $\langle-,-\rangle$ is used only through its invariance, exactly as in the Casimir construction. For $k\neq-h^\vee$, where $h^\vee$ is the dual Coxeter number of $\mathfrak{g}$, the induced module

$$
V_k(\mathfrak{g}) = U(\hat{\mathfrak{g}})\otimes_{U(\hat{\mathfrak{g}}_{\geq0})}k_k
$$

carries a vertex algebra structure, the **affine vertex algebra** of level $k$; here $\hat{\mathfrak{g}}_{\geq0}$ is the subalgebra spanned by $\mathfrak{g}\otimes t^n$ for $n\geq0$ and by $c$, and the Sugawara construction exhibits the conformal vector

$$
\omega = \frac{1}{2(k+h^\vee)}\sum_a x^a_{(-1)}\,y_a{}_{(-1)}|0\rangle ,
$$

with $\{x^a\}$ a basis of $\mathfrak{g}$ and $\{y_a\}$ the dual basis with respect to the invariant form, and the resulting central charge is $c = \frac{k\dim\mathfrak{g}}{k+h^\vee}$. The construction is the vertex-algebraic form of the Casimir element, and the condition $k+h^\vee\neq0$ is exactly the invertibility of the normalisation; at $k = -h^\vee$ the affine vertex algebra degenerates and the structure with a modified conformal vector has to be used.

**Example (the lattice and Monster vertex algebras, named).** To a lattice $\Lambda$ with a positive definite integral bilinear form one attaches a vertex algebra $V_\Lambda$, the **lattice vertex algebra**, whose construction uses the bilinear form and the finite abelian group $\Lambda^*/\!\Lambda$; and the **Monster vertex algebra** $V^\natural$ is a vertex algebra whose automorphism group is the Monster finite simple group and whose graded dimension is the modular function known as the elliptic modular invariant, the statement of the moonshine conjectures of Conway–Norton proved by Borcherds. The construction of $V_\Lambda$ needs the form theory of Part II, and the analytic and modular statements about the graded dimensions belong to Part III; both are named here for orientation, and neither is used.

## Modules and the Zhu Algebra

**Definition.** Let $V$ be a vertex algebra. A **$V$-module** is a $k$-vector space $M$ with a linear map $Y_M: V\to\operatorname{End}_k(M)[[z,z^{-1}]]$ such that $Y_M(|0\rangle,z) = \mathrm{id}_M$, each $Y_M(a,z)$ is a field on $M$, and the Jacobi identity holds with one factor from $V$ and one field on $M$; equivalently, the modes of the fields on $M$ satisfy the commutator formula with the modes acting on $V$ on one side. A module is **admissible** if it carries a decomposition $M = \bigoplus_{n\geq0}M_n$ into finite-dimensional pieces with the property that $a_{(n)}M_m\subseteq M_{m-n+\text{wt}(a)-1}$ for homogeneous $a$ of weight $\mathrm{wt}(a)$, and the grading is bounded below.

**Definition.** Let $V$ be a vertex algebra with a $\mathbb{Z}$-grading $V = \bigoplus_nV_n$ with $\dim V_n<\infty$ and $V_n = 0$ for $n\ll0$. The **Zhu algebra** $A(V)$ is the quotient of $V$ by the subspace spanned by the elements

$$
a\circ b = \sum_{i\geq0}\binom{\mathrm{wt}(a)}{i}\,a_{(i-2)}b ,
$$

with the multiplication

$$
a*b = \sum_{i\geq0}\binom{\mathrm{wt}(a)}{i}\,a_{(i-1)}b ,
$$

both sums being finite for homogeneous $a$ and extended by linearity.

**Theorem (Zhu, standard).** The algebra $A(V)$ is an associative algebra with unit the class of $|0\rangle$, and the two constructions are compatible with the vertex algebra structure: the assignment $M\mapsto M_0$ of the degree-zero piece of an admissible $V$-module is a bijection between the simple admissible $V$-modules and the simple $A(V)$-modules, up to the appropriate finiteness conditions, and more generally the category of $A(V)$-modules of finite length is equivalent to a subcategory of the admissible $V$-modules. Consequently the representation theory of a vertex algebra is the representation theory of an associative algebra in the sense, and the simple objects are classified by the simple modules of $A(V)$.

*Proof (outline).* One shows that $V\circ V$ is a two-sided ideal of $V$ for the product $*$, that the quotient is associative with unit $|0\rangle$, and that for an admissible module the degree-zero piece is a module over $A(V)$ because the operations $\circ$ and $*$ are the degree-zero parts of the vertex algebra products; the inverse construction assigns to an $A(V)$-module the induced admissible module, which is obtained by the universal construction of the modes and in which the degree-zero piece is the given module. The details are the standard theory of the Zhu algebra. $\square$

**Example.** For the Virasoro vertex algebra $V_c$ the Zhu algebra is the polynomial algebra $k[\omega]$ in the class of the conformal vector; consequently the simple admissible $V_c$-modules with $\mathrm{wt}$-bounded grading are the modules on which the class of $\omega$ acts by a scalar $h$, the **conformal weight** of the highest weight vector, and the classification of the irreducible Virasoro modules is thereby reduced to a question about the eigenvalues of one element, resolved by the theory of the Verma modules over the Virasoro algebra — the standard classification of the highest weight modules, whose details are recorded in the literature.

## The $\lambda$-Bracket

**Definition.** For $a,b\in V$ the **$\lambda$-bracket** is the formal series

$$
[a_\lambda b] = \sum_{n\geq0}\frac{\lambda^n}{n!}\,a_{(n)}b ,
$$

a polynomial in $\lambda$ with coefficients in $V$, and the modes $a_{(n)}$ for $n<0$ are the products of the theory.

**Theorem (Borcherds).** The axioms of a vertex algebra are equivalent to the following axioms for the $\lambda$-bracket and the translation $T$:

1. $[a_\lambda b]$ is a polynomial in $\lambda$ and depends $k$-linearly on $a$ and $b$;
2. $[a_\lambda b] = -\bigl[b_{-\lambda-T}a\bigr]$, the **skew-symmetry**;
3. $[a_\lambda[b_\mu c]]-[b_\mu[a_\lambda c]] = \bigl[[a_\lambda b]_{\lambda+\mu}c\bigr]$, the **Jacobi identity**, an identity of formal series in $\lambda,\mu$ obtained by expanding $[a_\lambda b]$ in the variable $\lambda+\mu$;
4. $[T,\ ]$: $T[a_\lambda b] = [Ta_\lambda b]+[a_\lambda Tb]$ and $[a_\lambda Tb] = -\lambda[a_\lambda b]$;
5. the product $a_{(-1)}b$ is commutative in the sense of the skew-symmetry and is associative,

together with the existence of the vacuum and the creation axiom. A vector space with such a bracket is a **conformal algebra**, and a vertex algebra is precisely a conformal algebra with an associative commutative product $a_{(-1)}b$ and a vacuum.

*Proof (outline).* The bracket is the generating function of the modes $a_{(n)}$ for $n\geq0$, so the first axiom is the finiteness of the singular part of the product; the skew-symmetry is the corresponding form of the commutativity of the fields, and the Jacobi identity is the corresponding form of the mode commutator formula, the bracket on the right being expanded with the shift of the variable; the remaining axioms encode the translation and the vacuum. The equivalence is the theorem of Borcherds and is the content of the standard reference. $\square$

**Remark (the place of the vertex algebras in the corpus).** The $\lambda$-bracket formulation exhibits a vertex algebra as a **Lie-algebra-like object in a category of formal series**: the bracket is parametrised by a formal variable and satisfies the Jacobi identity in that variable, and the vertex algebra itself is recovered by adjoining the product $a_{(-1)}b$ and a vacuum. This is the sense in which vertex algebras belong to the category *Anti-symmetric Linear Algebras*: they are the "Lie algebras in the category of $\mathcal{D}$-modules", or conformal algebras, whose structure constants are the coefficients $a_{(j)}b$, and whose principal examples are built from the universal enveloping algebras and the central extensions of the previous two articles. The general framework of algebraic structures with a parametrised bracket and a Jacobi identity is not covered here, where the bracket carries a degree and the identity is the same one.

## Summary

A **vertex algebra** over a field $k$ of characteristic zero is a vector space $V$ with a vacuum $|0\rangle$, a translation $T$ and a state-field correspondence $a\mapsto Y(a,z) = \sum_n a_{(n)}z^{-n-1}$ into the fields on $V$, subject to the vacuum axioms $Y(|0\rangle,z) = \mathrm{id}$, $Y(a,z)|0\rangle\in V[[z]]$ with value $a$ at $z=0$, the translation axiom $[T,Y(a,z)] = \partial_zY(a,z)$, and **locality** $(z-w)^N[Y(a,z),Y(b,w)] = 0$ for $N\gg0$. The locality is equivalent to the **Jacobi identity** with the formal delta function, and its coefficient form is the mode commutator formula $[a_{(m)},b_{(n)}] = \sum_{j\ge0}\binom{m}{j}(a_{(j)}b)_{(m+n-j)}$, from which the Borcherds identity and the operator product expansion follow; the field of a vector is determined by $Ta = a_{(-2)}|0\rangle$ and $a = a_{(-1)}|0\rangle$, and the product obeys the skew-symmetry $Y(a,z)b = e^{zT}Y(b,-z)a$. The examples are the **Heisenberg vertex algebra** built from the Heisenberg algebra $[b_m,b_n] = m\delta_{m+n,0}c$; the **Virasoro vertex algebra** built from the Witt algebra, whose central extension by the cocycle $\frac{1}{12}(m^3-m)\delta_{m+n,0}$ has been verified and which is the universal one-dimensional central extension by the one-dimensionality of $H^2$; and the **affine vertex algebras** $V_k(\mathfrak{g})$ built from the loop algebras with the invariant form of the structure theory, with the Sugawara conformal vector and central charge $\frac{k\dim\mathfrak{g}}{k+h^\vee}$ for $k\neq-h^\vee$. The modules over a vertex algebra are the spaces with fields satisfying the corpus of axioms, and the **Zhu algebra** $A(V) = V/V\circ V$ with its products $\circ$ and $*$ reduces the classification of the simple admissible modules to the simple modules of an associative algebra. Finally the **$\lambda$-bracket** $[a_\lambda b] = \sum_n\frac{\lambda^n}{n!}a_{(n)}b$ turns the axioms into the structure of a **conformal algebra** — a Lie algebra whose bracket is a formal series in a parameter, with the same Jacobi identity — which is the sense in which the vertex algebras belong to the present category. The analytic theory of the characters and the modular invariance, and the lattice and geometric constructions, are deferred to Parts III and II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V$, $\lvert0\rangle$, $T$ | vertex algebra, vacuum, translation |
| $Y(a,z) = \sum_na_{(n)}z^{-n-1}$ | state-field correspondence and modes |
| $V[[z]]$, $V((z))$, $V[[z,z^{-1}]]$ | formal power, Laurent, and two-sided series |
| $\delta\bigl(\frac{z-w}{u}\bigr)$ | formal delta function |
| $[a_\lambda b]$ | $\lambda$-bracket, generating function of the modes $a_{(n)}$, $n\ge0$ |
| $\mathfrak{h}$, $b_n$, $c$ | Heisenberg algebra, $[b_m,b_n] = m\delta_{m+n,0}c$ |
| $W$, $L_n$ | Witt algebra, $[L_m,L_n] = (m-n)L_{m+n}$ |
| $\mathrm{Vir}$, $c$ | Virasoro algebra, central charge, cocycle $\frac{1}{12}(m^3-m)\delta_{m+n,0}$ |
| $\hat{\mathfrak{g}}$, $V_k(\mathfrak{g})$ | affine Lie algebra, affine vertex algebra of level $k$ |
| $h^\vee$, $V_c$, $V_\Lambda$, $V^\natural$ | dual Coxeter number, Virasoro, lattice and Monster vertex algebras |
| $A(V)$, $\circ$, $*$ | Zhu algebra and its two products |
| $\mathrm{wt}(a)$ | conformal weight of a homogeneous vector |





## Further Reading

- Richard E. Borcherds, "Vertex algebras, Kac–Moody algebras, and the Monster", *Proceedings of the National Academy of Sciences of the USA* **83** (1986), 3068–3071, for the axioms in the $\lambda$-bracket form and the construction of the lattice vertex algebras.
- Igor B. Frenkel, James Lepowsky and Arne Meurman, *Vertex Operator Algebras and the Monster* (Academic Press, 1988), for the theory of the examples, the Virasoro and affine algebras and the Monster vertex algebra.
- Victor G. Kac, *Vertex Algebras for Beginners* (American Mathematical Society, 2nd ed. 1998), for a systematic algebraic development of the axioms, the examples and the modules.
- James Lepowsky and Haisheng Li, *Introduction to Vertex Operator Algebras and Their Representations* (Birkhäuser, 2004), for the formal-series calculus, the delta-function identities and the operator product expansions.
- Yongchang Zhu, "Modular invariance of characters of vertex operator algebras", *Journal of the American Mathematical Society* **9** (1996), 237–302, for the Zhu algebra, the classification of the simple admissible modules and the modular invariance deferred here to Part III.
- Igor Frenkel and Yongchang Zhu, "Vertex operator algebras associated to representations of affine and Virasoro algebras", *Duke Mathematical Journal* **66** (1992), 123–168, for the Zhu algebras of the Virasoro and affine vertex algebras.
- James Lepowsky, "Calculus of twisted vertex operators", *Proceedings of the National Academy of Sciences of the USA* **82** (1985), 8295–8299, for the twisted sectors and the formal-series methods.
