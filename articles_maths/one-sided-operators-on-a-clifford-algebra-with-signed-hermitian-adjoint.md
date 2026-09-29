# __One-Sided Operators on a Clifford Algebra with Signed Hermitian Adjoint__

## Introduction

Every two-sided operator of *Two-Sided Operators on a Clifford Algebra* is the product of a left multiplication and a right multiplication, and the signed Hermitian sandwich of *Two-Sided Operators on a Clifford Algebra with Signed Hermitian Adjoint* factors accordingly:

$$
\Theta^{\alpha}_x=\Lambda^{\alpha}_x\circ R_{x^{\dagger}},
\qquad
\Lambda^{\alpha}_x(y)=\alpha(x)\,y,\qquad R_{x^{\dagger}}(y)=y\,x^{\dagger}.
$$

The **signed left multiplication** $\Lambda^{\alpha}_x$ is the one that carries the parity sign, and the **dagger right multiplication** $R_{x^{\dagger}}$ is the one that carries the involution of the base. This article treats the two factors separately. It is the Hermitian counterpart of *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, where the right factor is the inverse right multiplication $R_{x^{-1}}$; the general theory of the two one-sided families is *One-Sided Operators on a Clifford Algebra with Hermitian Adjoint* and *One-Sided Operators on a Clifford Algebra*, and nothing of it is reproved.

The two factors have opposite linear behaviour, and that is the first structural fact. The signed left multiplication is defined on the whole algebra and is $\sigma$-free, so it is linear in its parameter, $\Lambda^{\alpha}_{ax}=a\,\Lambda^{\alpha}_x$. The dagger right multiplication is $\sigma$-**semilinear** in its parameter, $R_{(ax)^{\dagger}}=\sigma(a)R_{x^{\dagger}}$, because the dagger is. The product of the two rules is the parameter rule of the two-sided operator,

$$
\Theta^{\alpha}_{ax}=\Lambda^{\alpha}_{ax}R_{(ax)^{\dagger}}=a\,\sigma(a)\,\Lambda^{\alpha}_xR_{x^{\dagger}}=a\,\sigma(a)\,\Theta^{\alpha}_x,
$$

so the semilinearity of the Hermitian family is entirely in the right factor and the sign is entirely in the left one.

The second fact is that the adjoint of each one-sided operator, for the form $(x,y)=\mathrm{Sc}(x^{\dagger}y)$, is the one-sided operator of the dagger: $\Lambda^{\alpha}_x$ has adjoint $\Lambda^{\alpha}_{x^{\dagger}}$, and $R_{x^{\dagger}}$ has adjoint $R_{(x^{\dagger})^{\dagger}}=R_x$. On the unitary slice the adjoint is the inverse, and that is where the one-sided operators become unitary and the whole family collapses.

The algebra, the dagger and the involution of the base are *Involutive Clifford Algebras*; the general two one-sided families, their composition laws, their mutual commutants and the adjoint theorem are *One-Sided Operators on a Clifford Algebra with Hermitian Adjoint*; the two-sided operator and its parameter rule are *Two-Sided Operators on a Clifford Algebra with Signed Hermitian Adjoint*; the module consequences are *Pin Representations and Clifford Modules with Signed Hermitian Adjoint*; the ideal-theoretic consequences are *Spinors as Minimal Left Ideals with Signed Hermitian Adjoint*. Nothing owned by those entries is re-derived.

**Conventions.** $A$ is a commutative ring with involution $\sigma$, $V$ is free of finite rank with a non-degenerate $q$, $x^{\dagger}=\sigma(\alpha(x^{r}))$, $\varepsilon_x=(-1)^{|x|}$, $U=\{x:x^{\dagger}x=1\}$. The forms are on the regular module: $(x,y)=\mathrm{Sc}(x^{\dagger}y)$ for the dagger, and the adjoint of an operator is written ${}^{*}$.

## The Signed Left Multiplication

**Definition.** For $x\in\mathrm{Cl}(V,q)$ the **signed left multiplication** by $x$ is the $A$-linear map

$$
\Lambda^{\alpha}_x:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad \Lambda^{\alpha}_x(y)=\alpha(x)\,y .
$$

It is the left one-sided operator $\Lambda^{\theta}_x$ of the general theory with $\theta=\alpha$, and it is defined for every $x$, invertibility not being required.

**Proposition (the sign, and the conjugate form).** Let $x$ be homogeneous of degree $k$ and $\varepsilon_x=(-1)^{k}$, so that $\alpha(x)=\varepsilon_x x$. Then

$$
\Lambda^{\alpha}_x=\varepsilon_x\,L_x=\alpha\circ L_x\circ\alpha ,
$$

so $\Lambda^{\alpha}_x=L_x$ for even $x$ and $\Lambda^{\alpha}_x=-L_x$ for odd $x$; the operator is $A$-linear in the parameter, $\Lambda^{\alpha}_{ax}=a\,\Lambda^{\alpha}_x$.

*Proof.* The first equality is $\alpha(x)=\varepsilon_x x$ with $\varepsilon_x$ central. For the conjugation form, $\alpha(L_x(\alpha(y)))=\alpha(x\,\alpha(y))=\alpha(x)y$. The parameter rule is $\alpha(ax)=a\,\alpha(x)$ with $a$ central.

**Proposition (value at the unit, parity, composition).** One has $\Lambda^{\alpha}_x(1)=\alpha(x)$, equal to $+x$ on the even part and $-x$ on the odd part; the operator preserves the parity grading when $x$ is even and interchanges the two components when $x$ is odd; and

$$
\Lambda^{\alpha}_{xz}=\Lambda^{\alpha}_x\circ\Lambda^{\alpha}_z .
$$

*Proof.* The value at the unit and the composition law are the general left-family statements with $\theta=\alpha$; the parity statement is $\Lambda^{\alpha}_x(\mathrm{Cl}^i)\subseteq\mathrm{Cl}^{i+|x|}$, since $\alpha$ preserves the degree mod two.

**Proposition (the adjoint).** For the form $(x,y)=\mathrm{Sc}(x^{\dagger}y)$ of the regular module,

$$
\bigl(\Lambda^{\alpha}_x\bigr)^{*}=\Lambda^{\alpha}_{x^{\dagger}} .
$$

So the signed left multiplication is self-adjoint exactly when $\alpha(x^{\dagger})=\alpha(x)$, that is, for $x$ with $x^{\dagger}=\alpha(x)$, and unitary when $x\in U$.

*Proof.* The identity $(\Lambda^{\theta}_x)^{*}=\Lambda^{\theta}_{x^{\dagger}}$ is the adjoint theorem of the general one-sided theory with $\theta=\alpha$.

**Remark (the sign is invisible to the left factor alone).** $\Lambda^{\alpha}_x=\varepsilon_xL_x$ and $\varepsilon_x$ is a central unit, so every intrinsic property of the operator as a one-sided operator — its kernel, its image, its rank, its self-adjointness up to sign — is shared with the plain left multiplication $L_x$. The sign becomes visible only when the left factor is paired with the right one, that is, in the two-sided operator.

## The Dagger Right Multiplication

**Definition.** For $x\in\mathrm{Cl}(V,q)$ the **dagger right multiplication** is

$$
R_{x^{\dagger}}:\mathrm{Cl}(V,q)\longrightarrow\mathrm{Cl}(V,q),\qquad R_{x^{\dagger}}(y)=y\,x^{\dagger}.
$$

It is the right one-sided operator $\mathrm P^{c}_x$ of the general theory with $c={}^{\dagger}$, defined for every $x$ because the dagger is, and it is the Hermitian counterpart of the inverse right multiplication $R_{x^{-1}}$.

**Proposition (composition, order preserved; semilinearity).** For all $x,z$,

$$
R_{x^{\dagger}}\circ R_{z^{\dagger}}=R_{(xz)^{\dagger}},\qquad
R_{x^{\dagger}}(1)=x^{\dagger},\qquad
R_{(ax)^{\dagger}}=\sigma(a)\,R_{x^{\dagger}} \quad (a\ \text{central}).
$$

So the right family composes in the same order as the left one, because the dagger is an anti-automorphism and the reversal in $c$ is compensated by the reversal of the composition; and the family is $\sigma$-semilinear in its parameter.

*Proof.* $R_{x^{\dagger}}(R_{z^{\dagger}}(y))=y\,z^{\dagger}x^{\dagger}=y\,(xz)^{\dagger}$, using $(xz)^{\dagger}=z^{\dagger}x^{\dagger}$; the value at $1$ is the definition; and the parameter rule is $(ax)^{\dagger}=\sigma(a)x^{\dagger}$ with $a$ central.

**Proposition (the two pairings).** The left and right factors commute, and

$$
L_x\circ R_{x^{\dagger}}=\Theta_x,\qquad \Lambda^{\alpha}_x\circ R_{x^{\dagger}}=\Theta^{\alpha}_x ,
$$

the signed and unsigned Hermitian sandwiches. On the unitary slice both pairings reduce to the conjugations, $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$ and $\Theta_x=\mathrm{Ad}_x$.

*Proof.* $\Lambda^{\alpha}_x(R_{x^{\dagger}}(y))=\alpha(x)\,y\,x^{\dagger}$; the commutation of a left and a right multiplication is associativity; the slice statement is the slice reduction of the two-sided article.

**Proposition (the adjoint of the right factor).** For the form $(x,y)=\mathrm{Sc}(x^{\dagger}y)$,

$$
\bigl(R_{x^{\dagger}}\bigr)^{*}=R_{(x^{\dagger})^{\dagger}}=R_x .
$$

*Proof.* The identity $(\mathrm P^{c}_x)^{*}=\mathrm P^{c}_{x^{\dagger}}$ of the general one-sided theory with $c={}^{\dagger}$ gives the first equality; $(x^{\dagger})^{\dagger}=x$ gives the second.

**Corollary (the minus is in the left factor, again).** The two pairings differ by the parity sign,

$$
\Theta^{\alpha}_x=\varepsilon_x\,\Theta_x,\qquad \Lambda^{\alpha}_x=\varepsilon_x\,L_x,
$$

with the same $\varepsilon_x$. The right factor is common to the signed and the unsigned pairing, so the entire sign bookkeeping of the two-sided operator is carried by the left one-sided operator, exactly as in the inverse formulation.

**Corollary (the reflection).** For a vector $u$ with $q(u)\neq0$ the pairing gives

$$
\Lambda^{\alpha}_u\bigl(R_{u^{\dagger}}(v)\bigr)=\Theta^{\alpha}_u(v)=-q(u)\,\rho_u(v),
\qquad
L_u\bigl(R_{u^{\dagger}}(v)\bigr)=\Theta_u(v)=q(u)\,\rho_u(v),
$$

for $v\in V$; on the unitary slice, where $q(u)=-1$, the signed pairing gives $\rho_u$ and the unsigned pairing gives $-\rho_u$. So a reflection is produced by the pair, and the sign that selects $\rho_u$ over $-\rho_u$ is the one carried by $\Lambda^{\alpha}_u$.

*Proof.* $R_{u^{\dagger}}(v)=v\,u^{\dagger}=-v\,\sigma(u)$ and $\Lambda^{\alpha}_u$ multiplies by $\alpha(u)=-u$; the result is $u\,v\,\sigma(u)$, which is the vector formula of the two-sided article. The slice statement is the corollary of the reflection proposition there.

**Remark (why no one-sided operator acts on the quadratic space).** The only left multiplications with $L_x(V)\subseteq V$ are the scalars, by the general one-sided theory, and the same holds on the right; so no one-sided operator, signed or not, acts on the quadratic space, and the sign has no one-sided manifestation there. The reflection appears only in the pairing, and on the module the sign appears instead in the parity of the operator, which is the next article.

## Kernels, Images and the Involution

**Proposition.** The kernel and the image of the signed left multiplication are those of the ordinary one,

$$
\ker\Lambda^{\alpha}_x=\ell(\alpha(x))=\ell(x),\qquad
\Lambda^{\alpha}_x\bigl(\mathrm{Cl}(V,q)\bigr)=x\cdot\mathrm{Cl}(V,q),
$$

the left annihilator and the right ideal generated by $x$. For the dagger right multiplication,

$$
\ker R_{x^{\dagger}}=r(x^{\dagger})=\ell(x^{\dagger}),\qquad
R_{x^{\dagger}}\bigl(\mathrm{Cl}(V,q)\bigr)=\mathrm{Cl}\cdot x^{\dagger},
$$

the right annihilator of $x^{\dagger}$, that is the left annihilator of $x^{\dagger}$ in the commutative sense of the antipode, and the left ideal generated by $x^{\dagger}$.

*Proof.* $\alpha(x)=\varepsilon_xx$ with $\varepsilon_x$ a unit, so $\alpha(x)y=0$ exactly when $xy=0$ and the image is the right ideal $x\cdot\mathrm{Cl}$; the right statements are the general ones with $c={}^{\dagger}$.

**Proposition (the involution is visible, the sign is not).** The kernel and the image of the two one-sided operators do **not** see the parity sign, because multiplication by $\alpha(x)$ and by $x$ differ by the central unit $\varepsilon_x$; they **do** see the coefficient involution, because the right factor is $x^{\dagger}=\sigma(\alpha(x^{r}))$ and not $x$: the image of $R_{x^{\dagger}}$ is the left ideal generated by $\sigma(\alpha(x^{r}))$, which for a nontrivial $\sigma$ is a different ideal from the one generated by $x$.

*Proof.* The first statement is the previous proof; the second is the computation of the ideal generated by $x^{\dagger}$, and $\sigma(\alpha(x^{r}))\neq x$ in general.

**Remark.** The asymmetry between the two factors is the Hermitian specificity of the one-sided theory. In the inverse formulation the right factor is $x^{-1}$, an anti-automorphism of the same element $x$; here it is the dagger, which applies the grade involution, the reversion and the coefficient involution to $x$ before multiplying. The left factor carries the sign and the right factor carries the involution, and only their product is the two-sided operator of the geometric layer.

## Worked Cases

### An Odd Element

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$ and $\sigma=\mathrm{id}$, let $x=e_1$. Then $\alpha(e_1)=-e_1$, $e_1^{\dagger}=-e_1$, and

$$
\Lambda^{\alpha}_{e_1}(y)=-e_1y,\qquad R_{e_1^{\dagger}}(y)=-y\,e_1=-e_1y,
$$

so on this oddly supported element both factors are the same operator $-L_{e_1}=L_{-e_1}$, and their pairing is $\Theta^{\alpha}_{e_1}(y)=(-e_1)y(-e_1)=e_1ye_1$. On a vector $v$ this is $\rho_{e_1}(v)$: the one-sided factors are each a plain left multiplication by $-e_1$, and only the pair produces the reflection.

### An Even Element

Let $R=e_1e_2$, even, with $R^{\dagger}=R^{-1}=e_2e_1$. Then $\Lambda^{\alpha}_R=L_R$ and $R_{R^{\dagger}}=R_{R^{-1}}$, so the factorisation is that of the inverse formulation and $\Theta^{\alpha}_R=\Theta_R=\mathrm{Ad}_R$, the half-turn. The signed and unsigned left factors agree on the even part, and the right factors differ by the defect $R\,R^{\dagger}=1$ on the slice.

### The Semilinearity in the Parameter

Over $\mathbb{C}$ in the algebra with $e^{2}=-1$, let $x=2+ie$ and $a=i$. Then $\Lambda^{\alpha}_{ax}=i\,\Lambda^{\alpha}_x$ because the left family is linear in the parameter, while

$$
R_{(ax)^{\dagger}}=\sigma(a)\,R_{x^{\dagger}}=-i\,R_{x^{\dagger}},
$$

so the two-sided parameter rule is $\Theta^{\alpha}_{ax}=a\sigma(a)\Theta^{\alpha}_x=i(-i)\Theta^{\alpha}_x=\Theta^{\alpha}_x$: the phase of the parameter cancels in the two-sided operator exactly because the left factor is linear and the right factor is antilinear. This is the one-sided form of the semilinearity correction of *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint*.

## Summary

The signed Hermitian sandwich factors into a **signed left multiplication** and a **dagger right multiplication**,

$$
\Theta^{\alpha}_x=\Lambda^{\alpha}_x\circ R_{x^{\dagger}},\qquad
\Lambda^{\alpha}_x(y)=\alpha(x)\,y,\quad R_{x^{\dagger}}(y)=y\,x^{\dagger}.
$$

The left factor carries the parity sign, $\Lambda^{\alpha}_x=\varepsilon_xL_x=\alpha\circ L_x\circ\alpha$, it is defined on the whole algebra, it is $A$-linear in its parameter, and it composes in the order $\Lambda^{\alpha}_{xz}=\Lambda^{\alpha}_x\Lambda^{\alpha}_z$. The right factor carries the involution of the base and the dagger, $R_{(ax)^{\dagger}}=\sigma(a)R_{x^{\dagger}}$, it is also defined on the whole algebra, it composes in the same order, $R_{x^{\dagger}}R_{z^{\dagger}}=R_{(xz)^{\dagger}}$, and it is $\sigma$-semilinear in its parameter. The two factors commute and their product is the two-sided operator, whose parameter rule $a\sigma(a)$ is the product of the two one-sided rules: **the semilinearity is in the right factor and the sign is in the left one**. For the form $\mathrm{Sc}(x^{\dagger}y)$ the adjoint of each factor is the factor of the dagger, $(\Lambda^{\alpha}_x)^{*}=\Lambda^{\alpha}_{x^{\dagger}}$ and $(R_{x^{\dagger}})^{*}=R_x$; on the unitary slice the dagger is the inverse and both pairings collapse to the conjugations. The kernels and images of the factors do not see the sign, since $\alpha(x)$ and $x$ differ by the central unit $\varepsilon_x$, but they do see the coefficient involution, because the right factor is built from $x^{\dagger}$ and not from $x$. As in the inverse formulation, no one-sided operator acts on the quadratic space; the reflection appears only in the pairing, and there the signed pair gives $\rho_u$ where the unsigned pair gives $-\rho_u$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\alpha}_x(y)=\alpha(x)y$ | Signed left multiplication |
| $\Lambda^{\alpha}_x=\varepsilon_xL_x=\alpha\circ L_x\circ\alpha$ | The sign, and conjugation by $\alpha$ |
| $R_{x^{\dagger}}(y)=y\,x^{\dagger}$ | Dagger right multiplication |
| $\Lambda^{\alpha}_{xz}=\Lambda^{\alpha}_x\Lambda^{\alpha}_z$, $R_{x^{\dagger}}R_{z^{\dagger}}=R_{(xz)^{\dagger}}$ | Composition laws, same order |
| $\Lambda^{\alpha}_{ax}=a\Lambda^{\alpha}_x$, $R_{(ax)^{\dagger}}=\sigma(a)R_{x^{\dagger}}$ | Linear left, semilinear right |
| $\Theta^{\alpha}_x=\Lambda^{\alpha}_x R_{x^{\dagger}}$ | The pairing, the two-sided operator |
| $(\Lambda^{\alpha}_x)^{*}=\Lambda^{\alpha}_{x^{\dagger}}$, $(R_{x^{\dagger}})^{*}=R_x$ | Adjoints for $\mathrm{Sc}(x^{\dagger}y)$ |
| $\Theta^{\alpha}_u(v)=-q(u)\rho_u(v)$ | The reflection read in the pairing |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, semilinear maps and the adjoint with respect to a Hermitian form.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the one-sided multiplications and their adjoints.
- Nathan Jacobson, *Structure of Rings*, Colloquium Publications 37 (American Mathematical Society, 1956), for the adjoint and the unitary group of an algebra with involution.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action and the self-adjointness with respect to a Hermitian form.
