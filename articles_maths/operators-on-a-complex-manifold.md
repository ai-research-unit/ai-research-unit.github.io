
# __Operators on a Complex Manifold__

## Introduction

A complex manifold $(M,J)$ carries a chosen form — a Hermitian metric $g$ — and an operator on it is a linear operator on the spaces of functions, of vector fields and of forms that the complex structure and the metric allow. The structure that is intrinsic to $J$ alone is the **type**: the complexified tangent space splits as $T_{\mathbb C}M = T^{1,0}\oplus T^{0,1}$ into the $+i$ and $-i$ eigenvectors of $J$, and every operator is read by the types it raises and lowers. A $\mathbb{C}$-linear operator is **holomorphic** when it commutes with $J$ and **antiholomorphic** when it anticommutes with $J$, that is when it is conjugate-linear; on functions these are the Cauchy–Riemann operators $\partial$ and $\bar\partial$, and on forms the exterior derivative splits as $d = \partial + \bar\partial$, which is the integrability of $J$ seen at the level of operators. The operator layer of the category is the algebra these operators generate, together with the complex structure $J$ itself, and the metric $g$ enters only where an operator is measured against it: the formal adjoints, the codifferential and the Laplacian, which the later articles of the category develop.

The article has four sections: the type decomposition and the operators that respect it; the Cauchy–Riemann operators and the Dolbeault complex; the holomorphic vector fields and the operators commuting with $J$; and the metric and the operators it defines. The complex manifold, the almost complex structure, the type decomposition, the Nijenhuis tensor and the integrability theorem are *Hermitian Geometry and Almost Complex Structures*, and the Hermitian metric, the fundamental form and the Chern connection are the same article and *Kähler Geometry*; none of that is re-derived. The differential forms, the exterior derivative and the de Rham complex are *Differential Forms* and *The Exterior Derivative*; the Riemannian metric, the Levi-Civita connection and the curvature are *Riemannian Geometry*. The Kähler form read as an operator on the exterior algebra is *The Kähler Form Operator*, the curvature operator is *The Curvature Operator of a Complex Manifold*, and the Bergman operator is *The Bergman Operator*, the companion articles. The Hodge theory of the Dolbeault complex and the elliptic-operator finiteness are Part III, where the measure and the limit are available, and no integration is used here.

Throughout, $M$ is a complex manifold of complex dimension $n$ with complex structure $J$, $T_{\mathbb C}M = T^{1,0}M\oplus T^{0,1}M$ is its complexified tangent bundle, $g$ is a Hermitian metric, $\Omega(X,Y) = g(JX,Y)$ is the fundamental form, $\Omega^{p,q}(M)$ is the space of forms of type $(p,q)$, and the operators $\partial$, $\bar\partial$, $d$ act on the exterior algebra of $M$. A local holomorphic frame is written $(\partial_{z^1},\dots,\partial_{z^n})$ with the conjugate frame $(\partial_{\bar z^1},\dots,\partial_{\bar z^n})$.

## The Type Decomposition and the Operators that Respect It

**Definition.** On the complexified tangent space the complex structure has the two eigenvalues $\pm i$, and the eigenspaces
$$
T^{1,0}M = \ker(J - i\,\mathrm{id}), \qquad T^{0,1}M = \ker(J + i\,\mathrm{id}),
$$
are the **holomorphic** and **antiholomorphic** tangent spaces; $T_{\mathbb C}M = T^{1,0}M\oplus T^{0,1}M$ and the two are conjugate, $\overline{T^{1,0}M} = T^{0,1}M$. The **type** of a $k$-form is the pair $(p,q)$ with $p+q = k$ giving its degrees in the two parts; the space of such forms is $\Omega^{p,q}(M)$, and $\Omega^k(M)\otimes\mathbb{C} = \bigoplus_{p+q=k}\Omega^{p,q}(M)$.

**Definition.** A $\mathbb{C}$-linear operator $D$ on the complexified forms is **of type $(r,s)$** when it raises the holomorphic degree by $r$ and the antiholomorphic degree by $s$,
$$
D\bigl(\Omega^{p,q}(M)\bigr) \subseteq \Omega^{p+r,q+s}(M);
$$
it is **holomorphic** when it is of type $(1,0)$, that is when it commutes with $J$ on the underlying tangent directions, and **antiholomorphic** when it is of type $(0,1)$. An operator is **$J$-linear** when it commutes with $J$ and **$J$-antilinear** when it anticommutes with it; over the complexified space the two are the type $(1,0)$ and the type $(0,1)$ cases.

**Proposition (the type is preserved by the structure).** A holomorphic local map $F : M\to N$ of complex manifolds pulls forms back by type, $F^{*}\Omega^{p,q}(N)\subseteq\Omega^{p,q}(M)$, and the Lie bracket of two holomorphic vector fields is holomorphic; the type decomposition is thus intrinsic to the complex structure and independent of the metric.

**Proof.** The pullback acts on the two eigenspaces of $J$ through the differential, and $dF\circ J = J'\circ dF$ preserves the splitting; the bracket statement is the integrability of the almost complex structure, *Hermitian Geometry and Almost Complex Structures*, where the Nijenhuis tensor of a complex manifold vanishes. No metric is used.

**Remark (the metric is not used for the type).** The type decomposition, the Cauchy–Riemann operators and the holomorphic vector fields of the next sections depend only on $J$. The chosen Hermitian metric $g$ enters when an operator is to be adjointed, when lengths are to be measured, or when the two parts of the Laplacian are to be compared; the sections below mark where.

## The Cauchy–Riemann Operators and the Dolbeault Complex

**Definition.** On a smooth function $f : M\to\mathbb{C}$ the **Cauchy–Riemann operators** are the type $(1,0)$ and $(0,1)$ parts of the differential,
$$
\partial f = \tfrac12\bigl(df - i\,df\circ J\bigr), \qquad \bar\partial f = \tfrac12\bigl(df + i\,df\circ J\bigr),
$$
so that $d = \partial + \bar\partial$; a function is **holomorphic** when $\bar\partial f = 0$ and **antiholomorphic** when $\partial f = 0$.

**Proposition (the decomposition of $d$).** On a complex manifold the exterior derivative splits by type,
$$
d = \partial + \bar\partial, \qquad \partial : \Omega^{p,q}\to\Omega^{p+1,q}, \qquad \bar\partial : \Omega^{p,q}\to\Omega^{p,q+1},
$$
and the two components satisfy
$$
\partial^2 = 0, \qquad \bar\partial^2 = 0, \qquad \partial\bar\partial + \bar\partial\partial = 0 .
$$

**Proof.** The decomposition of $d$ by type is the statement that the ideal generated by the $(1,0)$-forms and the ideal generated by the $(0,1)$-forms are each $d$-stable, which holds exactly on a complex manifold, equivalently $N_J = 0$, by *Hermitian Geometry and Almost Complex Structures*. From $0 = d^2 = \partial^2 + (\partial\bar\partial+\bar\partial\partial) + \bar\partial^2$ and the type of each summand, each component vanishes separately.

**Definition.** The **Dolbeault complex** is the complex
$$
0 \longrightarrow \Omega^{p,0} \xrightarrow{\ \bar\partial\ } \Omega^{p,1} \xrightarrow{\ \bar\partial\ } \Omega^{p,2} \xrightarrow{\ \bar\partial\ } \cdots ,
$$
with cohomology the **Dolbeault groups** $H^{p,q}_{\bar\partial}(M) = \ker\bar\partial/\operatorname{im}\bar\partial$ on $\Omega^{p,q}$; the conjugate complex, formed with $\partial$, gives $H^{q,p}(M)$ under complex conjugation of forms.

**Remark.** The operators $\partial$ and $\bar\partial$ are conjugate to one another, $\overline{\bar\partial \alpha} = \partial\bar\alpha$, so the two complexes carry the same information and the antiholomorphic operators are the complex conjugates of the holomorphic ones. The comparison of the two Laplacians,
$$
\Delta_{\bar\partial} = \bar\partial\bar\partial^{*} + \bar\partial^{*}\bar\partial , \qquad \Delta_{\partial} = \partial\partial^{*} + \partial^{*}\partial ,
$$
with ${}^{*}$ the formal adjoint for the metric $g$, needs the chosen form and is the point where the metric enters the operator layer; the finiteness of the Dolbeault cohomology on a compact manifold is the Hodge theory of Part III, quoted and not proved here.

## Holomorphic Vector Fields and the Operators Commuting with $J$

**Definition.** A **holomorphic vector field** is a section $X$ of $T^{1,0}M$, a complex vector field of type $(1,0)$; equivalently, a complex vector field with $[X,\bar Z] = 0$ for every antiholomorphic field $\bar Z$, or $X$ complex-linear and $\mathcal{L}_X J = 0$. The holomorphic vector fields form a Lie algebra $\mathfrak{X}^{1,0}(M)$ under the bracket.

**Proposition (the operators commuting with $J$).** A $\mathbb{C}$-linear operator $D$ on the smooth functions of $M$ commutes with $J$, $D\circ J = J\circ D$ on the differentials, exactly when the one-form it produces from $f$ is of type $(1,0)$; the first-order operators commuting with $J$ are generated by the holomorphic vector fields and the identity, and they form the algebra $\mathfrak{X}^{1,0}(M)\ltimes C^\infty(M,\mathbb{C})$. The operators anticommuting with $J$ are generated by the antiholomorphic fields and are the conjugates of the commuting ones.

**Proof.** A first-order operator with symbol a vector field $X$ commutes with $J$ exactly when $\mathcal{L}_XJ = 0$, that is when $X$ is holomorphic; the bracket of two such fields is again holomorphic by the proposition of the first section, and the constants are the zeroth-order part. Anticommuting operators have conjugate-linear symbol and are the complex conjugates.

**Example (the complex structure itself).** The complex structure $J$ is a $(1,1)$-tensor field and an operator on the tangent bundle with $J^2 = -\mathrm{id}$, isometric for the Hermitian metric, $g(JX,JY) = g(X,Y)$, and skew for the fundamental form, $\Omega(JX,JY) = \Omega(X,Y)$. As an operator on the complexified tangent space it is diagonal with the two eigenvalues $\pm i$, and the type of a form is the number of its holomorphic and antiholomorphic legs; $J$ is a section of $\operatorname{End}(TM)$ whose holonomy is contained in $U(n)$ exactly when the metric is Hermitian and the structure is parallel.

**Example (the flat space).** On $\mathbb{C}^n$ with the standard metric, $J$ is multiplication by $i$, a holomorphic vector field is $\sum f_j\,\partial_{z^j}$ with $f_j$ holomorphic, the two Cauchy–Riemann operators are $\partial = \sum dz^j\wedge\partial_{z^j}$ and $\bar\partial = \sum d\bar z^j\wedge\partial_{\bar z^j}$, and the Dolbeault complex computes the cohomology of the polydisc and, on the projective space, the sheaf cohomology of the structure sheaf, by the theorem of Dolbeault, quoted.

## The Metric and the Operators It Defines

**Definition.** The **Hermitian metric** $g$ is a Riemannian metric on $M$ with $g(JX,JY) = g(X,Y)$; its **fundamental form** is $\Omega(X,Y) = g(JX,Y)$, a real $(1,1)$-form. For a form $\alpha$ the **formal adjoint** $\bar\partial^{*}\alpha$ is the operator defined by
$$
\int_M g(\bar\partial\alpha,\beta)\,dV = \int_M g(\alpha,\bar\partial^{*}\beta)\,dV
$$
for compactly supported forms, $dV$ the volume form of $g$.

**Proposition.** The formal adjoint of $\partial$ is the conjugate of the formal adjoint of $\bar\partial$, $\partial^{*} = \overline{\bar\partial^{*}}$, and the two Laplacians $\Delta_{\partial}$ and $\Delta_{\bar\partial}$ are conjugate; the metric is Kähler, $d\Omega = 0$, exactly when they are equal, and then they equal half the Hodge Laplacian, $\Delta_{\bar\partial} = \tfrac12\Delta_d$.

**Proof.** The adjoint is computed by integrating by parts against $dV$, which uses the chosen metric; conjugating the identity for $\bar\partial$ gives the one for $\partial$. The equality $\Delta_{\partial} = \Delta_{\bar\partial}$ is one of the Kähler identities, whose proof uses $d\Omega = 0$ and the primitivity of the Kähler form, *Kähler Manifolds and the Hermitian Form*, and is quoted here. The last identity is the Kähler identity $\Delta_d = 2\Delta_{\bar\partial}$.

**Remark (what the metric decides).** The type, the Cauchy–Riemann operators, the Dolbeault complex and the holomorphic vector fields are fixed by $J$ alone; the formal adjoints, the codifferential, the Hodge star and the Laplacian are fixed by the metric, and it is here that two Hermitian metrics on the same complex manifold give different operator algebras. This is the sense in which the operator layer of the category is geometric: the holomorphic operators are intrinsic to the complex structure, and the metric chooses the adjoint and the Laplacian that pair them.

## Summary

A complex manifold carries the intrinsic operator layer of its complex structure: the type decomposition $T_{\mathbb C}M = T^{1,0}\oplus T^{0,1}$, the Cauchy–Riemann operators $\partial,\bar\partial$ with $d = \partial+\bar\partial$, $\partial^2 = \bar\partial^2 = \partial\bar\partial+\bar\partial\partial = 0$, the Dolbeault complex and its cohomology, and the holomorphic vector fields, the first-order operators commuting with $J$, which form the algebra $\mathfrak{X}^{1,0}(M)\ltimes C^\infty(M,\mathbb C)$. Holomorphic operators are those of type $(1,0)$ and antiholomorphic those of type $(0,1)$, and the two families are complex conjugates. The chosen Hermitian metric $g$ enters only through the formal adjoints and the Laplacians: it defines $\bar\partial^{*}$ and $\partial^{*} = \overline{\bar\partial^{*}}$, the metric is Kähler exactly when $\Delta_{\partial} = \Delta_{\bar\partial} = \tfrac12\Delta_d$, and different metrics on the same complex manifold give different adjoints. The Dolbeault finiteness and the Hodge theory of the complex are Part III; the Kähler form as an operator, the curvature operator and the Bergman operator are the companion articles of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $J$, $n$ | complex manifold, complex structure, complex dimension |
| $T^{1,0}M$, $T^{0,1}M$ | holomorphic and antiholomorphic tangent spaces, the $\pm i$ eigenbundles |
| $g$, $\Omega(X,Y)=g(JX,Y)$ | Hermitian metric and fundamental form |
| $\Omega^{p,q}(M)$ | forms of type $(p,q)$ |
| $\partial$, $\bar\partial$ | Cauchy–Riemann operators, the type $(1,0)$ and $(0,1)$ parts of $d$ |
| $H^{p,q}_{\bar\partial}(M)$ | Dolbeault cohomology of the $\bar\partial$-complex |
| $\bar\partial^{*}$, $\partial^{*}$ | formal adjoints for the metric $g$ |
| $\Delta_{\partial}$, $\Delta_{\bar\partial}$ | Laplace operators of $\partial$ and $\bar\partial$ |
| $\mathfrak{X}^{1,0}(M)$ | holomorphic vector fields |

## Further Reading

- Kunihiko Kodaira, *Complex Manifolds and Deformation of Complex Structures* (Springer, 1986), for the Dolbeault complex, the holomorphic operators and the deformation theory.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hodge theory of the $\bar\partial$-complex and the Kähler identities.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry II* (Interscience, 1969), for the complex structure as a tensor field, the holomorphic vector fields and the Hermitian and Kähler metrics.
- Raymond O. Wells, *Differential Analysis on Complex Manifolds* (Springer, third edition, 2008), for the Dolbeault operators, the type decomposition and the formal adjoints.
