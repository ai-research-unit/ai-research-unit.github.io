
# __The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions__

## Introduction

The sesquilinear multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ is neither commutative nor anticommutative, so it splits into its symmetric and its antisymmetric part. Writing $2$ for the doubled unit and using the hypothesis that $2$ is invertible, the split is

$$
\tilde P\star\tilde Q=\tilde P\circ\tilde Q+\tfrac12\,[\tilde P,\tilde Q]_\varsigma , \qquad
\tilde P\circ\tilde Q=\tfrac12\bigl(\tilde P\star\tilde Q+\tilde Q\star\tilde P\bigr) , \qquad
[\tilde P,\tilde Q]_\varsigma=\tilde P\star\tilde Q-\tilde Q\star\tilde P ,
$$

the **symmetrised product** and the **sesquilinear commutator**, or **difference**. The two are the operatoral halves of the multiplication: the symmetric half is the polarisation of the square, and the antisymmetric half is what the squares do not see. Their images lie in the two halves of the involution of *Hermitian and Skew-Hermitian Elements* in the two possible ways: the symmetrised product takes Hermitian values on every pair, and the commutator takes skew-Hermitian values on every pair.

Neither half is an algebra in the naive sense over $\mathbb{C}$. The two operations are only $\mathbb{R}$-bilinear, because each slot receives one linear and one conjugate-linear contribution from the two scalar rules, and the surviving scalars are the fixed field $\mathbb{R}$; and the two classical identities fail off the Hermitian half. The sesquilinear commutator is a Lie bracket on the skew-Hermitian half alone, and the symmetrised product is a Jordan product on the Hermitian half alone: off those halves the Jacobi identity and the Jordan identity fail, with the witnesses below computed on $\mathbb{B}$.

The article is the eighth of the batch and reads the two general articles *The Sesquilinear Commutator* and *The Sesquilinear Symmetrised Product*, whose antisymmetry, scalar theorems, half-theorems and failure witnesses are quoted; the two bilinear operations that the sesquilinear ones are compared with are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the Lie and the Jordan structures of the sesqualgebra are *Lie Algebras of Sesqualgebras* and *Jordan Algebras of Sesqualgebras*. The ternary product that repairs the associativity is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*, and the operator forms of the two halves are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

The setting is that of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The scalar and vector parts are $\tilde Q=Q_0e_0+\mathbf Q$, and the Hermitian form is $\langle\tilde P,\tilde Q\rangle_*=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *The Hermitian Form on the Biquaternion Algebra*.

## The Split of the Multiplication

### The Two Halves

**Proposition (the split).** For all $\tilde P,\tilde Q$,

$$
\tilde P\star\tilde Q=\tilde P\circ\tilde Q+\tfrac12\,[\tilde P,\tilde Q]_\varsigma ,
$$

the symmetrised part being invariant and the bracket part changing sign under the exchange of the two arguments:

$$
\tilde Q\circ\tilde P=\tilde P\circ\tilde Q , \qquad [\tilde Q,\tilde P]_\varsigma=-[\tilde P,\tilde Q]_\varsigma .
$$

**Proof.** This is the split of *The Sesquilinear Symmetrised Product*, §*The Definition*, and of *The Sesquilinear Commutator*, §*The Values in the Skew-Hermitian Part*: adding and subtracting $\tfrac12(\tilde Q\star\tilde P)$ in the product gives the display, the symmetrised part is unchanged by the exchange by its definition, and the bracket changes sign by the antisymmetry of the subtraction. $\square$

**Remark.** The split is the decomposition of the multiplication into its two eigenspaces for the exchange of the arguments; it uses only the additivity and the invertibility of $2$, and not the associativity of the underlying product. On the diagonal the bracket vanishes and the symmetrised product is the square, $\tilde P\circ\tilde P=\tilde P\star\tilde P=\tilde P\tilde P^{*}$; off the diagonal the square does not see the bracket, which is the content of the polarisation.

### The Scalars

**Theorem (the scalars).** For $\lambda\in\mathbb{C}$ and all $\tilde P,\tilde Q$,

$$
(\lambda\tilde P)\circ\tilde Q=\lambda(\tilde P\circ\tilde Q)+\tfrac12\bigl(\overline{\lambda}-\lambda\bigr)\bigl(\tilde Q\star\tilde P\bigr) ,
$$

and the same display with the two slots exchanged; the operations are therefore $\mathbb{R}$-bilinear and no more, $\mathbb{R}$ being the fixed field of the conjugation.

**Proof.** This is the scalar theorem of *The Sesquilinear Symmetrised Product*, §*The Scalar Rules*, and of *The Sesquilinear Commutator*, §*The Scalars and the Correction Term*, with $\varsigma$ the complex conjugation and the fixed ring $\mathbb{R}$; the correction carries the transposed product $\tilde Q\star\tilde P$ because the scalar sits in the second slot of the transposed factor. $\square$

**Remark.** The correction term vanishes exactly on the real scalars, and it is the whole content of the semilinearity of the two operations: a genuinely sesquilinear product gives a bracket and a symmetrisation over $\mathbb{R}$ and not over $\mathbb{C}$. For the bilinear product $\tilde P\tilde Q$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* the correction is absent and the two operations are $\mathbb{C}$-bilinear, which is the first of the two differences between the two readings.

### The Other Exchange, and the Two Sesquilinear Halves

The split above is taken under the **plain** exchange of the two arguments, and the correction term is what the plain exchange costs. The exchange by a conjugation $c$, $f^{c}(\tilde P,\tilde Q)=c(f(\tilde Q,\tilde P))$, keeps the class of the two sesquilinear products, and its two halves $f^{c}_{\pm}=\tfrac12(f\pm f^{c})$ are sesquilinear over $\mathbb{C}$; the construction is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*.

With $c=\overline{\cdot}$ the four halves on the two products of this article are these: for $\tilde P\tilde Q^{*}$,

$$
\tfrac12\bigl(\tilde P\tilde Q^{*}+(\tilde P\tilde Q^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde P\tilde Q^{*})=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}}),\qquad
\tfrac12\bigl(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde P\tilde Q^{*}),
$$

the scalar part, central, and the vector part of the value; and for $\tilde P^{\natural}\tilde Q^{*}$, since $\overline{\tilde Q^{\natural}}=\tilde Q^{*}$,

$$
\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr),\qquad
\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr),
$$

the symmetrisation of $\tilde P^{\natural}$ with $\tilde Q^{*}$ and half their commutator in the plain product. So each sesquilinear product carries **two** pairs of halves, one under each exchange, and the pair above is the one that stays in the class: the symmetrised product and the sesquilinear commutator of this article are the plain pair, and the scalar and the vector part of the value are the adapted pair of the first product.

## The Sesquilinear Commutator

### Definition and Antisymmetry

**Definition.** The **sesquilinear commutator** of $\tilde P,\tilde Q$ is

$$
[\tilde P,\tilde Q]_\varsigma=\tilde P\star\tilde Q-\tilde Q\star\tilde P=\tilde P\tilde Q^{*}-\tilde Q\tilde P^{*} .
$$

**Proposition (antisymmetry).** $[\tilde Q,\tilde P]_\varsigma=-[\tilde P,\tilde Q]_\varsigma$ and $[\tilde P,\tilde P]_\varsigma=0$ for every $\tilde P$.

**Proof.** The antisymmetry of the subtraction applied to the two terms, as in *The Sesquilinear Commutator*, §*Definition and Antisymmetry*; it uses neither the involution nor the associativity. $\square$

**Remark.** Antisymmetry is the one property the bracket has without a hypothesis, and it is free. The Jacobi identity is not free, and the identity must fail, since the bracket is not $\mathbb{C}$-bilinear and there is no associativity to inherit; the failure is computed below.

### The Values in the Skew-Hermitian Half

**Proposition (the values).** For all $\tilde P,\tilde Q$ the bracket is skew-Hermitian,

$$
[\tilde P,\tilde Q]_\varsigma^{*}=-[\tilde P,\tilde Q]_\varsigma ,
$$

so the bracket is a map $\mathbb{B}\times\mathbb{B}\to\mathbb{M}_-$ into the anti-Hermitian half.

**Proof.** The conjugate of a product reverses it, $(\tilde P\star\tilde Q)^{*}=\tilde Q\star\tilde P$, by the anti-multiplicativity of the involution; hence $[\tilde P,\tilde Q]_\varsigma^{*}=[\tilde Q,\tilde P]_\varsigma=-[\tilde P,\tilde Q]_\varsigma$, which is the proposition of *The Sesquilinear Commutator*, §*The Values in the Skew-Hermitian Part*. $\square$

**Remark.** The image of the bracket therefore never meets the Hermitian half unless it vanishes, and this is a sharp difference from the ordinary commutator, which moves between the two halves according to the parities of its arguments: the commutator of two Hermitian elements is skew-Hermitian, of two skew-Hermitian elements is skew-Hermitian with the opposite sign, and of a Hermitian and a skew-Hermitian element is Hermitian. The sesquilinear bracket has only the first of these behaviours, and it has it on every pair.

### The Two Halves

**Theorem (the bracket on the two halves).** For $\tilde h,\tilde h'\in\mathbb{M}_+$ and $\tilde s,\tilde s'\in\mathbb{M}_-$,

$$
[\tilde h,\tilde h']_\varsigma=[\tilde h,\tilde h'] , \qquad [\tilde s,\tilde s']_\varsigma=-[\tilde s,\tilde s'] , \qquad [\tilde s,\tilde h]_\varsigma=\tilde s\tilde h+\tilde h\tilde s ,
$$

where the brackets on the right are the ordinary commutator of the algebra.

**Proof.** For Hermitian $\tilde h$ the derived operation is the algebra product in both slots, $\tilde h\star\tilde h'=\tilde h\tilde h'$, so the bracket is the ordinary commutator; for skew-Hermitian $\tilde s$ the involution contributes a sign, $\tilde s^{*}=-\tilde s$, so $[\tilde s,\tilde s']_\varsigma=-(\tilde s\tilde s'-\tilde s'\tilde s)$; and for the mixed pair $[\tilde s,\tilde h]_\varsigma=\tilde s\tilde h^{*}-\tilde h\tilde s^{*}=\tilde s\tilde h+\tilde h\tilde s$. This is the theorem of *The Sesquilinear Commutator*, §*The Two Halves*. $\square$

**Corollary (the Lie algebra of the skew-Hermitian half).** On the skew-Hermitian half the sesquilinear bracket is $\mathbb{R}$-bilinear, antisymmetric and satisfies the Jacobi identity, being the negative of the commutator of the associative envelope; the sesquilinear bracket and the ordinary commutator make $\mathbb{M}_-$ one and the same Lie algebra over $\mathbb{R}$, up to the sign of the bracket. That Lie algebra is the unitary Lie algebra of *The Unitary Group of the Biquaternion Algebra* and *Lie Algebras of Sesqualgebras*.

**Proof.** The theorem gives $[\tilde s,\tilde s']_\varsigma=-[\tilde s,\tilde s']$ on $\mathbb{M}_-$, and the commutator of an associative algebra is a Lie bracket; the sign carries through the three terms of the Jacobi identity. $\square$

### The Failure of the Jacobi Identity

**Theorem.** The Jacobi identity for the sesquilinear bracket fails on $\mathbb{B}$. With the three Hermitian elements

$$
\tilde P=\tfrac12(e_0+ie_3)=\tilde\Pi_+(\hat e_3) , \qquad \tilde Q=\tfrac12(e_0-ie_3)=\tilde\Pi_+(-\hat e_3) , \qquad \tilde H=ie_1 ,
$$

the Jacobi sum is

$$
[[\tilde P,\tilde Q]_\varsigma,\tilde H]_\varsigma+[[\tilde Q,\tilde H]_\varsigma,\tilde P]_\varsigma+[[\tilde H,\tilde P]_\varsigma,\tilde Q]_\varsigma=2e_2\neq0 .
$$

**Proof.** The three elements are Hermitian: the two projections by *Projections of the Biquaternion Sesqualgebra*, and $\tilde H=ie_1$ because $e_1^{*}=-e_1$. The inner brackets are ordinary commutators by the half-theorem. The first vanishes, $[\tilde P,\tilde Q]_\varsigma=\tilde P\tilde Q-\tilde Q\tilde P=0$, because $\tilde P\tilde Q=\tfrac14(e_0+ie_3)(e_0-ie_3)=\tfrac14(e_0-e_0)=0$ and likewise in the other order. The other two are

$$
[\tilde Q,\tilde H]_\varsigma=\tilde Q\tilde H-\tilde H\tilde Q=\tfrac12\bigl(e_2+ie_1\bigr)-\tfrac12\bigl(ie_1-e_2\bigr)=e_2 , \qquad
[\tilde H,\tilde P]_\varsigma=\tilde H\tilde P-\tilde P\tilde H=\tfrac12\bigl(e_2+ie_1\bigr)-\tfrac12\bigl(ie_1-e_2\bigr)=e_2 ,
$$

where the basis products of *Biquaternions as a General Plain Sesqualgebra (GPS) over $\mathbb{C}$* give the two expansions. Both inner values are the skew-Hermitian $e_2$, and the outer brackets read a skew-Hermitian element with a Hermitian one by the mixed rule $[\tilde s,\tilde h]_\varsigma=\tilde s\tilde h+\tilde h\tilde s$:

$$
[e_2,\tilde P]_\varsigma=e_2\tilde P+\tilde Pe_2=\tfrac12\bigl(e_2+ie_1\bigr)+\tfrac12\bigl(e_2-ie_1\bigr)=e_2 , \qquad
[e_2,\tilde Q]_\varsigma=e_2\tilde Q+\tilde Qe_2=\tfrac12\bigl(e_2-ie_1\bigr)+\tfrac12\bigl(e_2+ie_1\bigr)=e_2 .
$$

The Jacobi sum is therefore $0+e_2+e_2=2e_2\neq0$. The same computation in the matrix model is the witness of *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity*, with $E_{11},E_{22},E_{12}+E_{21}$ and the value $2(E_{21}-E_{12})$, transported to $\mathbb{B}$ along the model of *Biquaternion $2\times2$ Matrix Element Representation*, whose inverse carries $E_{21}-E_{12}$ to $e_2$. $\square$

**Remark.** Three Hermitian elements suffice, which is the sharp form of the failure: the outer brackets meet skew-Hermitian values, and there they obey the symmetrised rule rather than the commutator rule, so the reassociation that the Jacobi identity performs is performed with a different operation. The failure is produced by the noncommutativity of $\mathbb{B}$ and not by the semilinearity of the multiplication: on the sesquilinear field $\mathbb{C}$ over $(\mathbb{C},\varsigma)$ the bracket $[x,y]_\varsigma=x\overline{y}-y\overline{x}$ is a Lie bracket over $\mathbb{R}$, by *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity*.

### The Bracket and the Involution

**Proposition.** For all $\tilde X,\tilde Y$,

$$
[\tilde X,e_0]_\varsigma=\tilde X-\tilde X^{*} , \qquad [\tilde X,\tilde Y]_\varsigma=0\text{ for all }\tilde X,\tilde Y \iff {}^{*}=\mathrm{id}\text{ and }\mathbb{B}\text{ is commutative} ,
$$

and the bracket does not commute with the involution: $[\tilde X,\tilde Y]_\varsigma^{*}=[\tilde Y,\tilde X]_\varsigma$, which differs from $[\tilde X^{*},\tilde Y^{*}]_\varsigma$ in general.

**Proof.** The first display is the proposition of *The Sesquilinear Commutator*, §*The Vanishing and the Involution*, read on $\mathbb{B}$; its vanishing for all $\tilde X$ is the criterion that the involution is trivial, which it is not here. For the last statement, the witness of that article in the matrix model is $\tilde X=\tfrac12(ie_1-e_2)$ and $\tilde Y=\tfrac12(e_0+ie_3)$: the bracket vanishes, while the bracket of the conjugates is $e_2$. $\square$

**Remark.** The bracket therefore detects the involution on the diagonal, $[\tilde X,e_0]_\varsigma=\tilde X-\tilde X^{*}$, and its vanishing is exactly the Hermitian condition; the bracket measures the asymmetry between the two slots that the involution produces, and it vanishes on the fixed field and on nothing else.

## The Symmetrised Product

### Definition and the Polarisation of the Square

**Definition.** The **symmetrised sesquilinear product** is

$$
\tilde P\circ\tilde Q=\tfrac12\bigl(\tilde P\star\tilde Q+\tilde Q\star\tilde P\bigr) , \qquad\text{equivalently}\qquad \tilde P\circ\tilde Q=\tilde P\star\tilde Q-\tfrac12[\tilde P,\tilde Q]_\varsigma .
$$

**Proposition (the polarisation).** For all $\tilde P,\tilde Q$,

$$
\tilde P\circ\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)\star(\tilde P+\tilde Q)-\tilde P\star\tilde P-\tilde Q\star\tilde Q\bigr) \quad\text{or, with the complex scalars,}\quad \tilde P\circ\tilde Q=\tfrac14\bigl((\tilde P+\tilde Q)\star(\tilde P+\tilde Q)-(\tilde P-\tilde Q)\star(\tilde P-\tilde Q)\bigr) ,
$$

so the squares determine the symmetrised product.

**Proof.** This is the polarisation of *The Sesquilinear Symmetrised Product*, §*The Polarisation of the Square*, using the additivity of the multiplication in each variable; the two forms differ by the coefficient that the expansion requires, and each is the standard polarisation of a quadratic map. $\square$

**Remark.** The square $\tilde P\mapsto\tilde P\star\tilde P=\tilde P\tilde P^{*}$ therefore determines the symmetric half, and the antisymmetric half is exactly what the square cannot see: the bracket takes opposite values on the two products and cancels in every square. On the diagonal the symmetrised product is the square of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and the polarisation is the reason the square theory and the symmetrised product are the same subject off the diagonal.

### The Hermitian Value

**Theorem.** For all $\tilde P,\tilde Q$ the symmetrised product is Hermitian,

$$
(\tilde P\circ\tilde Q)^{*}=\tilde P\circ\tilde Q ,
$$

so the symmetrised product is a map $\mathbb{B}\times\mathbb{B}\to\mathbb{M}_+$ into the Hermitian half; its scalar part is the real part of the Hermitian form,

$$
\mathrm{Sc}(\tilde P\circ\tilde Q)=\mathrm{Re}\sum_\mu P_\mu\overline{Q_\mu}=\mathrm{Re}\,\langle\tilde P,\tilde Q\rangle_* .
$$

**Proof.** $(\tilde P\star\tilde Q)^{*}=\tilde Q\star\tilde P$, so $(\tilde P\circ\tilde Q)^{*}=\tfrac12(\tilde Q\star\tilde P+\tilde P\star\tilde Q)=\tilde P\circ\tilde Q$; for the scalar part, $\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_\mu P_\mu\overline{Q_\mu}$ and $\mathrm{Sc}(\tilde Q\star\tilde P)=\overline{\sum_\mu P_\mu\overline{Q_\mu}}$, and the half-sum is the real part. This is the theorem of *The Sesquilinear Symmetrised Product*, §*The Hermitian Value*. $\square$

**Remark.** The image of the symmetrised product is therefore contained in the Hermitian half whatever the two arguments, and the scalar part is real and equal to the real part of the Hermitian form. The plain symmetrisation $\tilde P\tilde Q+\tilde Q\tilde P$ of the algebra product has no such property: its value is Hermitian only when the two arguments lie in the right halves, and the comparison of the two is the next section.

### The Hermitian Half

**Theorem (the symmetrisation on the Hermitian half).** For $\tilde h,\tilde h'\in\mathbb{M}_+$,

$$
\tilde h\circ\tilde h'=\tfrac12\bigl(\tilde h\tilde h'+\tilde h'\tilde h\bigr) ,
$$

the plain symmetrisation, and with this product $\mathbb{M}_+$ is a commutative Jordan algebra over $\mathbb{R}$, with the Jordan identity

$$
(\tilde h\circ\tilde h')\circ(\tilde h\circ\tilde h)=\tilde h\circ\bigl(\tilde h'\circ(\tilde h\circ\tilde h)\bigr) .
$$

**Proof.** For Hermitian $\tilde h$ the derived operation is the algebra product, $\tilde h\star\tilde h'=\tilde h\tilde h'$ and $\tilde h'\star\tilde h=\tilde h'\tilde h$; the two symmetrisations therefore agree on the half, and the symmetrisation of an associative product satisfies the Jordan identity, by *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*. This is the theorem of *The Sesquilinear Symmetrised Product*, §*On the Hermitian Part*. $\square$

**Remark.** The Jordan algebra is the Hermitian Jordan algebra of *The Hermitian Jordan Algebra* and of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and it is the positive cone theory of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*. The sesquilinear symmetrisation is therefore a Jordan product exactly on the Hermitian half, and there it is the same product as the one the algebra symmetrisation of the same article carries on that half.

### The Failure of the Jordan Identity

**Proposition (the identity fails off the Hermitian half).** On $\mathbb{B}$ there are elements with

$$
(\tilde X\circ\tilde Y)\circ(\tilde X\circ\tilde X)\neq\tilde X\circ\bigl(\tilde Y\circ(\tilde X\circ\tilde X)\bigr) .
$$

With

$$
\tilde X=\tfrac12(ie_1-e_2) , \qquad \tilde Y=\tfrac12(e_0-ie_3)=\tilde\Pi_+(-\hat e_3) ,
$$

the two sides are

$$
(\tilde X\circ\tilde Y)\circ(\tilde X\circ\tilde X)=\tfrac{i}{4}e_1 , \qquad \tilde X\circ\bigl(\tilde Y\circ(\tilde X\circ\tilde X)\bigr)=0 ,
$$

and the first is not zero.

**Proof.** The computation is the one of *The Sesquilinear Symmetrised Product*, §*Off the Hermitian Part*, transported to $\mathbb{B}$ along the model of *Biquaternion $2\times2$ Matrix Element Representation*: the element $\tilde X$ is the image of the matrix unit $E_{12}$ and the element $\tilde Y$ the image of $E_{22}$, whose symmetrised products are

$$
\tilde X\circ\tilde X=\tilde X\tilde X^{*}=\tfrac12(e_0+ie_3) , \qquad \tilde X\circ\tilde Y=\tfrac{i}{2}e_1 , \qquad \tilde Y\circ(\tilde X\circ\tilde X)=0 ,
$$

the last because $\tilde Y\tilde X\tilde X^{*}=0$; the two sides of the identity are then $\tfrac{i}{4}e_1$ and $0$, as the transport of $\tfrac14(E_{12}+E_{21})$ and $0$ along the inverse of the model. $\square$

**Remark.** One of the two elements is Hermitian, $\tilde Y$, and one is not, $\tilde X$; a single element off the Hermitian half is enough to break the identity, and the perturbation is exactly the failure of $\tilde X$ to be Hermitian. The value $\tilde X\circ\tilde X=\tilde X\tilde X^{*}=\tfrac12(e_0+ie_3)$ is Hermitian, as the Hermitian-value theorem promises, but the symmetry of the derived product with one slot off the half is the wrong one to carry the identity. The failure is the reason the Jordan structure of the sesqualgebra lives on the Hermitian half alone, and it is *Jordan Algebras of Sesqualgebras*, §*The Hermitian Part*, that locates it there.

## The Biquaternion Reading

### The Two Operations on the Basis

**Proposition (the symmetrised basis).** On the real basis $e_0,e_1,e_2,e_3$,

$$
e_\mu\circ e_\nu=\delta_{\mu\nu}\,e_0 ,
$$

so for elements with real coordinates the symmetrised product is $e_0$ times the Euclidean dot product of the coordinate vectors.

**Proof.** $e_\mu\circ e_\mu=e_\mu\star e_\mu=\varepsilon_\mu e_\mu^{2}$: for $\mu=0$ this is $e_0$, and for $\mu=k$ it is $(-1)(-e_0)=e_0$. For $\mu\neq\nu$ the two terms of the symmetrisation are $\varepsilon_\nu e_\mu e_\nu$ and $\varepsilon_\mu e_\nu e_\mu$, and the basis products anticommute, $e_\mu e_\nu=-e_\nu e_\mu$, with $\varepsilon_\mu=\varepsilon_\nu$ unless one of the indices is $0$; in every case the two terms cancel. $\square$

**Proposition (the commutator basis).** On the real basis,

$$
[e_0,e_k]_\varsigma=-2e_k , \qquad [e_j,e_k]_\varsigma=-2\,e_j\times e_k ,
$$

the second for the vector indices, so on the vector part the bracket is $-2$ times the cross product of the vector parts.

**Proof.** $[e_0,e_k]_\varsigma=e_0e_k^{*}-e_ke_0^{*}=-e_k-e_k=-2e_k$, using $e_k^{*}=-e_k$; for the vector indices, $[e_j,e_k]_\varsigma=e_je_k^{*}-e_ke_j^{*}=-e_je_k+e_ke_j=-2e_je_k=-2\,e_j\times e_k$ for distinct $j,k$, and it vanishes for $j=k$. $\square$

**Remark.** The two tables are the extreme cases of the split: the symmetrised product of two distinct basis elements vanishes and the diagonal values are all $e_0$, so the symmetric half of the multiplication is the pairing that makes of the basis an orthogonal set with the constant square $e_0$; the bracket of two distinct basis elements is $-2$ times their cross product, so the antisymmetric half is the cross product of the vector part read with the coefficient $-2$, which is the negative of the ordinary commutator on the vector elements. The scalar part of the symmetrised product is $\mathrm{Re}\,\langle\tilde P,\tilde Q\rangle_*$, and the scalar part of the bracket is $2i\,\mathrm{Im}\,\langle\tilde P,\tilde Q\rangle_*$.

### The Comparison with the Two Bilinear Operations

The bilinear commutator $\tilde P\tilde Q-\tilde Q\tilde P$ and the bilinear symmetrisation $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are $\mathbb{C}$-bilinear and satisfy their identities on the whole algebra. The sesquilinear operations agree with them on the Hermitian half and fail off it.

| operation | bilinear or sesquilinear | Jacobi identity | Jordan identity |
|---|---|---|---|
| $\tilde P\tilde Q-\tilde Q\tilde P$ | bilinear | holds on $\mathbb{B}$ | not asked |
| $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | bilinear | not asked | holds on $\mathbb{B}$ |
| $[\tilde P,\tilde Q]_\varsigma$ | sesquilinear | fails; holds on $\mathbb{M}_-$ | not asked |
| $\tilde P\circ\tilde Q$ | sesquilinear | not asked | holds on $\mathbb{M}_+$, fails off it |

**Remark.** The table is the biquaternion form of the general dichotomy: the bilinear operations are $\mathbb{C}$-bilinear and carry their identities everywhere, the sesquilinear operations are $\mathbb{R}$-bilinear, and their identities survive exactly on the half where the derived operation coincides with the algebra product. On the Hermitian half the four rows collapse to two, the sesquilinear operations agreeing with the bilinear ones there; the failure of the Jordan identity of §*The Failure of the Jordan Identity* uses the element $\tilde X$ off the half, and the failure of the Jacobi identity of §*The Failure of the Jacobi Identity* uses the symmetrised rule that the outer brackets obey on the skew-Hermitian values.

## Summary

The sesquilinear multiplication splits as $\tilde P\star\tilde Q=\tilde P\circ\tilde Q+\tfrac12[\tilde P,\tilde Q]_\varsigma$ into the symmetrised product and the sesquilinear commutator, both $\mathbb{R}$-bilinear and no more, $\mathbb{R}$ being the fixed field of the conjugation. The commutator is antisymmetric, takes its values in the skew-Hermitian half, and is the negative of the ordinary commutator on that half, so the skew-Hermitian half is a Lie algebra over $\mathbb{R}$, the unitary Lie algebra; its Jacobi identity fails on the whole algebra, with the three-Hermitian-element witness $\tilde\Pi_+(\hat e_3),\tilde\Pi_+(-\hat e_3),ie_1$ giving $2e_2$, because the outer brackets obey the symmetrised rule on the skew-Hermitian values.

The symmetrised product is the polarisation of the square, takes its values in the Hermitian half, has scalar part the real part of the Hermitian form, and agrees with the plain symmetrisation on the Hermitian half, where it is a Jordan algebra; off the half the Jordan identity fails, with the witness $\tilde X=\tfrac12(ie_1-e_2)$, $\tilde Y=\tfrac12(e_0-ie_3)$ giving $\tfrac{i}{4}e_1$ against $0$. On the basis the symmetrised product is $\delta_{\mu\nu}e_0$ and the commutator of two vector basis elements is $-2$ times their cross product. The two bilinear operations of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* are the $\mathbb{C}$-bilinear case, with their identities everywhere; the sesquilinear operations carry them on the two halves alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\circ\tilde Q=\tfrac12(\tilde P\star\tilde Q+\tilde Q\star\tilde P)$ | the symmetrised sesquilinear product, Hermitian-valued |
| $[\tilde P,\tilde Q]_\varsigma=\tilde P\star\tilde Q-\tilde Q\star\tilde P$ | the sesquilinear commutator, skew-Hermitian-valued |
| $\tilde P\star\tilde Q=\tilde P\circ\tilde Q+\tfrac12[\tilde P,\tilde Q]_\varsigma$ | the split of the multiplication |
| $\tilde P\circ\tilde P=\tilde P\star\tilde P=\tilde P\tilde P^{*}$ | the diagonal is the square |
| $\mathbb{R}=\mathbb{C}^{\varsigma}$ | the fixed field, the ring of scalars of the two operations |
| $[\tilde h,\tilde h']_\varsigma=[\tilde h,\tilde h']$ | the bracket on the Hermitian half |
| $[\tilde s,\tilde s']_\varsigma=-[\tilde s,\tilde s']$ | the bracket on the skew-Hermitian half, the unitary Lie algebra |
| $(\tilde h\circ\tilde h')\circ(\tilde h\circ\tilde h)=\tilde h\circ(\tilde h'\circ(\tilde h\circ\tilde h))$ | the Jordan identity, on $\mathbb{M}_+$ |
| $\tilde\Pi_+(\hat e_3),\tilde\Pi_+(-\hat e_3),ie_1$ | the Hermitian triple whose Jacobi sum is $2e_2$ |
| $\tfrac12(ie_1-e_2),\tfrac12(e_0-ie_3)$ | the pair whose Jordan identity fails, $\tfrac{i}{4}e_1$ against $0$ |
| $e_\mu\circ e_\nu=\delta_{\mu\nu}e_0$ | the symmetrised product on the basis |
| $[e_j,e_k]_\varsigma=-2\,e_j\times e_k$ | the commutator on the vector basis |
| $\mathrm{Sc}(\tilde P\circ\tilde Q)=\mathrm{Re}\langle\tilde P,\tilde Q\rangle_*$ | the scalar part of the symmetrised product |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the Jacobi identity, the Lie algebras of an associative algebra and the unitary Lie algebra.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the Jordan identity, the symmetrisation of an associative algebra and the Lie-admissible and Jordan-admissible algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan product, its powers and the Jordan identity.
- K. A. Zhevlakov, A. M. Slin'ko, I. P. Shestakov and A. I. Shirshov, *Rings That Are Nearly Associative* (Academic Press, 1982), for the identities of the Lie and the Jordan symmetrisations of a non-associative algebra.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the skew-symmetric elements, the commutator of an involutive ring and the Lie structure it carries.
