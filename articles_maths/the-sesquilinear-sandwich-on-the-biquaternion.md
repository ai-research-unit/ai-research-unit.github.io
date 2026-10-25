
# __The Sesquilinear Sandwich on the Biquaternion__

## Introduction

The left and the right multiplication of the sesqualgebra $(\mathbb{B},\star)$ are one-sided: each puts a fixed element in one slot of the multiplication and leaves the other slot to the variable. The **sesquilinear sandwich** puts a fixed element in both outer slots and leaves the middle slot to the variable:

$$
S_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\star\tilde Q_1\star\tilde Q_2=(\tilde Q\star\tilde Q_1)\star\tilde Q_2=\tilde Q\tilde Q_1^{*}\tilde Q_2^{*} .
$$

It is the two-sided operator of the multiplication, the operator analogue of the ordinary two-sided multiplication $\tilde Q_1\mapsto\tilde Q\tilde Q_1\tilde Q_2$ of the algebra, and the whole difference between the two is the involution in the middle: $S_{\tilde Q,\tilde Q_2}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$, where $T_{\tilde Q,\tilde Q_2^{*}}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_2^{*}$ is the linear two-sided multiplication and ${}^{*}$ is the involution. The sandwich is therefore conjugate-linear, and it is the composite $R_{\tilde Q_2}L_{\tilde Q}$ of the right and the left multiplication of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

Three properties fix the operator. It is conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second, so it carries one parity from the middle slot and one from the second parameter. The sandwiches are not closed under composition: the composite of two of them is the linear two-sided multiplication $T_{\tilde Q_3\tilde Q_2,\tilde Q_8^{*}\tilde Q_9^{*}}$, the two conjugations cancelling, so the sandwiches together with the two-sided multiplications form a monoid in which the parity is multiplicative and the sandwiches are the conjugate-linear half. And the sandwich is invertible exactly when both parameters are units, with the explicit inverse $S_{\tilde Q_2^{-1},\tilde Q^{-1}}$.

The article is the sixth of the batch and reads the general article *The Sesquilinear Sandwich Operator*, whose composition table and invertibility criterion are quoted; the two-sided multiplication it uses is the linear operator of the same article, and the two one-sided cases are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, above in this group. The ternary form of the sandwich is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*, and the operator of the ternary product is *The Ternary Product as an Operator*; the adjoint of the sandwich is *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*, below.

The setting is that of *Introduction to the General Plain Sesqualgebra*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde Q\star\tilde Q_2=\tilde Q\tilde Q_2^{*}$. Writing $T_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_2$ for the ordinary two-sided multiplication, the sandwich is $S_{\tilde Q,\tilde Q_2}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$. The invertible elements are those with $\langle\tilde Q_2\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$, by *N-Regularity and Degeneracy in the Biquaternion Algebra*, and the rank of an element is the rank of its matrix in the model of *Biquaternion $2\times2$ Matrix Element Representation*.

## The Definition

### The Sandwich

**Definition.** For $\tilde Q,\tilde Q_2\in\mathbb{B}$ the **sesquilinear sandwich** with the two parameters is the operator

$$
S_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\star\tilde Q_1\star\tilde Q_2=\tilde Q\tilde Q_1^{*}\tilde Q_2^{*} .
$$

It is the two-sided operator of the multiplication, and it is additive in $\tilde Q_1$ because the multiplication is additive in each variable.

**Proposition.** The sandwich is the ordinary two-sided multiplication composed with the involution,

$$
\boxed{\;S_{\tilde Q,\tilde Q_2}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*} , \qquad T_{\tilde Q,\tilde Q_2^{*}}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_2^{*}\;},
$$

and it is the composite $R_{\tilde Q_2}L_{\tilde Q}$ of the right multiplication by $\tilde Q_2$ and the left multiplication by $\tilde Q$.

**Proof.** $T_{\tilde Q,\tilde Q_2^{*}}(\tilde Q_1^{*})=\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}=S_{\tilde Q,\tilde Q_2}(\tilde Q_1)$, which is the first display. For the second, $R_{\tilde Q_2}L_{\tilde Q}(\tilde Q_1)=R_{\tilde Q_2}(\tilde Q\tilde Q_1^{*})=(\tilde Q\tilde Q_1^{*})\tilde Q_2^{*}=S_{\tilde Q,\tilde Q_2}(\tilde Q_1)$; the composite of the two one-sided operators is the mixed composition $R_{\tilde Q_8}L_{\tilde Q_2}=S_{\tilde Q_2,\tilde Q_8}$ of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*, with $\tilde Q_8=\tilde Q_2$ and $\tilde Q_2=\tilde Q$.

**Remark.** The second reading is the reason the sandwich is the two-sided completion of the one-sided actions: the left multiplication conjugates the variable and the right multiplication conjugates the parameter, and the two together conjugate both. The associativity of the algebra is what makes the composite well defined, and the failure of the associativity of the multiplication is what makes $S_{\tilde Q,\tilde Q_2}$ different from $S$ with the two parameters interchanged; the two groupings of the triple $(\tilde Q,\tilde Q_1,\tilde Q_2)$ differ by the associator of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

### The Three Arguments

**Proposition (the parities).** The sandwich is conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second:

$$
S_{\tilde Q,\tilde Q_2}(\lambda\tilde Q_1)=\overline{\lambda}\,S_{\tilde Q,\tilde Q_2}(\tilde Q_1), \qquad
S_{\lambda\tilde Q,\tilde Q_2}=\lambda\,S_{\tilde Q,\tilde Q_2}, \qquad
S_{\tilde Q,\lambda\tilde Q_2}=\overline{\lambda}\,S_{\tilde Q,\tilde Q_2} .
$$

**Proof.** $S_{\tilde Q,\tilde Q_2}(\lambda\tilde Q_1)=\tilde Q(\lambda\tilde Q_1)^{*}\tilde Q_2^{*}=\overline{\lambda}\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}$ by the conjugate-linearity of ${}^{*}$; the parameter readings are $(\lambda\tilde Q)\tilde Q_1^{*}\tilde Q_2^{*}=\lambda S_{\tilde Q,\tilde Q_2}(\tilde Q_1)$ and $\tilde Q\tilde Q_1^{*}(\lambda\tilde Q_2)^{*}=\overline{\lambda}S_{\tilde Q,\tilde Q_2}(\tilde Q_1)$. These are the parities of the general sandwich of *The Sesquilinear Sandwich Operator*, §*The Definition*, in the biquaternion notation.

**Remark.** The parity of the sandwich in its variable is that of the left multiplication and of the involution, and the parity of its parametrisation splits: linear in the left parameter, conjugate-linear in the right. The middle slot is the conjugate-linear one of the ternary product, which is the reason the sandwich, and not the ordinary two-sided multiplication, is the operator attached to the ternary structure.

### Two Elementary Values

**Proposition.** At the unit,

$$
S_{e_t,e_t}={}^{*} , \qquad S_{\tilde Q,e_t}=L_{\tilde Q} , \qquad S_{e_t,\tilde Q_2}=R_{\tilde Q_2}L_{e_t} = \text{the operator } \tilde Q_1\mapsto\tilde Q_1^{*}\tilde Q_2^{*} ,
$$

and $S_{e_t,e_t}$ is the involution of the algebra.

**Proof.** $S_{e_t,e_t}(\tilde Q_1)=e_t\tilde Q_1^{*}e_t=\tilde Q_1^{*}$; $S_{\tilde Q,e_t}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}=L_{\tilde Q}(\tilde Q_1)$ by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Definition*; and $S_{e_t,\tilde Q_2}(\tilde Q_1)=\tilde Q_1^{*}\tilde Q_2^{*}$.

**Remark.** The sandwich with a unit in the second slot is the left multiplication, and with a unit in the first slot it is the composite of the involution with the right multiplication. The two are not the two one-sided multiplications: the right multiplication is $S_{?}$ with a unit in the *first* slot only in the ordinary two-sided notation, and here the involution enters the middle. The asymmetry is the asymmetry of the multiplication, whose unit is a right unit alone.

## The Composition

### The Two Families Together

**Theorem (the composition table).** For all $\tilde Q_8,\tilde Q_2,\tilde Q_3,\tilde Q_9,\tilde Q,\tilde Q_7,\tilde Q_6,\tilde S$,

$$
S_{\tilde Q_3,\tilde Q_9}S_{\tilde Q_8,\tilde Q_2}=T_{\tilde Q_3\tilde Q_2,\tilde Q_8^{*}\tilde Q_9^{*}} , \qquad
T_{\tilde Q,\tilde Q_7}S_{\tilde Q_8,\tilde Q_2}=S_{\tilde Q\tilde Q_8,\tilde Q_7^{*}\tilde Q_2} ,
$$
$$
S_{\tilde Q_3,\tilde Q_9}T_{\tilde Q,\tilde Q_7}=S_{\tilde Q_3\tilde Q_7^{*},\tilde Q_9\tilde Q} , \qquad
T_{\tilde Q,\tilde Q_7}T_{\tilde Q_6,\tilde S}=T_{\tilde Q\tilde Q_6,\tilde S\tilde Q_7} .
$$

**Proof.** Each is the composition table of *The Sesquilinear Sandwich Operator*, §*The Multiplication Table*, transported to the sandwich $S_{\tilde Q,\tilde Q_2}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$; the first is the direct computation $S_{\tilde Q_3,\tilde Q_9}(S_{\tilde Q_8,\tilde Q_2}(\tilde Q_1))=\tilde Q_3(\tilde Q_8\tilde Q_1^{*}\tilde Q_2^{*})^{*}\tilde Q_9^{*}=\tilde Q_3\tilde Q_2\tilde Q_1\tilde Q_8^{*}\tilde Q_9^{*}$, and the others are the same computation with one factor of the involution and one two-sided multiplication in each order.

**Corollary (the parity of a composite).** Two sandwiches compose to a two-sided multiplication, a sandwich and a two-sided multiplication in either order compose to a sandwich, and two two-sided multiplications compose to a two-sided multiplication. The set

$$
\{S_{\tilde Q,\tilde Q_2}\}\cup\{T_{\tilde Q,\tilde Q_2}\}
$$

is a monoid under composition with identity $T_{e_t,e_t}=\mathrm{id}$, in which the sandwiches are the conjugate-linear elements and the two-sided multiplications the linear ones.

**Proof.** The four identities of the theorem show that the parity of a composite is the product of the parities, and that each composite stays in one of the two families; the identity is $T_{e_t,e_t}$.

**Remark.** The parity is the whole content: the composite of two conjugate-linear maps is linear, so two sandwiches cannot compose to a sandwich, and the residue is an ordinary two-sided multiplication. This is the same phenomenon as for the left and the right multiplications, and it is why the operator theory of a sesqualgebra carries two families rather than one; the sandwich is the two-sided completion of the two one-sided families of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

### The Square and the Involution

**Corollary (the square).** For all $\tilde Q_8,\tilde Q_2$,

$$
S_{\tilde Q_8,\tilde Q_2}^{2}=T_{\tilde Q_8\tilde Q_2,\tilde Q_8^{*}\tilde Q_2^{*}} ,
$$

so a sandwich is an involution exactly when $\tilde Q_8\tilde Q_2=ce_t$ for some $c\in\mathbb{C}$ with $\lvert c\rvert=1$; in particular it is an involution as soon as $\tilde Q_8\tilde Q_2=e_t$ and $\tilde Q_8^{*}\tilde Q_2^{*}=e_t$.

**Proof.** The first identity is the theorem at $(\tilde Q_3,\tilde Q_9)=(\tilde Q_8,\tilde Q_2)$. For the criterion, $S^2=\mathrm{id}$ reads $T_{\tilde Q_8\tilde Q_2,\tilde Q_8^{*}\tilde Q_2^{*}}=T_{e_t,e_t}$. Now $T_{\tilde Q,\tilde Q_2}=T_{e_t,e_t}$ holds exactly when $(\tilde Q,\tilde Q_2)=(ce_t,c^{-1}e_t)$ for some $c\in\mathbb{C}^{\times}$: the equation $\tilde Q\tilde Q_1\tilde Q_2=\tilde Q_1$ for every $\tilde Q_1$ gives $\tilde Q\tilde Q_2=e_t$ at $\tilde Q_1=e_t$, so both are units with $\tilde Q_2=\tilde Q^{-1}$, and then $\tilde Q\tilde Q_1\tilde Q^{-1}=\tilde Q_1$ for every $\tilde Q_1$ forces $\tilde Q$ to be central, that is $\tilde Q=ce_t$. The criterion is therefore $\tilde Q_8\tilde Q_2=ce_t$ and $\tilde Q_8^{*}\tilde Q_2^{*}=c^{-1}e_t$ for some $c\in\mathbb{C}^{\times}$. The second equation follows from the first with the value $\bar c$: from $\tilde Q_8\tilde Q_2=ce_t$ one has $\tilde Q_2=c\tilde Q_8^{-1}$, hence $\tilde Q_8^{*}\tilde Q_2^{*}=\bar c\,\tilde Q_8^{*}(\tilde Q_8^{*})^{-1}=\bar c\,e_t$; the two amount to $\tilde Q_8\tilde Q_2=ce_t$ with $\bar c=c^{-1}$, that is $\lvert c\rvert=1$. The case $c=1$ is the sufficient condition of the display.

**Remark.** For a unitary $\tilde u$, so that $\tilde u\tilde u^{*}=e_t=\tilde u^{*}\tilde u$ by *Units and the Unitary Elements*, the sandwich $S_{\tilde u,\tilde u^{*}}$ is a reflection, $S_{\tilde u,\tilde u^{*}}(\tilde Q_1)=\tilde u\tilde Q_1^{*}\tilde u$, while $S_{\tilde u,\tilde u}(\tilde Q_1)=\tilde u\tilde Q_1^{*}\tilde u^{*}=\sigma_{\tilde u}(\tilde Q_1)$ is the inner involution of *The Involutions of a Sesqualgebra*, an involution exactly when $\tilde u^{2}$ is central. The two families of *The Sesquilinear Sandwich Operator*, §*The Reflections*, are $S_{\tilde u,\tilde u}$ and $S_{\tilde u,\tilde u^{*}}$ in that notation; in the notation of this batch the two parameters are written with the unit in the second slot carrying the star, so the reflection is $S_{\tilde u,\tilde u^{*}}$ and the inner involution is $S_{\tilde u,\tilde u}$.

### The Invertible Sandwiches

**Theorem.** The sandwich $S_{\tilde Q,\tilde Q_2}$ is invertible if and only if $\tilde Q$ and $\tilde Q_2$ are units of $\mathbb{B}$, and then

$$
\boxed{\;S_{\tilde Q,\tilde Q_2}^{-1}=S_{\tilde Q_2^{-1},\tilde Q^{-1}}\;}.
$$

**Proof.** If $\tilde Q$ or $\tilde Q_2$ is not a unit then the ordinary multiplication by it is not injective, by *N-Regularity and Degeneracy in the Biquaternion Algebra*, so $S_{\tilde Q,\tilde Q_2}$ has a nonzero kernel and is not invertible. Conversely, for units, $S_{\tilde Q,\tilde Q_2}S_{\tilde Q_2^{-1},\tilde Q^{-1}}$ is $T_{\tilde Q\tilde Q^{-1},\tilde Q_2^{-1*}\tilde Q_2^{*}}=T_{e_t,e_t}$ by the composition table, and the same computation in the other order gives the identity as well.

**Remark.** The inverse exchanges the two parameters and inverts them, and in the general notation of *The Sesquilinear Sandwich Operator*, §*The Invertible Sandwiches*, the same statement is written $S_{a,b}^{-1}=S_{(b^{-1})^{*},(a^{-1})^{*}}$; the translation carries the star from the parameter to the last slot, which is the convention of this batch. The parametrisation is not injective: $S_{\tilde Q\tilde Q_4,\tilde Q_2\tilde Q_4^{-1*}}=S_{\tilde Q,\tilde Q_2}$ for a central unit $\tilde Q_4$, and on the units the kernel of the parametrisation is the group of the central units, which is $\mathbb{C}^{\times}e_t$ here.

## The Kernel and the Rank

### The Image

**Proposition.** The image of the sandwich is the set

$$
S_{\tilde Q,\tilde Q_2}(\mathbb{B})=\tilde Q\,\mathbb{B}\,\tilde Q_2^{*}=\{\tilde Q\tilde Q_5\tilde Q_2^{*}:\tilde Q_5\in\mathbb{B}\} ,
$$

the two-sided ideal-like space generated by $\tilde Q$ and $\tilde Q_2$; it is the image of the ordinary two-sided multiplication $T_{\tilde Q,\tilde Q_2^{*}}$, since $\tilde Q_1^{*}$ ranges over all of $\mathbb{B}$.

**Proof.** As $\tilde Q_1$ ranges over $\mathbb{B}$ its conjugate $\tilde Q_1^{*}$ ranges over all of $\mathbb{B}$, because the involution is bijective; hence $\{\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}\}=\{\tilde Q\tilde Q_5\tilde Q_2^{*}\}$, which is the image of $T_{\tilde Q,\tilde Q_2^{*}}$.

### The Rank

**Theorem.** The dimension of the image of $S_{\tilde Q,\tilde Q_2}$, and hence its rank as a conjugate-linear map, is the product of the ranks of the two parameters:

$$
\boxed{\;\operatorname{rank}S_{\tilde Q,\tilde Q_2}=\operatorname{rank}\tilde Q\cdot\operatorname{rank}\tilde Q_2\;}.
$$

In the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ of *Biquaternion $2\times2$ Matrix Element Representation*, the rank of an element is $0$, $1$ or $2$, and the possible ranks of a sandwich are $0$, $1$, $2$ and $4$.

**Proof.** Each parameter has rank $0$, $1$ or $2$ in the two-by-two model. The ordinary two-sided multiplication by a matrix of rank $r$ on the left and a matrix of rank $s$ on the right has image of dimension $rs$, the standard rank identity $\dim(A \mathsf{M}_2 B)=(\operatorname{rank}A)(\operatorname{rank}B)$; the sandwich has the same image by the proposition above, and the conjugation is a bijection.

**Corollary (the rank table).** With rank $2$ read as *a unit* and rank $1$ as *a zero divisor*,

| | $\tilde Q_2$ a unit | $\tilde Q_2$ a zero divisor | $\tilde Q_2=0$ |
|---|---|---|---|
| $\tilde Q$ a unit | $4$, a conjugate-linear bijection | $2$ | $0$ |
| $\tilde Q$ a zero divisor | $2$ | $1$ | $0$ |
| $\tilde Q=0$ | $0$ | $0$ | $0$ |

**Proof.** The table is the theorem read with the three possible ranks of each parameter.

**Remark.** The sandwich therefore never has rank three, and it is invertible exactly in the top-left corner of the table, in agreement with §*The Invertible Sandwiches*. A sandwich is a rank-one operator exactly when both parameters are zero divisors, and it is the zero operator exactly when either parameter vanishes; the middle of the table is the family of the rank-two sandwiches, one parameter a unit and the other a zero divisor.

### The Kernel

**Corollary (the kernel).** The kernel of the sandwich has dimension

$$
\dim\ker S_{\tilde Q,\tilde Q_2}=4-\operatorname{rank}\tilde Q\cdot\operatorname{rank}\tilde Q_2 ,
$$

so the sandwich is injective exactly when both parameters are units, and it has a two-dimensional kernel when one parameter is a unit and the other a zero divisor.

**Proof.** The rank formula $\dim\operatorname{im}+\dim\ker=4$ for a map of the four-dimensional complex space, with the image dimension from the theorem.

**Remark.** The kernel is the set of the $\tilde Q_1$ with $\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}=0$, whose conjugate is the set of the $\tilde Q_5$ with $\tilde Q\tilde Q_5\tilde Q_2^{*}=0$, the two-sided annihilator of the pair $(\tilde Q,\tilde Q_2^{*})$; the two-sided operators attached to a zero divisor therefore carry a two-dimensional kernel, which is the operator form of the fact that a zero divisor of $\mathbb{B}$ is neither injective nor surjective, by *N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

## The Ternary Product and the Quadratic Representation

**Proposition.** The sandwich is the operator form of the ternary product with the variable in the middle:

$$
S_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\{\tilde Q,\tilde Q_1,\tilde Q_2^{*}\} ,
$$

where $\{\tilde Q_8,\tilde Q_5,\tilde Q_2\}=\tilde Q_8\tilde Q_5^{*}\tilde Q_2$ is the ternary product of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

**Proof.** The ternary product of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra* is $\{\tilde Q_8,\tilde Q_5,\tilde Q_2\}=\tilde Q_8\tilde Q_5^{*}\tilde Q_2$, with the star in the middle slot alone; substituting $(\tilde Q_8,\tilde Q_5,\tilde Q_2)=(\tilde Q,\tilde Q_1,\tilde Q_2^{*})$ gives $\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}=S_{\tilde Q,\tilde Q_2}(\tilde Q_1)$, which is the display.

**Remark.** The star on the third parameter is what makes the sandwich and the ternary product agree, and it is the same star that distinguishes the sandwich from the ordinary two-sided multiplication. The ternary product with the two parameters written without the star is the ordinary two-sided multiplication of the conjugated middle variable, $T_{\tilde Q,\tilde Q_2}$, and not the sandwich; the difference of the two readings is the involution on the last parameter, and it is the operator form of the fact that the ternary product of the batch carries the involution in the middle slot of the sandwich and not on the outer parameters. The **quadratic representation** of the ternary product is the case in which the outer two variables are tied to one element, and it is the operator

$$
\tilde Q_4\longmapsto\{\tilde Q_4,\tilde Q_5,\tilde Q_4\}=\tilde Q_4\tilde Q_5^{*}\tilde Q_4=S_{\tilde Q_4,\tilde Q_4^{*}}(\tilde Q_5) ,
$$

the sandwich with the two parameters conjugate to each other and the middle variable $\tilde Q_5$.

**Remark.** The quadratic representation is the operator of *The Ternary Product as an Operator*, §*The Quadratic Representation*, read on $\mathbb{B}$; its adjoint, and the adjoint of the sandwich with arbitrary parameters, is *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*, below. The two operator families, the one-sided and the two-sided, are the whole of the operator theory that the multiplication carries, and the ternary product is the two-sided family read with one parameter tied.

## The Sandwich as the Two-Sided Action

**Proposition.** The sandwich is the two-sided action of the algebra on itself for the sesquilinear structure:

$$
S_{\tilde Q,\tilde Q_2}=R_{\tilde Q_2}\circ L_{\tilde Q} ,
$$

and the four composition laws of §*The Two Families Together* say that this action closes under composition and contains the identity.

**Proof.** The identity is §*The Definition*, and the closure is the composition table; the identity of the action is $S_{?}$ with both parameters the unit only in the ordinary two-sided reading, namely $T_{e_t,e_t}$, while $S_{e_t,e_t}={}^{*}$ is the involution and not the identity.

**Remark.** The two-sided action therefore does not contain the identity among the sandwiches: the identity is a two-sided multiplication and not a sandwich, exactly as the right unit $e_t$ is a right unit and not a left unit. The action is nevertheless a monoid once the two-sided multiplications are adjoined, and it is the largest operator family the sesqualgebra carries; the ordinary two-sided multiplications are the linear half and the sandwiches the conjugate-linear half.

**Remark (the ordinary two-sided multiplication).** The ordinary two-sided multiplication is the sandwich composed with the involution, $T_{\tilde Q,\tilde Q_2}=S_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$, because $S_{\tilde Q,\tilde Q_2^{*}}({}^{*}\tilde Q_1)=\tilde Q(\tilde Q_1^{*})^{*}(\tilde Q_2^{*})^{*}=\tilde Q\tilde Q_1\tilde Q_2$. It is the linear shadow of the sandwich, and hence the whole operator theory of the algebra is generated by the two-sided family and the involution; the sandwich is the operator of the sesquilinear structure and the ordinary two-sided multiplication its linear rescaling, exactly as the left multiplication is the conjugate-linear shadow of the ordinary left multiplication.

## Worked Cases

### The Projections

**Example.** Let $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ be a projection of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, of rank one in the matrix model, and consider $S_{\tilde\Pi,\tilde\Pi}$. Its image is $\tilde\Pi\mathbb{B}\tilde\Pi^{*}$, of dimension $1$, so the sandwich of a projection with itself is a rank-one conjugate-linear operator; the same holds for $S_{\tilde\Pi,\tilde\Pi^{\perp}}$ with $\tilde\Pi^{\perp}=e_t-\tilde\Pi$. The two projections $\tilde\Pi$ and $\tilde\Pi^{\perp}$ are idempotents of the multiplication, so that $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ and $S_{\tilde\Pi,e_t}=L_{\tilde\Pi}$ fixes $\tilde\Pi$.

**Proof.** The rank of $\tilde\Pi$ is one, so the rank theorem gives $\operatorname{rank}S_{\tilde\Pi,\tilde\Pi}=1$; the identity $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ is the idempotence of the projection, and $S_{\tilde\Pi,e_t}=L_{\tilde\Pi}$ is §*Two Elementary Values*.

### The Basis

**Example.** On the basis,

$$
S_{e_\mu,e_\nu}(e_\lambda)=e_\mu e_\lambda^{*}e_\nu^{*}=\varepsilon_\lambda\varepsilon_\nu\,e_\mu e_\lambda e_\nu ,
$$

so the sandwich of two basis elements sends each basis element to a basis element up to the sign $\varepsilon_\lambda\varepsilon_\nu$ and the signs of the quaternion table. For $\mu=\nu=0$ the operator is the involution, $S_{e_t,e_t}(e_\lambda)=\varepsilon_\lambda e_\lambda=e_\lambda^{*}$.

**Proof.** Substituting $e_\lambda^{*}=\varepsilon_\lambda e_\lambda$ and $e_\nu^{*}=\varepsilon_\nu e_\nu$ from the basis table of *Introduction to the General Plain Sesqualgebra* in the definition gives the display; the case $\mu=\nu=0$ is §*Two Elementary Values*.

## Summary

The sesquilinear sandwich is $S_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\star\tilde Q_1\star\tilde Q_2=\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$, the two-sided operator of the multiplication, conjugate-linear in its variable, linear in the first parameter and conjugate-linear in the second, and equal to the composite $R_{\tilde Q_2}L_{\tilde Q}$ of the right and the left multiplication. Its image is $\tilde Q\mathbb{B}\tilde Q_2^{*}$ and its rank is the product of the ranks of its two parameters, taking the values $0$, $1$, $2$, $4$; it is invertible exactly when both parameters are units, with $S_{\tilde Q,\tilde Q_2}^{-1}=S_{\tilde Q_2^{-1},\tilde Q^{-1}}$.

Two sandwiches compose to the linear two-sided multiplication $T_{\tilde Q_3\tilde Q_2,\tilde Q_8^{*}\tilde Q_9^{*}}$, a sandwich and a two-sided multiplication compose to a sandwich, and the two families together form a monoid with identity $T_{e_t,e_t}$; the sandwiches are its conjugate-linear half. A unitary parameter gives the reflection $S_{\tilde u,\tilde u^{*}}$ and the inner involution $S_{\tilde u,\tilde u}$. The sandwich is the operator form of the ternary product, the quadratic representation being the case of conjugate parameters, and it is the two-sided action of the algebra, whose linear shadow is the ordinary two-sided multiplication.

## Summary of Notation

| symbol | meaning |
|---|---|
| $S_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\star\tilde Q_1\star\tilde Q_2=\tilde Q\tilde Q_1^{*}\tilde Q_2^{*}$ | the sesquilinear sandwich, conjugate-linear |
| $T_{\tilde Q,\tilde Q_2}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_2$ | the ordinary two-sided multiplication, linear |
| $S_{\tilde Q,\tilde Q_2}=T_{\tilde Q,\tilde Q_2^{*}}\circ{}^{*}$ | the sandwich as the two-sided multiplication with the involution |
| $L_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}$, $R_{\tilde Q_2}(\tilde Q_1)=\tilde Q_1\tilde Q_2^{*}$ | the left and the right multiplication |
| $S_{\tilde Q,\tilde Q_2}=R_{\tilde Q_2}\circ L_{\tilde Q}$ | the sandwich as the mixed composite |
| $S_{\tilde Q_3,\tilde Q_9}S_{\tilde Q_8,\tilde Q_2}=T_{\tilde Q_3\tilde Q_2,\tilde Q_8^{*}\tilde Q_9^{*}}$ | the composite of two sandwiches |
| $S_{\tilde Q_8,\tilde Q_2}^{2}=T_{\tilde Q_8\tilde Q_2,\tilde Q_8^{*}\tilde Q_2^{*}}$ | the square of a sandwich |
| $S_{\tilde Q,\tilde Q_2}^{-1}=S_{\tilde Q_2^{-1},\tilde Q^{-1}}$ | the inverse on the units |
| $\operatorname{rank}S_{\tilde Q,\tilde Q_2}=\operatorname{rank}\tilde Q\cdot\operatorname{rank}\tilde Q_2$ | the rank of a sandwich |
| $S_{\tilde\Pi,\tilde\Pi}$ | the rank-one sandwich of a projection |
| $\{\tilde Q_8,\tilde Q_5,\tilde Q_2\}=\tilde Q_8\tilde Q_5^{*}\tilde Q_2$ | the ternary product |
| $\tilde Q_4\mapsto\tilde Q_4\tilde Q_5^{*}\tilde Q_4=S_{\tilde Q_4,\tilde Q_4^{*}}(\tilde Q_5)$ | the quadratic representation |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the triple products of a ring with involution and the operators they induce.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the sandwich operators of a ring with involution and the conjugate-linear maps attached to them.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the semilinear operators, the two-sided multiplications and the case of the trivial involution.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the triple product $xy^{*}z$ and the quadratic representation it defines.
- Ottmar Loos, *Jordan Pairs* (Springer Lecture Notes in Mathematics 460, 1975), for the triple product $xy^{*}z$, the quadratic representation and its operator forms.
