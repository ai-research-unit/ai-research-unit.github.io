# __The Operators of the Quaternionic Product: the Opposite Monoid and the Norm__

## Introduction

This article is the operator article of the general quaternionic algebra, the algebra of *The Interval as the Square
and the Charge of the Material Composition*. Its product is the general quaternionic bilinear product

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q ,
$$

the second of the four general products of the biquaternion complex space (*The Four General Products of the
Biquaternion $\mathbb{C}$ Space*; *Introduction to the General Quaternionic Algebra of Biquaternions*), built with the
**natural** conjugation in the first slot and not with the Hermitian one. The operators of the band are the maps that
attach an element to an argument:

$$
L_{\tilde P}(\tilde X)=\tilde P\star\tilde X,\qquad
R_{\tilde P}(\tilde X)=\tilde X\star\tilde P,\qquad
\varrho_{\tilde P}(\tilde X)=\tilde X\tilde P^{\natural} .
$$

The first is the **left multiplication** of the product and the second is its **right multiplication**; the third is
the **twisted right multiplication**, the closed mirror of the left family. The two-sided operators of the band are the
products $L_{\tilde P}\varrho_{\tilde Q}$. The composition laws of the two families, and the interpretation of a multiplication
as a process, belong to *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and to *The
Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*. This article states the one
thing the composition laws do not: **which form the operators are adjoint for, and what that adjoint does**.

The answer is one sentence. The form of the band is the general quaternionic bilinear form

$$
N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),
$$

of Gram matrix $I_4$, the polar form of the biquaternion norm, and the adjoint for it — written ${}^{N}$ and called the
**quaternionic adjoint** — **keeps the side** and carries the **parameter** through the natural conjugation:

$$
\bigl(L_{\tilde P}\bigr)^{N}=L_{\tilde P^{\natural}},\qquad
\bigl(\varrho_{\tilde P}\bigr)^{N}=\varrho_{\tilde P^{\natural}} .
$$

Every type criterion of the band is therefore a criterion on **one** parameter. This is the sharp contrast with the
general plain algebra, whose form is the scalar part of its own product, whose adjoint is the transpose, and whose
transpose **swaps the two sides**, so that its one-sided criterion is a criterion on one parameter while its two-sided
criteria are criteria on the **product** of two (*The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the
Sandwich*). The
consequences multiply. The self-adjoint and the skew-adjoint one-sided operators are cut out by the sign character of
the natural conjugation, so both sectors are populated — the centre and the vector subspace — where the plain row has a
trivial skew sector. The norm enters every criterion: a multiplication scales the form by the norm of its parameter, the
determinant of a multiplication is the square of that norm, and the form-preserving one-sided operators are the norm-one
slice, a rich group. The two-sided operator of the band selected by the conjugation is **quadratic** in its parameter and
is multiplicative up to the norm for **every** parameter, whereas the plain two-sided operator obeys only a partial law
and then only when the product of its two parameters is central. The criteria and their proofs are the mathematics of
*One-Sided Operators on the General Quaternionic Algebra of Biquaternions* and *Two-Sided Operators on the General
Quaternionic Algebra of Biquaternions*; the composition law is the mathematics of *The Left Multiplications of the
Quaternionic Product and the Opposite Monoid*; the article reads them.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$,
$e_k^{2}=-e_0$ and central imaginary $i$; a general element is $\tilde Q=Q_0e_0+\vec Q$ with the vector part
$\vec Q=Q_1e_1+Q_2e_2+Q_3e_3$. Juxtaposition is the **plain**, associative product. The conjugations are the
coefficientwise $\bar{\cdot}$, the natural ${\natural}$ fixing $i$ and negating $e_1,e_2,e_3$, and the Hermitian
${}^{*}=\bar{\cdot}\circ{\natural}$; the sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$. The product
of the band is written $\star$, and it is read through the natural conjugation alone. The form is the one displayed
above, of Gram matrix $I_4$; it is cited, never re-proved, and on the material sector $\mathbb{M}_-$ it is the interval
$-c^{2}t^{2}+\vec x^{2}$, of signature $(3,1)$ (*The Interval as the Square and the Charge of the Material Composition*). Its algebraic norm is the
**biquaternion norm**

$$
N(\tilde Q)=N(\tilde Q,\tilde Q)=\tilde Q\tilde Q^{\natural}=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2},
$$

central, multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and an element is a unit of the plain algebra
exactly when $N(\tilde Q)\neq0$. The adjoint for the form is written ${}^{N}$, so that
$\langle T\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,T^{N}\tilde Q\rangle_{\natural}$ by definition; the
Hermitian adjoint is written ${}^{*}$ and belongs to the probability band.

## The Two Multiplications and Their Composition

The product attaches three operators to an element, and the two families of the band are its left and its twisted right
multiplications.

**Definition (the multiplications of the product).** For $\tilde P\in\mathbb{B}$, the **left multiplication** and the
**right multiplication** of $\star$ are the $\mathbb{C}$-linear maps on $\mathbb{B}$

$$
L_{\tilde P}(\tilde X)=\tilde P\star\tilde X=\tilde P^{\natural}\tilde X ,\qquad
R_{\tilde P}(\tilde X)=\tilde X\star\tilde P=\tilde X^{\natural}\tilde P ,
$$

and the **twisted right multiplication** is the $\mathbb{C}$-linear map $\varrho_{\tilde P}(\tilde X)=\tilde X\tilde P^{\natural}$.
The left multiplication is the plain left multiplication by the **conjugated** element, $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$,
and the twisted right multiplication is the plain right multiplication by it, $\varrho_{\tilde P}=R^{\mathrm{plain}}_{\tilde P^{\natural}}$.

**Theorem (the composition law).** For all $\tilde P,\tilde R$,

$$
L_{\tilde P}\circ L_{\tilde R}=L_{\tilde R\tilde P},\qquad
\varrho_{\tilde P}\circ\varrho_{\tilde R}=\varrho_{\tilde P\tilde R},
$$

the product on the right being the **plain** product of the algebra; the two laws are opposite, the left family
reversing the order and the twisted right family preserving it.

*Proof.* The laws are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, §*The Left
Multiplications* and §*The Right Multiplications*. In one line each,
$L_{\tilde P}L_{\tilde R}(\tilde X)=\tilde P^{\natural}(\tilde R^{\natural}\tilde X)=(\tilde P^{\natural}\tilde R^{\natural})\tilde X=(\tilde R\tilde P)^{\natural}\tilde X$,
the last step being the anti-automorphism property of ${\natural}$, $\tilde P^{\natural}\tilde R^{\natural}=(\tilde R\tilde P)^{\natural}$;
and $\varrho_{\tilde P}\varrho_{\tilde R}(\tilde X)=\tilde X\tilde R^{\natural}\tilde P^{\natural}=\tilde X(\tilde P\tilde R)^{\natural}$.
The order reversal is exactly the anti-automorphism: it is not the associativity of $\star$, which fails, but the
associativity of the plain product read through ${\natural}$.

**Corollary (the two monoids).** The set $M_L=\{L_{\tilde P}\}$ is a monoid with identity $L_{e_0}=\mathrm{id}$, and the
assignment $\tilde P\mapsto L_{\tilde P}$ is an **injective anti-isomorphism of monoids** from the multiplicative monoid
of the plain algebra onto $M_L$,

$$
M_L\cong\mathbb{B}^{\mathrm{op}},
$$

the opposite monoid. The set $M_R=\{\varrho_{\tilde P}\}$ is a monoid with identity $\varrho_{e_0}=\mathrm{id}$ and
$\tilde P\mapsto\varrho_{\tilde P}$ is an **isomorphism** $M_R\cong\mathbb{B}$. Where the anti-isomorphism lies is in the
natural conjugation: it is the anti-automorphism, and only it, that reverses the order of a composite.

*Proof.* Closure and the identities are read off the laws: $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ is again a
left multiplication, and $L_{e_0}(\tilde X)=e_0^{\natural}\tilde X=\tilde X$. Injectivity is read at $e_0$,
$L_{\tilde P}(e_0)=\tilde P^{\natural}$, which recovers $\tilde P$. The group of units of $M_L$ is the unit group of the
plain algebra with the reversed law, and an operator $L_{\tilde P}$ is invertible exactly when $N(\tilde P)\neq0$.

**Proposition (the product has no two-sided unit).** The element $e_0$ is a **left** unit of $\star$,
$e_0\star\tilde Q=\tilde Q$, and there is **no right** unit: the right action of the identity is the natural
conjugation, $\tilde Q\star e_0=\tilde Q^{\natural}$, which differs from $\tilde Q$ for every non-central $\tilde Q$. The
product therefore has no two-sided unit and is unital on one side alone, and the right multiplication $R_{\tilde P}$ of
the product does not close under composition: $R_{\tilde P}R_{\tilde Q}(\tilde X)=\tilde Q^{\natural}\tilde X\tilde P$.
The monoids $M_L$ and $M_R$ nevertheless contain the two-sided identity $\mathrm{id}$.

*Proof.* The unit statements are the two evaluations $e_0^{\natural}=e_0$ and $\tilde Q^{\natural}e_0=\tilde Q^{\natural}$;
a right unit $u$ would satisfy $\tilde X^{\natural}u=\tilde X$ for all $\tilde X$, and at $\tilde X=e_0$ this forces
$u=e_0$, which then fails at a pure $\tilde X$. The non-closure is *The Left Multiplications of the Quaternionic Product
and the Opposite Monoid*, §*The Right Multiplications*, with the witness $R_{e_1}R_{e_1}(e_0)=e_0$ and
$R_{e_1}R_{e_1}(e_1)=e_1$, whereas a right multiplication of the product with value $e_0$ at $e_0$ is $R_{e_0}$, which
sends $e_1$ to $-e_1$.

**Read as a physical statement.** The orientation of the composition is the operator form of the orientation of the
material composition: the first slot is read through the natural conjugation and the second as it stands, so an element
attached on the left and the same element attached on the right are different operations, and only the left attachment
composes on the nose. The composition of two left multiplications is a left multiplication — the operations of the band
form a monoid and compose associatively — although the product of two elements does not associate. The interpretation is the
corpus's: **the process is the map and the state is the idempotent** (*The Monoid of Acting Maps*), and here the process
is the opposite monoid, the element being only a representative read through the conjugation.

**Theorem (the mixed composites span the endomorphism algebra).** For all $\tilde P,\tilde Q$ the mixed composites
commute and close,

$$
L_{\tilde P}\circ\varrho_{\tilde Q}=\varrho_{\tilde Q}\circ L_{\tilde P},\qquad
L_{\tilde P}\circ\varrho_{\tilde Q}(\tilde X)=\tilde P^{\natural}\tilde X\tilde Q^{\natural},
$$

and their complex span is the whole endomorphism algebra
$\operatorname{span}_{\mathbb{C}}\{L_{\tilde P}\varrho_{\tilde Q}\}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of
complex dimension sixteen.

*Proof.* Commutation and closure are the plain associativity read in the two-sided regular representation, and the span
is *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, §*The Mixed Compositions*: the
sixteen operators $L_{e_m}\varrho_{e_n}$ are the products of the two bases $\{L_{e_m}\}$ and $\{\varrho_{e_n}\}$ of the
left and the right regular representation and are linearly independent, so they already span all of
$\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The two-sided family itself is the image of the decomposable tensors of
$\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$, the linearisation of the pair $(\tilde P,\tilde Q)$; a sum of
two-sided operators is two-sided only when the corresponding tensor is decomposable, and a general endomorphism of the
frame is such a sum and not a single two-sided product.

**Read as a physical statement.** The two-sided operations of the band are closed under composition and generate every
linear operation of the frame: the failure of associativity of the product is invisible at the level of the operators,
which generate the full endomorphism algebra. What the product loses by its twisting of the first slot it recovers in
its operator algebra, and the two-sided operator is again the carrier of the general linear action on the frame, as it
is for the plain product. The interpretation is a naming of a proved algebraic fact and is labelled so.

## The Adjoint of the Quaternionic Form Keeps the Sides

**Theorem (the adjoints for the quaternionic form).** For all $\tilde P,\tilde X,\tilde Y\in\mathbb{B}$,

$$
\bigl\langle L_{\tilde P}\tilde X,\tilde Y\bigr\rangle_{\natural}=\bigl\langle\tilde X,L_{\tilde P^{\natural}}\tilde Y\bigr\rangle_{\natural},
\qquad\text{that is}\qquad
\bigl(L_{\tilde P}\bigr)^{N}=L_{\tilde P^{\natural}},
$$

and the same for the twisted right multiplication, $(\varrho_{\tilde P})^{N}=\varrho_{\tilde P^{\natural}}$.

*Proof.* The adjoints are *One-Sided Operators on the General Quaternionic Algebra of Biquaternions*, §*The Adjoints
for the Bilinear Form*. In one line,
$\langle L_{\tilde P}\tilde X,\tilde Y\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde X\tilde Y^{\natural})$,
and by the cyclicity of the scalar part this equals
$\mathrm{Sc}(\tilde X\tilde Y^{\natural}\tilde P^{\natural})=\mathrm{Sc}(\tilde X(\tilde P\tilde Y)^{\natural})=\langle\tilde X,L_{\tilde P^{\natural}}\tilde Y\rangle_{\natural}$,
using $\tilde P^{\natural}\tilde Y^{\natural}=(\tilde P\tilde Y)^{\natural}$. The right case is the same computation with
the factors in the other order.

**Corollary (the adjoint keeps the side and conjugates the parameter).** The adjoint of a left multiplication is a left
multiplication, the adjoint of a twisted right multiplication is a twisted right multiplication, and in both cases the
parameter is carried through the natural conjugation. The adjoint therefore maps each family onto itself and preserves
the side, and it acts on the parameter by ${\natural}$ and on nothing else.

*Proof.* Immediate from the theorem, and the involution ${}^{\natural}$ of order two makes the adjoint an involution on
each family, $((L_{\tilde P})^{N})^{N}=L_{\tilde P}$.

**Read as a physical statement.** The pairing of the band is the interval, and transporting an operation across it
leaves the side alone: an operation attached before an argument is still attached before it afterwards, and only the
parameter is conjugated. This is the operator content of the statement that the interval is the invariant form of a
single attachment, so the form remembers the side on which an operation stands and forgets nothing of it. The contrast
with the composition band is total: there the form is the scalar part of the product and cannot tell a left attachment
from a right one, and its adjoint is the swap. That the swap belongs to the plain form alone is the reason the plain
one-sided criterion is a criterion on the centrality of its single parameter and its skew sector is trivial, while its
**two-sided** criteria are criteria on the **product** of its two parameters — proportional, central, vanishing — and
every type criterion of this band is a criterion on one parameter; the
comparison of the four adjoints is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint
and Bracket*, which is not one of the twelve.

## The Types of the Operators

**Definition (the types).** For a form $\varphi$ on $\mathbb{B}$, an operator $T$ is **$\varphi$-self-adjoint** when
$T^{\varphi}=T$, **$\varphi$-skew-adjoint** when $T^{\varphi}=-T$, and **$\varphi$-preserving** when
$\varphi(T\tilde X,T\tilde Y)=\varphi(\tilde X,\tilde Y)$ for all $\tilde X,\tilde Y$. Here $\varphi$ is the
quaternionic form $N$ and $T^{\varphi}$ is the quaternionic adjoint ${}^{N}$ of the previous section.

**Corollary (the one-sided types).** The left multiplication $L_{\tilde P}$ is $N$-self-adjoint exactly for a
**central** parameter, $N$-skew-adjoint exactly for a **pure** parameter, and $N$-preserving exactly for a parameter of
**norm one**, $N(\tilde P)=1$; the twisted right multiplication $\varrho_{\tilde P}$ obeys the same three criteria on the
same parameter. Each criterion is a criterion on the single parameter.

*Proof.* By the injectivity of the parameter map, $L_{\tilde P^{\natural}}=L_{\tilde P}$ is $\tilde P^{\natural}=\tilde P$,
that is $\tilde P$ central, and $L_{\tilde P^{\natural}}=-L_{\tilde P}=L_{-\tilde P}$ is $\tilde P^{\natural}=-\tilde P$,
that is $\tilde P$ pure; the preservation criterion is the scaling of the form below, $N(L_{\tilde P}\tilde X)=N(\tilde P)N(\tilde X)$,
which is the identity for all $\tilde X$ exactly when $N(\tilde P)=1$. The two statements are *One-Sided Operators on the
General Quaternionic Algebra of Biquaternions*, §*The Adjoints for the Bilinear Form*, §*The Norm and the Determinant of
a Multiplication*.

**Corollary (the two-sided types).** The twisted two-sided operator $\Theta_{\tilde A}=L_{\tilde A^{\natural}}\varrho_{\tilde A}$,
the map $\Theta_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A^{\natural}$, has adjoint
$(\Theta_{\tilde A})^{N}=\Theta_{\tilde A^{\natural}}$; it is $N$-self-adjoint exactly when
$\tilde A^{\natural}=\pm\tilde A$, that is exactly when the parameter lies in the **centre or the vector subspace**,
$\mathbb{C}_{\mathbb{B}}\cup\mathrm{Vect}(\mathbb{B})$, and **no** nonzero $\Theta_{\tilde A}$ is $N$-skew-adjoint.

*Proof.* The adjoint is *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, §*The Adjoint*: the
adjoint of a product is the product of the adjoints in reverse order and the factors commute, giving
$(\Theta_{\tilde A})^{N}=(\varrho_{\tilde A})^{N}(L_{\tilde A^{\natural}})^{N}=\varrho_{\tilde A^{\natural}}L_{\tilde A}=\Theta_{\tilde A^{\natural}}$.
Self-adjointness is $\Theta_{\tilde A^{\natural}}=\Theta_{\tilde A}$, and injectivity up to sign gives
$\tilde A^{\natural}=\pm\tilde A$, the two eigenspaces of the natural conjugation; the skew sector collapses by the
computation of the same proposition. The parameter map is injective up to the sign of its argument, so the criterion is
a criterion on one parameter and not on a pair.

**Read as a physical statement.** The two populated sectors are the two ways a single parameter can be symmetric for the
interval: a central parameter gives a self-adjoint multiplication, a pure parameter gives a skew-adjoint one, and a
mixed parameter gives neither. The skew family is the vector subspace, of real dimension six, and it is the operator
form of the statement that the material directions and the time direction are read by the interval with opposite signs;
unlike the composition band, where the skew sector is trivial and no generator appears, this band carries a family of
complex dimension three of skew-adjoint multiplications. That family does not close under composition, the product of
two pure parameters being mixed in general, so the generators of the band are read through the bracket of the
antisymmetric band and not through the multiplication. All of this is an interpretation of a proved algebraic criterion and is
labelled so.

| parameter $\tilde P$ | subalgebra | $L_{\tilde P}$ is $N$-self-adjoint | $N$-skew-adjoint | $N$-preserving |
|---|---|---|---|---|
| central, $\tilde P=\lambda e_0$ | $\mathbb{C}_{\mathbb{B}}$ | yes | only $\tilde P=0$ | $N(\tilde P)=1$ |
| pure, $\tilde P=\vec P$ | $\mathrm{Vect}(\mathbb{B})$ | only $\tilde P=0$ | yes | $N(\tilde P)=1$ |
| mixed, $\tilde P=a_0e_0+\vec P$ | — | no | no | $N(\tilde P)=1$ |

The table collects the one-sided criterion; the two-sided criterion of the second corollary is one row deeper and is
read as: self-adjoint for a parameter in the centre or the vector subspace, skew-adjoint never, and preserving exactly
for $N(\tilde A)=\pm1$.

## The Symmetries of the Form and of the Product

**Proposition (the conformal factor and the determinant).** For all $\tilde P,\tilde X$,

$$
N\bigl(L_{\tilde P}\tilde X\bigr)=N(\tilde P)\,N(\tilde X),\qquad
\det L_{\tilde P}=N(\tilde P)^{2},
$$

and the same two identities hold for $\varrho_{\tilde P}$.

*Proof.* The first is the multiplicativity of the norm, $N(\tilde P^{\natural}\tilde X)=N(\tilde P^{\natural})N(\tilde X)=N(\tilde P)N(\tilde X)$
with $N(\tilde P^{\natural})=N(\tilde P)$; the determinant is *One-Sided Operators on the General Quaternionic Algebra
of Biquaternions*, §*The Norm and the Determinant of a Multiplication*, where the multiplication is the Kronecker
product of the matrix $\mathsf{M}_2(\tilde P)$ with $I_2$ and the determinant is $\det\mathsf{M}_2(\tilde P)^{2}=N(\tilde P)^{2}$.

**Corollary (the form-preserving operators).** The one-sided operators preserving the quaternionic form are exactly the
left and the twisted right multiplications by a parameter of **norm one**, and their group is the norm-one slice, of
complex dimension three; a multiplication by a parameter of norm $-1$ reverses the sign of the form. A twisted
two-sided operator $\Theta_{\tilde A}$ preserves the form exactly when $N(\tilde A)=\pm1$, the norm-one part being the
inner automorphisms and the whole set the pin group.

*Proof.* The condition is $N(\tilde P)=1$ from the conformal factor, and $N(\Theta_{\tilde A}\tilde X)=N(\tilde A)^{2}N(\tilde X)$
for the two-sided case, *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, §*Automorphisms*.
The norm-one slice is closed under the plain product by multiplicativity of the norm, and it is the slice whose
elements the corpus reads as the Lorentz transformations on $\mathbb{M}_-$; the group of two-sided form-preserving
operators is the biquaternion pin group (*The Pin and Spin Groups of the General Quaternionic Algebra of
Biquaternions*).

**Theorem (the quadratic two-sided operator and its multiplication law).** The twisted two-sided operator
$\Theta_{\tilde A}=\tilde A\,[\,]\,\tilde A^{\natural}$ is **quadratic** in its parameter,
$\Theta_{\lambda\tilde A}=\lambda^{2}\Theta_{\tilde A}$ and $\Theta_{-\tilde A}=\Theta_{\tilde A}$, and it satisfies

$$
\Theta_{\tilde A}\circ\Theta_{\tilde B}=\Theta_{\tilde A\tilde B},\qquad
\Theta_{\tilde A}(\tilde Y)\,\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\,\Theta_{\tilde A}(\tilde Y\tilde Z)
\qquad\text{for every }\tilde A .
$$

*Proof.* The composition and the multiplication law are *Two-Sided Operators on the General Quaternionic Algebra of
Biquaternions*, §*The Multiplication Law*: the multiplication law is the one line
$\tilde A\tilde Y\tilde A^{\natural}\tilde A\tilde Z\tilde A^{\natural}=\tilde A\tilde YN(\tilde A)\tilde Z\tilde A^{\natural}$,
which uses $\tilde A^{\natural}\tilde A=N(\tilde A)e_0$, and the norm is central and may be moved out. This holds for
**every** parameter, since $\tilde A^{\natural}\tilde A=N(\tilde A)$ is central always and no centrality of a product of
two parameters is required.

**Corollary (the multiplicative operators).** The two-sided operators of the band that are **strictly** multiplicative,
$T(\tilde Y)T(\tilde Z)=T(\tilde Y\tilde Z)$, are exactly those with the two slots inverse,
$L_{\tilde P}\varrho_{\tilde Q}$ with $\tilde P\tilde Q=e_0$, and these are the inner automorphisms
$\mathrm{Ad}_{\tilde P^{\natural}}$; the family multiplicative **up to a scalar** is exactly the family whose slot
product is central, the scalar being $(\tilde P\tilde Q)^{\natural}$; and the twisted two-sided operators are, up to
scalars, exactly the multiplicative-up-to-a-scalar family.

*Proof.* The plain criterion is *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, §*When a
Product $L_aR_b$ Is Two-Sided*: the product is multiplicative up to the inserted scalar $\tilde B\tilde A$, so here up to
$(\tilde P\tilde Q)^{\natural}$, central exactly when $\tilde P\tilde Q$ is, and equal to $e_0$ exactly when
$\tilde P\tilde Q=e_0$. With $\tilde Q=\tilde P^{-1}$ the operator is exactly the inner automorphism
$\mathrm{Ad}_{\tilde P^{\natural}}$, which is the scalar multiple $N(\tilde P)^{-1}\Theta_{\tilde P^{\natural}}$ of the
twisted two-sided operator.

**Read as a physical statement.** The interval scales by the norm of a multiplying parameter, so the multiplication of
the band is a **conformal** map of the interval with conformal factor the norm, and the form-preserving ones are exactly
the norm-one parameters, the Lorentz transformations. The determinant interpretation is the same statement squared, and it
fixes the invertibility of the operator by the norm of the parameter. The multiplication law is the second interpretation: the
composition of a two-sided operator with itself is the operator again, up to the norm of the parameter as a scalar, and
this is unconditional in the band while the composition band carried it only when the product of the two parameters was
central. The **norm is the scalar of the composition**: it is what the product of the two slots leaves behind, and it is
the only obstruction to a two-sided operation being an automorphism. The interpretations are named **norm conformality** and
**unconditional multiplicativity** and are labelled as interpretations.

## The Operators Acting on the State Space

The operators of the band act on the state space of the corpus, and since $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$
their action is the plain action with the parameter conjugated. Let $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\tilde\Upsilon_2\}$
be the minimal left ideal, with $\tilde\Pi_-=e_0-\tilde\Pi_+$ the complementary idempotent and
$\mathbb{B}\tilde\Pi_-=\mathbb{C}\{\tilde\Pi_-,\tilde\Upsilon_1\}$ the complement, as in *The Spinor Space as a Module
and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning*.

**Proposition (the left actions exhaust the operators of the state space).** The map
$\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(S)$, $\tilde P\mapsto L_{\tilde P}|_{S}$, is an isomorphism: the plain
algebra acts faithfully on its defining module $S$ of complex dimension two, and both spaces have complex dimension
four, so the four plain left multiplications by the basis elements form a $\mathbb{C}$-basis of
$\operatorname{End}_{\mathbb{C}}(S)$. The four of the band differ from that basis only by the signs of the vector
directions,

$$
L_{e_0}=\mathrm{id},\qquad L_{e_k}=-L^{\mathrm{plain}}_{e_k}\quad(k=1,2,3),
$$

the signs entering because the left multiplication reads its parameter through the conjugation; they are therefore a
basis as well, and every operator of the state space is a left multiplication of the band.

*Proof.* The module $S=\mathbb{B}\tilde\Pi_+$, its complex dimension two and the faithfulness of the left action are *The
Spinor Space as a Module and as a Hilbert Space* and *Biquaternion Objects and Their Matrix Correspondences*; the
equality $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$ together with $e_\mu^{\natural}=\varepsilon_\mu e_\mu$
and $\varepsilon=(1,-1,-1,-1)$ is the isotope identity of *The Specificities of the General Quaternionic Algebra*,
§*The Isotope Identity*.

**Proposition (the projectors, and the swap of the two ideals).** The left multiplication $L_{\tilde P}$ is a projector
exactly when $\tilde P$ is a plain idempotent; and for the two minimal idempotents, whose natural conjugates are
exchanged, $\tilde\Pi_+^{\natural}=\tilde\Pi_-$ and $\tilde\Pi_-^{\natural}=\tilde\Pi_+$,
$L_{\tilde\Pi_+}=L^{\mathrm{plain}}_{\tilde\Pi_-}$ is the plain projector onto the **complementary** ideal
$\mathbb{B}\tilde\Pi_-$, while $L_{\tilde\Pi_-}=L^{\mathrm{plain}}_{\tilde\Pi_+}$ is the plain projector onto $S$; the
two are orthogonal, $L_{\tilde\Pi_+}L_{\tilde\Pi_-}=0$. In particular the element $\tilde\Pi_+$ is a **nilpotent** of the
band's own product, $\tilde\Pi_+\star\tilde\Pi_+=N(\tilde\Pi_+)e_0=0$, while the operator it defines is a projector: the
band realises a projector on an element of vanishing square.

*Proof.* The projector criterion is *The Specificities of the General Quaternionic Algebra*, §*The Projectors*: the
faithfulness of the parameter map reduces $L_{\tilde P}^{2}=L_{\tilde P}$ to $(\tilde P^{\natural})^{2}=\tilde P^{\natural}$,
and ${\natural}$ permutes the plain idempotents, so the elements are exactly the plain idempotents. The exchange
$\tilde\Pi_+^{\natural}=\tilde\Pi_-$ is the computation $\tfrac12(e_0+ie_3)^{\natural}=\tfrac12(e_0-ie_3)=\tilde\Pi_-$, and
the nilpotence is the same specificities article, $N(\tilde\Pi_+)=0$ on a nontrivial plain idempotent. Here $ie_3$ is a root of $+1$, $(ie_3)^2=e_0$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

**Proposition (the twisted right actions are the commutant).** A twisted right multiplication commutes with every left
one, so it is a $\mathbb{B}$-linear map of $S$ into itself or into the complement; the operators commuting with every
left multiplication are exactly the twisted right multiplications, and the operators commuting with both families are the
central scalars. A central element gives the same left and twisted right action, the scalar multiplication by its scalar
part.

*Proof.* The commutation is the mixed law of the first section, and the double-centraliser statement is *One-Sided
Operators on the General Quaternionic Algebra of Biquaternions*, §*The Two Multiplications*. The nilpotent twisted right
multiplications carrying $S$ onto the complement are the plain ones of *The Complementary Space of the Spinor Space and
Its Physical Meaning*.

**Read as a physical statement.** The left actions of the band are the observables on the state space, and every
operator of the state space is one of them, with the parameter read through the conjugation — the state space sees the
element only through its conjugate. The projectors are the plain ones, and the two algebraic norm projectors of the state
space and of its complement are **exchanged** by the conjugation: the band's own left multiplication by the minimal
idempotent projects onto the other ideal. This is a physical sharpening of the statement that the band's product
recognises almost none of its own projectors: the element whose square vanishes defines the projector, and the element
whose left multiplication projects is the conjugate of a plain idempotent. The interpretations are named **conjugated
observables** and **exchanged ideals** and are labelled as interpretations.

## The Sandwich and the Inner Automorphism

**Proposition (one conjugation, two parametrisations).** For every **unit** $\tilde A$,

$$
\Theta_{\tilde A}=N(\tilde A)\,\mathrm{Ad}_{\tilde A},\qquad
\mathrm{Ad}_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A^{-1},
$$

so the twisted two-sided operator is the inner automorphism scaled by the norm; the two operators agree exactly on the
**norm-one** parameters, and there and alone.

*Proof.* The factorisation is *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, §*The Sign and
the Inverse*: it is $\tilde A^{\natural}=N(\tilde A)\tilde A^{-1}$ read in the right factor, the norm being central. The
two agree exactly when the scalar is one, that is $N(\tilde A)=1$.

**Corollary (the two operators and the form).** The twisted two-sided operator scales the quaternionic form by the
factor $N(\tilde A)^{2}$, $N(\Theta_{\tilde A}\tilde X,\Theta_{\tilde A}\tilde Y)=N(\tilde A)^{2}N(\tilde X,\tilde Y)$,
while the inner automorphism preserves it **exactly**,
$N(\mathrm{Ad}_{\tilde A}\tilde X,\mathrm{Ad}_{\tilde A}\tilde Y)=N(\tilde X,\tilde Y)$, being an isometry of the form
for every unit; on the norm-one slice the two operators coincide, and there the scaling of $\Theta$ is the identity too.
Off the slice they differ by the central scalar $N(\tilde A)$, which is the whole content of the word *twisted*: the
sandwich is the inner automorphism continued to the units of all norms by the conjugation in place of the inverse.

*Proof.* The scaling of $\Theta$ by $N(\tilde A)^{2}$ is the automorphisms proposition of the previous section; for
$\mathrm{Ad}$ it is the multiplicativity of the norm,
$N(\tilde A\tilde X\tilde A^{-1})=N(\tilde A)N(\tilde X)N(\tilde A)^{-1}=N(\tilde X)$, which by polarisation is the
preservation of the bilinear form; equality on the slice is the proposition.

**Read as a physical statement.** The band attaches a conjugation to an element in two ways, by the inverse and by the
natural conjugate, and the two coincide exactly on the norm-one slice, which is the Lorentz group. The Lorentz action on
the material sector is therefore the inner automorphism, and it is also the twisted two-sided operator, because the
Lorentz parameters are precisely those of norm one; the two differ off the slice by the norm, and the norm is the mass
parameter of the material sector. This is the operator form of the corpus's division of the parameters into the
norm-one motions and the rest, and it is an interpretation and not a derivation: the Lorentz action itself and the double cover
are *Biquaternion Rotations and Lorentz Transformations*.

## A Worked Case

Take one mixed parameter of norm two,

$$
\tilde A=e_0+e_1,\qquad N(\tilde A)=2,\qquad \tilde A^{\natural}=e_0-e_1,\qquad \tilde A^{2}=2e_1 .
$$

The left multiplication by the parameter is the plain left multiplication by its conjugate, and it reads

$$
L_{\tilde A}(e_0)=e_0-e_1,\qquad L_{\tilde A}(e_1)=e_0+e_1,\qquad L_{\tilde A}(e_2)=e_2-e_3 ,
$$

so the composition law reads on $e_1$,
$L_{\tilde A}L_{\tilde A}(e_1)=2e_0=L_{\tilde A^{2}}(e_1)=L_{2e_1}(e_1)$, the parameter on the right being the plain
square. The adjoint keeps the left side and conjugates the parameter, displayed on the basis pair $(e_0,e_1)$:

$$
\bigl\langle L_{\tilde A}e_0,e_1\bigr\rangle_{\natural}=-1=\bigl\langle e_0,L_{\tilde A^{\natural}}e_1\bigr\rangle_{\natural},
\qquad L_{\tilde A^{\natural}}=L_{e_0-e_1} .
$$

The parameter is mixed, so $L_{\tilde A}$ is neither self-adjoint nor skew-adjoint, and its norm two scales the form by
two, so it is not form-preserving. By contrast, the pure parameter $\tilde V=e_1$ has norm one and gives a
skew-adjoint and form-preserving multiplication, the two properties the two criteria promise at once.

The twisted two-sided operator of the same parameter is $\Theta_{\tilde A}=2\,\mathrm{Ad}_{\tilde A}$, and on the basis
it is

$$
\Theta_{\tilde A}(e_0)=2e_0,\qquad \Theta_{\tilde A}(e_1)=2e_1,\qquad
\Theta_{\tilde A}(e_2)=2e_3,\qquad \Theta_{\tilde A}(e_3)=-2e_2 ,
$$

a scaling by two on the plane $\mathbb{C}\{e_0,e_1\}$ and twice a quarter turn on the plane $\mathbb{C}\{e_2,e_3\}$. The
quadraticity is visible at once, $\Theta_{2\tilde A}=4\,\Theta_{\tilde A}$, and the multiplication law holds for this
parameter with $N(\tilde A)=2$ as its scalar: for $\tilde Y=(1,2,3,4)$ and $\tilde Z=e_1$ the two sides of
$\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=2\,\Theta_{\tilde A}(\tilde Y\tilde Z)$ are both $(-8,4,12,16)$.
The operator is not form-preserving, since its parameter has norm two, and it is not an automorphism, in agreement with
the criterion.

The causal division is displayed by three material four-vectors and one Lorentz parameter. With the material sector
convention $\tilde T=ict\,e_0+\vec x$ and $c=1$,

$$
N(5ie_0+3e_1)=-16,\qquad N(3ie_0+3e_1)=0,\qquad N(3ie_0+5e_1)=16,
$$

the first **timelike**, the second **null**, on the causal cone, and the third **spacelike**. A boost parameter of norm
one, $\tilde U=\cosh u\,e_0+\sinh u\,ie_1$, has $N(\tilde U)=1$, and its left multiplication is a
form-preserving operator: $N(L_{\tilde U}(5ie_0+3e_1))=N(5ie_0+3e_1)=-16$ for every $u$, the interval of the
timelike four-vector unchanged.

**A numerical check.** The two composition laws, the mixed commutation, the sixteen-dimensional span, the isotope
identity, the three adjoints, the one-sided type criteria on random, central, pure and null parameters, the two-sided
self-adjointness criterion $\tilde A^{\natural}=\pm\tilde A$, the quadraticity and the multiplication law of $\Theta$,
the identity $\Theta_{\tilde A}=N(\tilde A)\mathrm{Ad}_{\tilde A}$ with the agreement on the norm-one slice, and the
projector criterion with the exchange $\tilde\Pi_+^{\natural}=\tilde\Pi_-$ were all recomputed outside the repository to
machine precision; the numerical values of the worked case, the three causal signs and the boost preserving the interval
were checked element by element.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must
declare.

- **The composition laws and the opposite monoid are not proved here.** They are *The Left Multiplications of the
  Quaternionic Product and the Opposite Monoid*, and the reading of the multiplication as a process belongs to *The
  Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent*.
- **The isotope identity and the projectors are not re-derived here.** The dictionary $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$,
  the projector criterion and the square-zero projectors are *The Specificities of the General Quaternionic Algebra*.
- **The adjoints, the norm and the determinant are not re-proved here.** They are *One-Sided Operators on the General
  Quaternionic Algebra of Biquaternions*, whose content the article applies through its two corollaries.
- **The sandwich is not re-read here.** The quadraticity, the multiplication law up to the norm, the injectivity up to
  sign and the pin and spin groups are *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* and
  *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*.
- **The physical adjoint is not this adjoint.** Self-adjointness for the quaternionic form is not hermiticity; the
  observables and the gauge generators are the self-adjoint and the skew-adjoint operators for the Hermitian form of the
  probability band, and they are *Observables, Gauge Generators and the Chirality of the Internal Action*. The dagger
  layer of the same multiplications is *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and
  *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*.
- **The bracket and the generators are not here.** The skew-adjoint family of the band is read through the bracket of the
  antisymmetric quaternionic band, which owns the structure of the generators.
- **The four adjoints are not compared here.** The comparison, block against block, is the crossing reader *The Operators
  of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve; this article declares
  only the quaternionic column.
- **The metric, the mass shell and the invertibility are the companion articles' business.** The interval and the
  biquaternion norm, the units and the zero divisors are *The Group of Units of the General Plain Algebra and the Complement of the Zero-Divisor Cone*; the mass shell, the rank
  and the positivity of the dagger are *Mass, Rank and the Positivity of the Dagger*; the interval read as the square of
  the material composition is *The Interval as the Square and the Charge of the Material Composition*, and the
  orientation of the composition is *Why the Material Composition Is Oriented and Cannot Measure*. This article owns
  none of them.
- **The state space is used, not studied.** The module $S$ and its complement are the subject of *The Spinor Space as a
  Module and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning*; they are
  used here only to display the action of the operators.

**What the framework does not claim.** The interpretation does not derive the Lorentz transformation, the light cone or the
mass shell from the operator calculus; it reads the three causal classes of the parameters that the corpus already uses.
It does not identify a physical symmetry with the inner automorphisms; it states that the symmetries of the interval
inside this family are the norm-one multiplications and their two-sided companions. And it does not claim that the
operator calculus of the twelve rows is one calculus: the swap of the sides belongs to the plain form alone.

## The Ledger

**Proved.** The left multiplications of the quaternionic product are $L_{\tilde P}(\tilde X)=\tilde P^{\natural}\tilde X$,
the plain left multiplications by the conjugated parameter, and they compose by the **reversed** law
$L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$, so that $M_L\cong\mathbb{B}^{\mathrm{op}}$ is a monoid
anti-isomorphic to the plain multiplicative monoid, the anti-isomorphism lying in the natural conjugation; the twisted
right multiplications $\varrho_{\tilde P}(\tilde X)=\tilde X\tilde P^{\natural}$ compose by the **direct** law and are a
monoid isomorphic to $\mathbb{B}$; the right multiplications of the product do not close; the product has a left unit
and no right unit, hence no two-sided unit; the mixed composites commute and span the whole endomorphism algebra, of
complex dimension sixteen; the adjoint for the quaternionic form is $(L_{\tilde P})^{N}=L_{\tilde P^{\natural}}$, keeps
the side and conjugates the parameter; a one-sided operator is self-adjoint exactly for a central parameter,
skew-adjoint exactly for a pure one, and form-preserving exactly for norm one, and each multiplication scales the form
by the norm of its parameter with $\det L_{\tilde P}=N(\tilde P)^{2}$; the twisted two-sided operator
$\Theta_{\tilde A}=L_{\tilde A^{\natural}}\varrho_{\tilde A}$ is quadratic in its parameter and multiplicative up to
$N(\tilde A)$ for every parameter, its adjoint is $\Theta_{\tilde A^{\natural}}$, it is self-adjoint exactly for a
parameter in the centre or the vector subspace and never skew-adjoint, it preserves the form exactly for
$N(\tilde A)=\pm1$, and it equals $N(\tilde A)\mathrm{Ad}_{\tilde A}$ on the units, agreeing with the inner automorphism
exactly on the norm-one slice; the strictly multiplicative two-sided operators are the inner automorphisms, and the
multiplicative-up-to-a-scalar ones are exactly the scalar multiples of the twisted two-sided operators; and the left
actions restricted to the state space are a basis of its operators, differing from the plain basis only by the sign of
the vector directions, with the two algebraic norm projectors exchanged by the natural conjugation.

**Interpretations.** That the adjoint of the band is the **parameter conjugation on one side**, so that the interval can tell a
left attachment from a right one and a type is a property of a single parameter; that the norm is the **conformal factor**
of a multiplication and the **scalar of the two-sided composition**, and that its sign partitions the parameters into the
timelike, the null and the spacelike; that the **null parameters are the causal cone** and the norm-one parameters are the
Lorentz transformations; that the two-sided operator is **quadratic** in its parameter and **defined on every element**,
where the inner automorphism needs the inverse; that the skew-adjoint family is the vector subspace, a generator-like
family that does not close under composition; and that the process of the band is the opposite monoid, the element being
only a representative read through the conjugation. Each is the framework's naming of a proved algebraic fact and is
labelled as such.

## Physical Readings

The operators of the quaternionic product read as the two ways of attaching a material operation to an element —
through the interval on the first slot, as it stands on the second — and as the conjugation sandwich of the band. The
job word of the band is **causality**, and the operator layer supplies its four statements. The invariant form of the
band is the **interval**, the general quaternionic bilinear form of signature
$(3,1)$ on the material sector; the operators that preserve it are exactly the multiplications by a parameter of norm
one, and they are the **Lorentz transformations**. The set of parameters on which the interval vanishes is the **causal
cone** — the lightlike parameters, the zero divisors of the plain algebra — and the left multiplication by a null
parameter collapses the form, $N(L_{\tilde P}\tilde X)=0$ for every $\tilde X$, which is the operator picture of
lightlike propagation. The sign of the norm multiplies under the composition, so the division of the parameters into
the timelike, the null and the spacelike is compatible with the product, and this is the **causal division** of the
parameters: the band's own composition law carries the causal character of a product as the product of the causal
characters, the table of the four cells being *The Interval as the Square and the Charge of the Material Composition*.
The second interpretation is architectural: the composition of the band defines a monoid of operators and not an algebra, the
product being unital on one side alone; the operations compose and the elements do not, which is the operator form of
the orientation of the material composition and of its refusal to measure. The third interpretation is the
two-sided one. The sandwich of the band is the conjugation sandwich $\tilde X\mapsto\tilde A\tilde X\tilde A^{\natural}$,
quadratic in its parameter and defined on every element, and it is the inner automorphism scaled by the norm; on the
norm-one slice — the Lorentz parameters — it is the inner automorphism, so the Lorentz action is the sandwich, while off
the slice the two differ by the norm, which is the mass. The fourth interpretation is the type criterion: a one-sided operator
is self-adjoint exactly for a central parameter and skew-adjoint exactly for a pure one, so the two populated sectors of
the band are the centre, which carries the time direction, and the vector subspace, which carries the three spatial
directions; the two-sided operator is self-adjoint on the union of the two, and the skew family is the vector subspace
itself — the operator picture of the one negative time direction and the three positive spatial directions of the
interval. All four
are interpretations of the proved operator facts and are labelled as interpretations, not as derivations.

## Summary

The operators of the quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ are the left
multiplication $L_{\tilde P}(\tilde X)=\tilde P^{\natural}\tilde X$, the right multiplication
$R_{\tilde P}(\tilde X)=\tilde X^{\natural}\tilde P$ and the twisted right multiplication
$\varrho_{\tilde P}(\tilde X)=\tilde X\tilde P^{\natural}$, with the two-sided operators $L_{\tilde P}\varrho_{\tilde Q}$.
The left family composes by the **reversed** law $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$, so it is a monoid
$M_L\cong\mathbb{B}^{\mathrm{op}}$ anti-isomorphic to the plain multiplicative monoid, the anti-isomorphism lying in the
natural conjugation; the twisted right family composes by the **direct** law and is a monoid isomorphic to
$\mathbb{B}$; the right multiplication of the product does not close; the product has a left unit and no right unit, so
no two-sided unit; and the mixed composites commute and span the whole endomorphism algebra of complex dimension
sixteen. The form of the band is the general quaternionic bilinear form
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ of Gram matrix $I_4$, the polar form of the norm, and its
adjoint — the **quaternionic adjoint** ${}^{N}$ — **keeps the side** and carries the **parameter** through the natural
conjugation: $(L_{\tilde P})^{N}=L_{\tilde P^{\natural}}$ and $(\varrho_{\tilde P})^{N}=\varrho_{\tilde P^{\natural}}$.
Every type criterion is therefore a criterion on **one** parameter: a one-sided operator is self-adjoint exactly for a
central parameter, skew-adjoint exactly for a pure one, and form-preserving exactly for norm one, each multiplication
scaling the form by the norm of its parameter with determinant the square of that norm. The twisted two-sided operator
$\Theta_{\tilde A}=\tilde A[\,]\tilde A^{\natural}$ is **quadratic** in its parameter and **multiplicative up to the norm
for every parameter**, $\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\Theta_{\tilde A}(\tilde Y\tilde Z)$,
where the plain two-sided operator carried only a partial law and then only when the product of the two parameters was
central; its adjoint is $\Theta_{\tilde A^{\natural}}$, it is self-adjoint exactly for a parameter in the centre or the
vector subspace and never skew-adjoint, it preserves the form exactly for $N(\tilde A)=\pm1$, and it equals
$N(\tilde A)\mathrm{Ad}_{\tilde A}$ on the units, agreeing with the inner automorphism exactly on the norm-one slice. On
the state space the left actions exhaust the operators of the module up to the sign of the vector directions, the
twisted right actions are the commutant, and the two algebraic norm projectors are exchanged by the conjugation. Read on the
interval, the band is the causality band: the
invariant form is the interval of signature $(3,1)$, its null set the causal cone, the norm-one parameters are the
Lorentz transformations, and the division of the parameters by the sign of the norm is the causal division.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion complex space, basis $e_0=1,e_1,e_2,e_3$ |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product of the band |
| $\tilde P\tilde Q$ | the plain, associative product of the algebra |
| $L_{\tilde P}(\tilde X)=\tilde P\star\tilde X=\tilde P^{\natural}\tilde X$ | the left multiplication; the plain left multiplication by $\tilde P^{\natural}$ |
| $R_{\tilde P}(\tilde X)=\tilde X\star\tilde P=\tilde X^{\natural}\tilde P$ | the right multiplication of the product; it does not close |
| $\varrho_{\tilde P}(\tilde X)=\tilde X\tilde P^{\natural}$ | the twisted right multiplication, the closed mirror |
| $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ | the reversed composition law; $M_L\cong\mathbb{B}^{\mathrm{op}}$ |
| $\varrho_{\tilde P}\varrho_{\tilde R}=\varrho_{\tilde P\tilde R}$ | the direct composition law; $M_R\cong\mathbb{B}$ |
| $L_{\tilde P}\varrho_{\tilde Q}(\tilde X)=\tilde P^{\natural}\tilde X\tilde Q^{\natural}$ | the two-sided operators; span $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, dimension sixteen |
| $N(\tilde P,\tilde Q)=\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$ | the general quaternionic bilinear form, Gram $I_4$; the interval on $\mathbb{M}_-$ |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$ | the biquaternion norm; unit exactly when $N\neq0$ |
| ${}^{N}$ | the quaternionic adjoint, $(L_{\tilde P})^{N}=L_{\tilde P^{\natural}}$; keeps the side |
| $\Theta_{\tilde A}=L_{\tilde A^{\natural}}\varrho_{\tilde A}$ | the twisted two-sided operator, $\tilde A\tilde X\tilde A^{\natural}$; quadratic in $\tilde A$ |
| $(\Theta_{\tilde A})^{N}=\Theta_{\tilde A^{\natural}}$ | the adjoint of the sandwich |
| $\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\Theta_{\tilde A}(\tilde Y\tilde Z)$ | multiplicativity up to the norm, for every parameter |
| $\Theta_{\tilde A}=N(\tilde A)\mathrm{Ad}_{\tilde A}$ | the sandwich against the inner automorphism, on the units |

## Further Reading

- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the composition laws, the opposite monoid and the mixed composites.
- *One-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the adjoints for the quaternionic form, the types, the norm and the determinant of a multiplication.
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the twisted two-sided operator, its quadraticity, its multiplication law and its adjoint.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the isotope identity and the projectors, and *Introduction to the General Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the product and its elementary laws.
- *The Pin and Spin Groups of the General Quaternionic Algebra of Biquaternions*, for the groups cut out by the norm, and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, for the form, and *The Four General Products and Operators*, §*The Products Decide the Four Adjoints*, for its adjoint.
- The band articles: *The Interval as the Square and the Charge of the Material Composition*, for the interval, the mass shell and the closed causal cone, and *Why the Material Composition Is Oriented and Cannot Measure*, for the orientation, the one-sided unit and the opposite monoid read physically.
- *The Spinor Space as a Module and as a Hilbert Space* and *The Complementary Space of the Spinor Space and Its Physical Meaning*, for the state space the operators act on.
- *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*, the sibling operator article of the composition band, and *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, the crossing reader of the twelve.
