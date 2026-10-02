
# __The Signed Left Multiplication on a Clifford Algebra__

## Introduction

The left multiplication $L_a$ of a Clifford algebra acts by $y\mapsto ay$, and it is multiplicative in the written order. Composing it with the grade involution gives the **signed left multiplication**

$$
\mathrm{L}^{\alpha}_a = L_a\circ\alpha , \qquad \mathrm{L}^{\alpha}_a(y) = a\,\alpha(y) ,
$$

the ordinary left multiplication applied to the twisted argument. It agrees with $L_a$ on the even part of the algebra and is $-L_a$ there where the argument is odd; it composes according to $L_{a\alpha(c)}$, so two signed left multiplications multiply to an ordinary one; and it is one half of the signed sandwich of *The Signed Sandwich on a Clifford Algebra*, the other half being an ordinary right multiplication. The article treats this operator, its fixed elements, and the precise sense in which a one-sided operator is half a motion of the quadratic space.

A word of disambiguation begins the account, because the corpus writes two different operators with the adjective signed in front of "left multiplication". In this article the twist is on the **argument**, $\mathrm{L}^{\alpha}_a=L_a\alpha$; in *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* and *The Graded Multiplication Operators* the twist is on the **parameter**, $\Lambda^{\alpha}_x(y)=\alpha(x)y$. The two agree only on the even part, and their purposes differ: the parameter twist belongs to the inner conjugation and the versor theory, the argument twist to the signed product and the reflections. Only the argument twist is treated here.

**The boundaries.** The one-sided calculus, the commutant and the composition of the ordinary families are *One-Sided Operators on a Clifford Algebra*; the signed product, its composition law and its fixed elements are *One-Sided Operators with the Signed Product*, and the two-sided version is *Two-Sided Operators with the Signed Product*; the parameter-twisted family is *The Graded Multiplication Operators*. The signed sandwich formed from the two factors is *The Signed Sandwich on a Clifford Algebra*, and the reflections are *Reflections as Signed Two-Sided Operators on a Clifford Algebra*. The base is a field $F$ of characteristic not $2$, $q$ a non-degenerate quadratic form with $q(u)=B(u,u)$ and $uv+vu=2B(u,v)$.

## The Operator

### Definition and Elementary Properties

**Definition.** For $a\in\mathrm{Cl}(V,q)$ the **signed left multiplication** is the $F$-linear operator

$$
\mathrm{L}^{\alpha}_a = L_a\circ\alpha : \mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q), \qquad \mathrm{L}^{\alpha}_a(y) = a\,\alpha(y) .
$$

**Proposition.** The following hold.

**(a)** $\mathrm{L}^{\alpha}_a = L_a\alpha = \alpha L_{\alpha(a)}$.

**(b)** For a homogeneous element $a$ of degree $k$ one has $\mathrm{L}^{\alpha}_a = (-1)^{k}L_a$ on the odd part of the algebra and $\mathrm{L}^{\alpha}_a = L_a$ on the even part.

**(c)** $\mathrm{L}^{\alpha}_1 = \alpha$, and $\mathrm{L}^{\alpha}_a$ is invertible exactly when $a$ is a unit.

**(d)** $\mathrm{L}^{\alpha}_a$ is a homogeneous operator of parity $|a|$.

**Proof.** (a) is $\alpha L_{\alpha(a)}(y)=\alpha(\alpha(a)y)=a\alpha(y)$. (b) For $y$ homogeneous of degree $j$, $\alpha(y)=(-1)^jy$; on the even part $j=0$ and on the odd part $j=1$, so the operator differs from $L_a$ by $-1$ on the odd part. (c) is the value at $1$ and the invertibility of $L_a$. (d) The shift of the grading is that of $L_a$, because $\alpha$ preserves the grading.

**Remark.** The operator $\mathrm{L}^{\alpha}_a$ is the composition of a multiplication operator with the parity operator $\Gamma(y)=\alpha(y)$; it is therefore the conjugate $L_a\alpha=\Gamma L_{\alpha(a)}\Gamma$, and the twisting enters through $\Gamma$, as *The Graded Multiplication Operators* records for the parameter-twisted family. Since $\Gamma$ is an involution that is the identity on the even part, every statement about $\mathrm{L}^{\alpha}_a$ is a statement about $L_a$ read separately on the two parity components.

### Composition and Fixed Elements

**Proposition (composition).** For all $a,c$,

$$
\mathrm{L}^{\alpha}_a\circ\mathrm{L}^{\alpha}_c = L_{a\alpha(c)} ,
\qquad
\mathrm{L}^{\alpha}_a\circ L_c = \mathrm{L}^{\alpha}_{ac} ,
\qquad
L_a\circ\mathrm{L}^{\alpha}_c = \mathrm{L}^{\alpha}_{a\alpha(c)} .
$$

Two signed left multiplications compose to an **ordinary** left multiplication, the two grade involutions cancelling; a signed and an ordinary one compose to a signed one. The signed left family is therefore a coset $L(\Gamma)\alpha$ of the group of invertible left multiplications and not a group, exactly as for the two-sided family.

**Proof.** $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c=L_a\alpha L_c\alpha=L_aL_{\alpha(c)}\alpha^2=L_{a\alpha(c)}$; the other two are the same computation with one factor untwisted.

**Proposition (the fixed elements).** The fixed space of $\mathrm{L}^{\alpha}_a$ is $\{y : a\alpha(y)=y\}$. For the scalar $a=\lambda$ it is the even part for $\lambda=1$, the odd part for $\lambda=-1$, and $\{0\}$ for every other $\lambda$. For a general $a$ it is the translate of a subspace by the equation $a\alpha(y)=y$, and it is not a graded subspace unless $a$ is scalar or the equation degenerates.

**Proof.** The defining equation is linear in $y$; for $a=\lambda$ it reads $\lambda\alpha(y)=y$, which on the even component is $(\lambda-1)y=0$ and on the odd component is $(-\lambda-1)y=0$, giving the three cases. The general case is the same equation with a non-scalar coefficient, and its solution space is not stable under the grading because $a$ need not be even.

## The Operator as Half a Motion

**Proposition (the pairing with the right factor).** For a unit $x$ the composition of the signed left multiplication with the ordinary right multiplication by the inverse of the twisted parameter is the signed sandwich,

$$
\mathrm{L}^{\alpha}_x\circ R_{\alpha(x)^{-1}} = T^{\alpha}_{x,\alpha(x)^{-1}} ,
$$

and for a vector $u$ with $q(u)\ne0$ this is the reflection $\rho_u$; the signed left multiplication alone is not a motion of $V$.

**Proof.** $(\mathrm{L}^{\alpha}_xR_{\alpha(x)^{-1}})(y)=x\alpha(y)\alpha(x)^{-1}$, which is the signed sandwich of *The Signed Sandwich on a Clifford Algebra* with parameters $(x,\alpha(x)^{-1})$; for $x=u$ a vector, $\alpha(u)^{-1}=u^{-1}$, and the reflection formula gives $\rho_u$. The last claim is the next proposition.

**Proposition (no one-sided operator preserves the space).** Let $u\in V$ with $q(u)\ne0$. Then $\mathrm{L}^{\alpha}_u$ does not map $V$ into itself: it sends the unit $1$ to $u$ and the vector $u$ to $u\alpha(u)=-q(u)$, a scalar, so the image of the even part of the algebra meets the odd part and vice versa. Consequently no signed left multiplication by a non-scalar element preserves the quadratic space.

**Proof.** $\mathrm{L}^{\alpha}_u(1)=u$ and $\mathrm{L}^{\alpha}_u(u)=u\,(-u)=-q(u)\in F$; the two values lie in different parity components, so $\mathrm{L}^{\alpha}_u$ does not preserve the subspace $V$ of the algebra. A one-sided multiplication by $a$ preserves the parity grading only when $a$ is even, and then it does not preserve $V$ either unless $a$ is a scalar.

**Remark (the geometry of the pairing).** The signed left multiplication is the left half of the signed sandwich, and only the pairing with a right multiplication restores the grading and produces an operator of $V$. This is the one-sided form of the statement that the reflections are two-sided operators, and it is why the geometry of the category is carried by the two-sided family. The parameter-twisted signed left multiplication of *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* has the same one-sided deficiency, and the pairing there is with the inverse right multiplication.

## Worked Cases

### A Vector in the Negative-Definite Three-Space

For $V$ of dimension three with $e_j^2=-1$ and $u=e_1$, the operator $\mathrm{L}^{\alpha}_{e_1}$ sends $1\mapsto e_1$, $e_1\mapsto -e_1^2=1$, $e_2\mapsto e_1(-e_2)=-e_1e_2$; the even and odd parts are exchanged, and the image is not contained in $V$. The pairing with $R_{e_1^{-1}}=R_{-e_1}$ returns the reflection $\rho_{e_1}$ of the previous article.

### The Scalar $-1$

For $a=-1$ the operator is $\mathrm{L}^{\alpha}_{-1}(y)=-\alpha(y)$, which is the identity on the odd part and minus the identity on the even part: the fixed space is the odd part, an example of the fixed-element proposition, and the operator is an involution.

### An Even Element

For $a=x=e_1e_2$, even, $\mathrm{L}^{\alpha}_x=L_x$ because $\alpha$ is the identity on the even part; the signed and the ordinary left multiplications coincide, and the pairing with $R_{x^{-1}}$ is the inner conjugation $\mathrm{Ad}_x$, a rotation of the plane. The signed family differs from the ordinary one only through the odd parameters, which is where the reflections live.

## Summary

The **signed left multiplication** $\mathrm{L}^{\alpha}_a=L_a\circ\alpha$, $\mathrm{L}^{\alpha}_a(y)=a\alpha(y)$, is the ordinary left multiplication of the twisted argument; it satisfies $\mathrm{L}^{\alpha}_a=\alpha L_{\alpha(a)}$, it coincides with $L_a$ on the even part of the algebra and is $-L_a$ on the odd part, it is invertible exactly for units, and it has the parity of $a$. Its products satisfy $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c=L_{a\alpha(c)}$, so the signed left family is a **coset** of the group of invertible left multiplications; its fixed space is $\{y : a\alpha(y)=y\}$, which for a scalar is the even part, the odd part or nothing according as the scalar is $1$, $-1$ or neither. The operator is one half of the signed sandwich, $\mathrm{L}^{\alpha}_xR_{\alpha(x)^{-1}}=T^{\alpha}_{x,\alpha(x)^{-1}}$, which for a vector is the reflection $\rho_u$; the signed left multiplication alone never preserves the quadratic space, because it exchanges the two parity components, and only the pairing with a right multiplication restores the grading. The parameter-twisted family $\alpha(x)y$ is a different operator, by *The Graded Multiplication Operators*; the one-sided calculus is *One-Sided Operators on a Clifford Algebra*, and the signed product is *One-Sided Operators with the Signed Product*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{L}^{\alpha}_a=L_a\circ\alpha$ | Signed left multiplication, $y\mapsto a\alpha(y)$ |
| $\Lambda^{\alpha}_x(y)=\alpha(x)y$ | The different parameter-twisted family, not treated here |
| $\mathrm{L}^{\alpha}_a=\alpha L_{\alpha(a)}$ | Relation to the ordinary left multiplication |
| $\mathrm{L}^{\alpha}_a=L_a$ on the even part, $-L_a$ on the odd part | The parity split |
| $\mathrm{L}^{\alpha}_a\mathrm{L}^{\alpha}_c=L_{a\alpha(c)}$ | Composition law; coset of the left-multiplication group |
| $\{y : a\alpha(y)=y\}$ | Fixed space; even part, odd part or nothing for a scalar |
| $\mathrm{L}^{\alpha}_xR_{\alpha(x)^{-1}}=T^{\alpha}_{x,\alpha(x)^{-1}}$ | Pairing to the signed sandwich |
| $\mathrm{L}^{\alpha}_u(1)=u$, $\mathrm{L}^{\alpha}_u(u)=-q(u)$ | Failure to preserve $V$ |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the one-sided operators, the grade involution and their pairings.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the signed one-sided actions and the composition laws in the low-dimensional algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the left and right multiplications twisted by the grading.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the one-sided action and the reason only two-sided operators preserve the vectors.
