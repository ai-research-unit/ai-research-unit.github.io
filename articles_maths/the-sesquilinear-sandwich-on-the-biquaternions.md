
# __The Sesquilinear Sandwich on the Biquaternions__

## Introduction

The left and the right multiplication of the sesqualgebra $(\mathbb{B},\star)$ are one-sided: each puts a fixed element in one slot of the multiplication and leaves the other slot to the variable. The **sesquilinear sandwich** puts a fixed element in both outer slots and leaves the middle slot to the variable:

$$
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=(\tilde P\star\tilde X)\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*} .
$$

It is the two-sided operator of the multiplication, the operator analogue of the ordinary two-sided multiplication $\tilde X\mapsto\tilde P\tilde X\tilde Q$ of the algebra, and the whole difference between the two is the involution in the middle: $S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$, where $T_{\tilde P,\tilde Q^{*}}(\tilde X)=\tilde P\tilde X\tilde Q^{*}$ is the linear two-sided multiplication and ${}^{*}$ is the involution. The sandwich is therefore conjugate-linear, and it is the composite $R_{\tilde Q}L_{\tilde P}$ of the right and the left multiplication of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

Three properties fix the operator. It is conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second, so it carries one parity from the middle slot and one from the second parameter. The sandwiches are not closed under composition: the composite of two of them is the linear two-sided multiplication $T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$, the two conjugations cancelling, so the sandwiches together with the two-sided multiplications form a monoid in which the parity is multiplicative and the sandwiches are the conjugate-linear half. And the sandwich is invertible exactly when both parameters are units, with the explicit inverse $S_{\tilde Q^{-1},\tilde P^{-1}}$.

The article is the sixth of the batch and reads the general article *The Sesquilinear Sandwich Operator*, whose composition table and invertibility criterion are quoted; the two-sided multiplication it uses is the linear operator of the same article, and the two one-sided cases are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, above in this group. The ternary form of the sandwich is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*, and the operator of the ternary product is *The Ternary Product as an Operator*; the adjoint of the sandwich is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, below.

The setting is that of *Introduction to the General Plain Sesqualgebra of Biquaternions*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. Writing $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ for the ordinary two-sided multiplication, the sandwich is $S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$. The invertible elements are those with $N(\tilde Q)=Q_0^2+Q_1^2+Q_2^2+Q_3^2\neq0$, by *Biquaternion Norm and Invertibility*, and the rank of an element is the rank of its matrix in the model of *Biquaternion $2\times2$ Matrix Element Representation*.

## The Definition

### The Sandwich

**Definition.** For $\tilde P,\tilde Q\in\mathbb{B}$ the **sesquilinear sandwich** with the two parameters is the operator

$$
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*} .
$$

It is the two-sided operator of the multiplication, and it is additive in $\tilde X$ because the multiplication is additive in each variable.

**Proposition.** The sandwich is the ordinary two-sided multiplication composed with the involution,

$$
S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*} , \qquad T_{\tilde P,\tilde Q^{*}}(\tilde X)=\tilde P\tilde X\tilde Q^{*} ,
$$

and it is the composite $R_{\tilde Q}L_{\tilde P}$ of the right multiplication by $\tilde Q$ and the left multiplication by $\tilde P$.

**Proof.** $T_{\tilde P,\tilde Q^{*}}(\tilde X^{*})=\tilde P\tilde X^{*}\tilde Q^{*}=S_{\tilde P,\tilde Q}(\tilde X)$, which is the first display. For the second, $R_{\tilde Q}L_{\tilde P}(\tilde X)=R_{\tilde Q}(\tilde P\tilde X^{*})=(\tilde P\tilde X^{*})\tilde Q^{*}=S_{\tilde P,\tilde Q}(\tilde X)$; the composite of the two one-sided operators is the mixed composition $R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A}$ of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*, with $\tilde A=\tilde Q$ and $\tilde B=\tilde P$. $\square$

**Remark.** The second reading is the reason the sandwich is the two-sided completion of the one-sided actions: the left multiplication conjugates the variable and the right multiplication conjugates the parameter, and the two together conjugate both. The associativity of the algebra is what makes the composite well defined, and the failure of the associativity of the multiplication is what makes $S_{\tilde P,\tilde Q}$ different from $S$ with the two parameters interchanged; the two groupings of the triple $(\tilde P,\tilde X,\tilde Q)$ differ by the associator of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

### The Three Arguments

**Proposition (the parities).** The sandwich is conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second:

$$
S_{\tilde P,\tilde Q}(\lambda\tilde X)=\overline{\lambda}\,S_{\tilde P,\tilde Q}(\tilde X), \qquad
S_{\lambda\tilde P,\tilde Q}=\lambda\,S_{\tilde P,\tilde Q}, \qquad
S_{\tilde P,\lambda\tilde Q}=\overline{\lambda}\,S_{\tilde P,\tilde Q} .
$$

**Proof.** $S_{\tilde P,\tilde Q}(\lambda\tilde X)=\tilde P(\lambda\tilde X)^{*}\tilde Q^{*}=\overline{\lambda}\tilde P\tilde X^{*}\tilde Q^{*}$ by the conjugate-linearity of ${}^{*}$; the parameter readings are $(\lambda\tilde P)\tilde X^{*}\tilde Q^{*}=\lambda S_{\tilde P,\tilde Q}(\tilde X)$ and $\tilde P\tilde X^{*}(\lambda\tilde Q)^{*}=\overline{\lambda}S_{\tilde P,\tilde Q}(\tilde X)$. These are the parities of the general sandwich of *The Sesquilinear Sandwich Operator*, §*The Definition*, in the biquaternion notation. $\square$

**Remark.** The parity of the sandwich in its variable is that of the left multiplication and of the involution, and the parity of its parametrisation splits: linear in the left parameter, conjugate-linear in the right. The middle slot is the conjugate-linear one of the ternary product, which is the reason the sandwich, and not the ordinary two-sided multiplication, is the operator attached to the ternary structure.

### Two Elementary Values

**Proposition.** At the unit,

$$
S_{e_0,e_0}={}^{*} , \qquad S_{\tilde P,e_0}=L_{\tilde P} , \qquad S_{e_0,\tilde Q}=R_{\tilde Q}L_{e_0} = \text{the operator } \tilde X\mapsto\tilde X^{*}\tilde Q^{*} ,
$$

and $S_{e_0,e_0}$ is the involution of the algebra.

**Proof.** $S_{e_0,e_0}(\tilde X)=e_0\tilde X^{*}e_0=\tilde X^{*}$; $S_{\tilde P,e_0}(\tilde X)=\tilde P\tilde X^{*}=L_{\tilde P}(\tilde X)$ by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Definition*; and $S_{e_0,\tilde Q}(\tilde X)=\tilde X^{*}\tilde Q^{*}$. $\square$

**Remark.** The sandwich with a unit in the second slot is the left multiplication, and with a unit in the first slot it is the composite of the involution with the right multiplication. The two are not the two one-sided multiplications: the right multiplication is $S_{?}$ with a unit in the *first* slot only in the ordinary two-sided notation, and here the involution enters the middle. The asymmetry is the asymmetry of the multiplication, whose unit is a right unit alone.

## The Composition

### The Two Families Together

**Theorem (the composition table).** For all $\tilde A,\tilde B,\tilde C,\tilde D,\tilde P,\tilde Q,\tilde R,\tilde S$,

$$
S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}} , \qquad
T_{\tilde P,\tilde Q}S_{\tilde A,\tilde B}=S_{\tilde P\tilde A,\tilde Q^{*}\tilde B} ,
$$
$$
S_{\tilde C,\tilde D}T_{\tilde P,\tilde Q}=S_{\tilde C\tilde Q^{*},\tilde D\tilde P} , \qquad
T_{\tilde P,\tilde Q}T_{\tilde R,\tilde S}=T_{\tilde P\tilde R,\tilde S\tilde Q} .
$$

**Proof.** Each is the composition table of *The Sesquilinear Sandwich Operator*, §*The Multiplication Table*, transported to the sandwich $S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$; the first is the direct computation $S_{\tilde C,\tilde D}(S_{\tilde A,\tilde B}(\tilde X))=\tilde C(\tilde A\tilde X^{*}\tilde B^{*})^{*}\tilde D^{*}=\tilde C\tilde B\tilde X\tilde A^{*}\tilde D^{*}$, and the others are the same computation with one factor of the involution and one two-sided multiplication in each order. $\square$

**Corollary (the parity of a composite).** Two sandwiches compose to a two-sided multiplication, a sandwich and a two-sided multiplication in either order compose to a sandwich, and two two-sided multiplications compose to a two-sided multiplication. The set

$$
\{S_{\tilde P,\tilde Q}\}\cup\{T_{\tilde P,\tilde Q}\}
$$

is a monoid under composition with identity $T_{e_0,e_0}=\mathrm{id}$, in which the sandwiches are the conjugate-linear elements and the two-sided multiplications the linear ones.

**Proof.** The four identities of the theorem show that the parity of a composite is the product of the parities, and that each composite stays in one of the two families; the identity is $T_{e_0,e_0}$. $\square$

**Remark.** The parity is the whole content: the composite of two conjugate-linear maps is linear, so two sandwiches cannot compose to a sandwich, and the residue is an ordinary two-sided multiplication. This is the same phenomenon as for the left and the right multiplications, and it is why the operator theory of a sesqualgebra carries two families rather than one; the sandwich is the two-sided completion of the two one-sided families of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

### The Square and the Involution

**Corollary (the square).** For all $\tilde A,\tilde B$,

$$
S_{\tilde A,\tilde B}^{2}=T_{\tilde A\tilde B,\tilde A^{*}\tilde B^{*}} ,
$$

so a sandwich is an involution exactly when $\tilde A\tilde B=ce_0$ for some $c\in\mathbb{C}$ with $\lvert c\rvert=1$; in particular it is an involution as soon as $\tilde A\tilde B=e_0$ and $\tilde A^{*}\tilde B^{*}=e_0$.

**Proof.** The first identity is the theorem at $(\tilde C,\tilde D)=(\tilde A,\tilde B)$. For the criterion, $S^2=\mathrm{id}$ reads $T_{\tilde A\tilde B,\tilde A^{*}\tilde B^{*}}=T_{e_0,e_0}$. Now $T_{\tilde P,\tilde Q}=T_{e_0,e_0}$ holds exactly when $(\tilde P,\tilde Q)=(ce_0,c^{-1}e_0)$ for some $c\in\mathbb{C}^{\times}$: the equation $\tilde P\tilde X\tilde Q=\tilde X$ for every $\tilde X$ gives $\tilde P\tilde Q=e_0$ at $\tilde X=e_0$, so both are units with $\tilde Q=\tilde P^{-1}$, and then $\tilde P\tilde X\tilde P^{-1}=\tilde X$ for every $\tilde X$ forces $\tilde P$ to be central, that is $\tilde P=ce_0$. The criterion is therefore $\tilde A\tilde B=ce_0$ and $\tilde A^{*}\tilde B^{*}=c^{-1}e_0$ for some $c\in\mathbb{C}^{\times}$. The second equation follows from the first with the value $\bar c$: from $\tilde A\tilde B=ce_0$ one has $\tilde B=c\tilde A^{-1}$, hence $\tilde A^{*}\tilde B^{*}=\bar c\,\tilde A^{*}(\tilde A^{*})^{-1}=\bar c\,e_0$; the two amount to $\tilde A\tilde B=ce_0$ with $\bar c=c^{-1}$, that is $\lvert c\rvert=1$. The case $c=1$ is the sufficient condition of the display. $\square$

**Remark.** For a unitary $\tilde u$, so that $\tilde u\tilde u^{*}=e_0=\tilde u^{*}\tilde u$ by *Units and the Unitary Elements*, the sandwich $S_{\tilde u,\tilde u^{*}}$ is a reflection, $S_{\tilde u,\tilde u^{*}}(\tilde X)=\tilde u\tilde X^{*}\tilde u$, while $S_{\tilde u,\tilde u}(\tilde X)=\tilde u\tilde X^{*}\tilde u^{*}=\sigma_{\tilde u}(\tilde X)$ is the inner involution of *The Involutions of a Sesqualgebra*, an involution exactly when $\tilde u^{2}$ is central. The two families of *The Sesquilinear Sandwich Operator*, §*The Reflections*, are $S_{\tilde u,\tilde u}$ and $S_{\tilde u,\tilde u^{*}}$ in that notation; in the notation of this batch the two parameters are written with the unit in the second slot carrying the star, so the reflection is $S_{\tilde u,\tilde u^{*}}$ and the inner involution is $S_{\tilde u,\tilde u}$.

### The Invertible Sandwiches

**Theorem.** The sandwich $S_{\tilde P,\tilde Q}$ is invertible if and only if $\tilde P$ and $\tilde Q$ are units of $\mathbb{B}$, and then

$$
S_{\tilde P,\tilde Q}^{-1}=S_{\tilde Q^{-1},\tilde P^{-1}} .
$$

**Proof.** If $\tilde P$ or $\tilde Q$ is not a unit then the ordinary multiplication by it is not injective, by *Biquaternion Norm and Invertibility*, so $S_{\tilde P,\tilde Q}$ has a nonzero kernel and is not invertible. Conversely, for units, $S_{\tilde P,\tilde Q}S_{\tilde Q^{-1},\tilde P^{-1}}$ is $T_{\tilde P\tilde P^{-1},\tilde Q^{-1*}\tilde Q^{*}}=T_{e_0,e_0}$ by the composition table, and the same computation in the other order gives the identity as well. $\square$

**Remark.** The inverse exchanges the two parameters and inverts them, and in the general notation of *The Sesquilinear Sandwich Operator*, §*The Invertible Sandwiches*, the same statement is written $S_{a,b}^{-1}=S_{(b^{-1})^{*},(a^{-1})^{*}}$; the translation carries the star from the parameter to the last slot, which is the convention of this batch. The parametrisation is not injective: $S_{\tilde P\tilde Z,\tilde Q\tilde Z^{-1*}}=S_{\tilde P,\tilde Q}$ for a central unit $\tilde Z$, and on the units the kernel of the parametrisation is the group of the central units, which is $\mathbb{C}^{\times}e_0$ here.

## The Kernel and the Rank

### The Image

**Proposition.** The image of the sandwich is the set

$$
S_{\tilde P,\tilde Q}(\mathbb{B})=\tilde P\,\mathbb{B}\,\tilde Q^{*}=\{\tilde P\tilde Y\tilde Q^{*}:\tilde Y\in\mathbb{B}\} ,
$$

the two-sided ideal-like space generated by $\tilde P$ and $\tilde Q$; it is the image of the ordinary two-sided multiplication $T_{\tilde P,\tilde Q^{*}}$, since $\tilde X^{*}$ ranges over all of $\mathbb{B}$.

**Proof.** As $\tilde X$ ranges over $\mathbb{B}$ its conjugate $\tilde X^{*}$ ranges over all of $\mathbb{B}$, because the involution is bijective; hence $\{\tilde P\tilde X^{*}\tilde Q^{*}\}=\{\tilde P\tilde Y\tilde Q^{*}\}$, which is the image of $T_{\tilde P,\tilde Q^{*}}$. $\square$

### The Rank

**Theorem.** The dimension of the image of $S_{\tilde P,\tilde Q}$, and hence its rank as a conjugate-linear map, is the product of the ranks of the two parameters:

$$
\operatorname{rank}S_{\tilde P,\tilde Q}=\operatorname{rank}\tilde P\cdot\operatorname{rank}\tilde Q .
$$

In the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ of *Biquaternion $2\times2$ Matrix Element Representation*, the rank of an element is $0$, $1$ or $2$, and the possible ranks of a sandwich are $0$, $1$, $2$ and $4$.

**Proof.** Each parameter has rank $0$, $1$ or $2$ in the two-by-two model. The ordinary two-sided multiplication by a matrix of rank $r$ on the left and a matrix of rank $s$ on the right has image of dimension $rs$, the standard rank identity $\dim(A \mathsf{M}_2 B)=(\operatorname{rank}A)(\operatorname{rank}B)$; the sandwich has the same image by the proposition above, and the conjugation is a bijection. $\square$

**Corollary (the rank table).** With rank $2$ read as *a unit* and rank $1$ as *a zero divisor*,

| | $\tilde Q$ a unit | $\tilde Q$ a zero divisor | $\tilde Q=0$ |
|---|---|---|---|
| $\tilde P$ a unit | $4$, a conjugate-linear bijection | $2$ | $0$ |
| $\tilde P$ a zero divisor | $2$ | $1$ | $0$ |
| $\tilde P=0$ | $0$ | $0$ | $0$ |

**Proof.** The table is the theorem read with the three possible ranks of each parameter. $\square$

**Remark.** The sandwich therefore never has rank three, and it is invertible exactly in the top-left corner of the table, in agreement with §*The Invertible Sandwiches*. A sandwich is a rank-one operator exactly when both parameters are zero divisors, and it is the zero operator exactly when either parameter vanishes; the middle of the table is the family of the rank-two sandwiches, one parameter a unit and the other a zero divisor.

### The Kernel

**Corollary (the kernel).** The kernel of the sandwich has dimension

$$
\dim\ker S_{\tilde P,\tilde Q}=4-\operatorname{rank}\tilde P\cdot\operatorname{rank}\tilde Q ,
$$

so the sandwich is injective exactly when both parameters are units, and it has a two-dimensional kernel when one parameter is a unit and the other a zero divisor.

**Proof.** The rank formula $\dim\operatorname{im}+\dim\ker=4$ for a map of the four-dimensional complex space, with the image dimension from the theorem. $\square$

**Remark.** The kernel is the set of the $\tilde X$ with $\tilde P\tilde X^{*}\tilde Q^{*}=0$, whose conjugate is the set of the $\tilde Y$ with $\tilde P\tilde Y\tilde Q^{*}=0$, the two-sided annihilator of the pair $(\tilde P,\tilde Q^{*})$; the two-sided operators attached to a zero divisor therefore carry a two-dimensional kernel, which is the operator form of the fact that a zero divisor of $\mathbb{B}$ is neither injective nor surjective, by *Zero Divisors of the General Plain Algebra*.

## The Ternary Product and the Quadratic Representation

**Proposition.** The sandwich is the operator form of the ternary product with the variable in the middle:

$$
S_{\tilde P,\tilde Q}(\tilde X)=\{\tilde P,\tilde X,\tilde Q^{*}\} ,
$$

where $\{\tilde A,\tilde Y,\tilde B\}=\tilde A\tilde Y^{*}\tilde B$ is the ternary product of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

**Proof.** The ternary product of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra* is $\{\tilde A,\tilde Y,\tilde B\}=\tilde A\tilde Y^{*}\tilde B$, with the star in the middle slot alone; substituting $(\tilde A,\tilde Y,\tilde B)=(\tilde P,\tilde X,\tilde Q^{*})$ gives $\tilde P\tilde X^{*}\tilde Q^{*}=S_{\tilde P,\tilde Q}(\tilde X)$, which is the display. $\square$

**Remark.** The star on the third parameter is what makes the sandwich and the ternary product agree, and it is the same star that distinguishes the sandwich from the ordinary two-sided multiplication. The ternary product with the two parameters written without the star is the ordinary two-sided multiplication of the conjugated middle variable, $T_{\tilde P,\tilde Q}$, and not the sandwich; the difference of the two readings is the involution on the last parameter, and it is the operator form of the fact that the ternary product of the batch carries the involution in the middle slot of the sandwich and not on the outer parameters. The **quadratic representation** of the ternary product is the case in which the outer two variables are tied to one element, and it is the operator

$$
\tilde Z\longmapsto\{\tilde Z,\tilde Y,\tilde Z\}=\tilde Z\tilde Y^{*}\tilde Z=S_{\tilde Z,\tilde Z^{*}}(\tilde Y) ,
$$

the sandwich with the two parameters conjugate to each other and the middle variable $\tilde Y$.

**Remark.** The quadratic representation is the operator of *The Ternary Product as an Operator*, §*The Quadratic Representation*, read on $\mathbb{B}$; its adjoint, and the adjoint of the sandwich with arbitrary parameters, is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, below. The two operator families, the one-sided and the two-sided, are the whole of the operator theory that the multiplication carries, and the ternary product is the two-sided family read with one parameter tied.

## The Sandwich as the Two-Sided Action

**Proposition.** The sandwich is the two-sided action of the algebra on itself for the sesquilinear structure:

$$
S_{\tilde P,\tilde Q}=R_{\tilde Q}\circ L_{\tilde P} ,
$$

and the four composition laws of §*The Two Families Together* say that this action closes under composition and contains the identity.

**Proof.** The identity is §*The Definition*, and the closure is the composition table; the identity of the action is $S_{?}$ with both parameters the unit only in the ordinary two-sided reading, namely $T_{e_0,e_0}$, while $S_{e_0,e_0}={}^{*}$ is the involution and not the identity. $\square$

**Remark.** The two-sided action therefore does not contain the identity among the sandwiches: the identity is a two-sided multiplication and not a sandwich, exactly as the right unit $e_0$ is a right unit and not a left unit. The action is nevertheless a monoid once the two-sided multiplications are adjoined, and it is the largest operator family the sesqualgebra carries; the ordinary two-sided multiplications are the linear half and the sandwiches the conjugate-linear half.

**Remark (the ordinary two-sided multiplication).** The ordinary two-sided multiplication is the sandwich composed with the involution, $T_{\tilde P,\tilde Q}=S_{\tilde P,\tilde Q^{*}}\circ{}^{*}$, because $S_{\tilde P,\tilde Q^{*}}({}^{*}\tilde X)=\tilde P(\tilde X^{*})^{*}(\tilde Q^{*})^{*}=\tilde P\tilde X\tilde Q$. It is the linear shadow of the sandwich, and hence the whole operator theory of the algebra is generated by the two-sided family and the involution; the sandwich is the operator of the sesquilinear structure and the ordinary two-sided multiplication its linear rescaling, exactly as the left multiplication is the conjugate-linear shadow of the ordinary left multiplication.

## Worked Cases

### The Projections

**Example.** Let $\tilde\Pi=\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ be a projection of *Projections of the Biquaternion Sesqualgebra*, of rank one in the matrix model, and consider $S_{\tilde\Pi,\tilde\Pi}$. Its image is $\tilde\Pi\mathbb{B}\tilde\Pi^{*}$, of dimension $1$, so the sandwich of a projection with itself is a rank-one conjugate-linear operator; the same holds for $S_{\tilde\Pi,\tilde\Pi^{\perp}}$ with $\tilde\Pi^{\perp}=e_0-\tilde\Pi$. The two projections $\tilde\Pi$ and $\tilde\Pi^{\perp}$ are idempotents of the multiplication, so that $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ and $S_{\tilde\Pi,e_0}=L_{\tilde\Pi}$ fixes $\tilde\Pi$.

**Proof.** The rank of $\tilde\Pi$ is one, so the rank theorem gives $\operatorname{rank}S_{\tilde\Pi,\tilde\Pi}=1$; the identity $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ is the idempotence of the projection, and $S_{\tilde\Pi,e_0}=L_{\tilde\Pi}$ is §*Two Elementary Values*. $\square$

### The Basis

**Example.** On the basis,

$$
S_{e_\mu,e_\nu}(e_\lambda)=e_\mu e_\lambda^{*}e_\nu^{*}=\varepsilon_\lambda\varepsilon_\nu\,e_\mu e_\lambda e_\nu ,
$$

so the sandwich of two basis elements sends each basis element to a basis element up to the sign $\varepsilon_\lambda\varepsilon_\nu$ and the signs of the quaternion table. For $\mu=\nu=0$ the operator is the involution, $S_{e_0,e_0}(e_\lambda)=\varepsilon_\lambda e_\lambda=e_\lambda^{*}$.

**Proof.** Substituting $e_\lambda^{*}=\varepsilon_\lambda e_\lambda$ and $e_\nu^{*}=\varepsilon_\nu e_\nu$ from the basis table of *Introduction to the General Plain Sesqualgebra of Biquaternions* in the definition gives the display; the case $\mu=\nu=0$ is §*Two Elementary Values*. $\square$

## Summary

The sesquilinear sandwich is $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$, the two-sided operator of the multiplication, conjugate-linear in its variable, linear in the first parameter and conjugate-linear in the second, and equal to the composite $R_{\tilde Q}L_{\tilde P}$ of the right and the left multiplication. Its image is $\tilde P\mathbb{B}\tilde Q^{*}$ and its rank is the product of the ranks of its two parameters, taking the values $0$, $1$, $2$, $4$; it is invertible exactly when both parameters are units, with $S_{\tilde P,\tilde Q}^{-1}=S_{\tilde Q^{-1},\tilde P^{-1}}$.

Two sandwiches compose to the linear two-sided multiplication $T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$, a sandwich and a two-sided multiplication compose to a sandwich, and the two families together form a monoid with identity $T_{e_0,e_0}$; the sandwiches are its conjugate-linear half. A unitary parameter gives the reflection $S_{\tilde u,\tilde u^{*}}$ and the inner involution $S_{\tilde u,\tilde u}$. The sandwich is the operator form of the ternary product, the quadratic representation being the case of conjugate parameters, and it is the two-sided action of the algebra, whose linear shadow is the ordinary two-sided multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*}$ | the sesquilinear sandwich, conjugate-linear |
| $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ | the ordinary two-sided multiplication, linear |
| $S_{\tilde P,\tilde Q}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$ | the sandwich as the two-sided multiplication with the involution |
| $L_{\tilde P}(\tilde X)=\tilde P\tilde X^{*}$, $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q^{*}$ | the left and the right multiplication |
| $S_{\tilde P,\tilde Q}=R_{\tilde Q}\circ L_{\tilde P}$ | the sandwich as the mixed composite |
| $S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$ | the composite of two sandwiches |
| $S_{\tilde A,\tilde B}^{2}=T_{\tilde A\tilde B,\tilde A^{*}\tilde B^{*}}$ | the square of a sandwich |
| $S_{\tilde P,\tilde Q}^{-1}=S_{\tilde Q^{-1},\tilde P^{-1}}$ | the inverse on the units |
| $\operatorname{rank}S_{\tilde P,\tilde Q}=\operatorname{rank}\tilde P\cdot\operatorname{rank}\tilde Q$ | the rank of a sandwich |
| $S_{\tilde\Pi,\tilde\Pi}$ | the rank-one sandwich of a projection |
| $\{\tilde A,\tilde Y,\tilde B\}=\tilde A\tilde Y^{*}\tilde B$ | the ternary product |
| $\tilde Z\mapsto\tilde Z\tilde Y^{*}\tilde Z=S_{\tilde Z,\tilde Z^{*}}(\tilde Y)$ | the quadratic representation |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the triple products of a ring with involution and the operators they induce.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the sandwich operators of a ring with involution and the conjugate-linear maps attached to them.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the semilinear operators, the two-sided multiplications and the case of the trivial involution.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the triple product $xy^{*}z$ and the quadratic representation it defines.
- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), for the triple product $xy^{*}z$, the quadratic representation and its operator forms.
