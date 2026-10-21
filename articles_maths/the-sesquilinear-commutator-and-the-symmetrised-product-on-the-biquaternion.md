
# __The Sesquilinear Commutator and the Symmetrised Product on the Biquaternion__

## Introduction

The sesquilinear multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ is neither commutative nor anticommutative, so it splits into its symmetric and its antisymmetric part. Writing $2$ for the doubled unit and using the hypothesis that $2$ is invertible, the split is

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1\circ\tilde Q_2+\tfrac12\,[\tilde Q_1,\tilde Q_2]_\varsigma , \qquad
\tilde Q_1\circ\tilde Q_2=\tfrac12\bigl(\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1\bigr) , \qquad
[\tilde Q_1,\tilde Q_2]_\varsigma=\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1 ,
$$

the **symmetrised product** and the **sesquilinear commutator**, or **difference**. The two are the operatoral halves of the multiplication: the symmetric half is the polarisation of the square, and the antisymmetric half is what the squares do not see. Their images lie in the two halves of the involution of *Hermitian and Skew-Hermitian Elements* in the two possible ways: the symmetrised product takes Hermitian values on every pair, and the commutator takes skew-Hermitian values on every pair.

Neither half is an algebra in the naive sense over $\mathbb{C}$. The two operations are only $\mathbb{R}$-bilinear, because each slot receives one linear and one conjugate-linear contribution from the two scalar rules, and the surviving scalars are the fixed field $\mathbb{R}$; and the two classical identities fail off the Hermitian half. The sesquilinear commutator is a Lie bracket on the skew-Hermitian half alone, and the symmetrised product is a Jordan product on the Hermitian half alone: off those halves the Jacobi identity and the Jordan identity fail, with the witnesses below computed on $\mathbb{B}$.

The article is the eighth of the batch and reads the two general articles *The Sesquilinear Commutator* and *The Sesquilinear Symmetrised Product*, whose antisymmetry, scalar theorems, half-theorems and failure witnesses are quoted; the two bilinear operations that the sesquilinear ones are compared with are *The 12 Products of the Biquaternion Complex Space*, and the Lie and the Jordan structures of the sesqualgebra are *Lie Algebras of Sesqualgebras* and *Jordan Algebras of Sesqualgebras*. The ternary product that repairs the associativity is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*, and the operator forms of the two halves are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

The setting is that of *Introduction to the General Plain Sesqualgebra*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$. The scalar and vector parts are $\tilde Q=Q_te_t+\vec Q$, and the Hermitian form is $\langle\tilde Q_1,\tilde Q_2\rangle_*=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

## The Split of the Multiplication

### The Two Halves

**Proposition (the split).** For all $\tilde Q_1,\tilde Q_2$,

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1\circ\tilde Q_2+\tfrac12\,[\tilde Q_1,\tilde Q_2]_\varsigma ,
$$

the symmetrised part being invariant and the bracket part changing sign under the exchange of the two arguments:

$$
\tilde Q_2\circ\tilde Q_1=\tilde Q_1\circ\tilde Q_2 , \qquad [\tilde Q_2,\tilde Q_1]_\varsigma=-[\tilde Q_1,\tilde Q_2]_\varsigma .
$$

**Proof.** This is the split of *The Sesquilinear Symmetrised Product*, §*The Definition*, and of *The Sesquilinear Commutator*, §*The Values in the Skew-Hermitian Part*: adding and subtracting $\tfrac12(\tilde Q_2\star\tilde Q_1)$ in the product gives the display, the symmetrised part is unchanged by the exchange by its definition, and the bracket changes sign by the antisymmetry of the subtraction.

**Remark.** The split is the decomposition of the multiplication into its two eigenspaces for the exchange of the arguments; it uses only the additivity and the invertibility of $2$, and not the associativity of the underlying product. On the diagonal the bracket vanishes and the symmetrised product is the square, $\tilde Q_1\circ\tilde Q_1=\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$; off the diagonal the square does not see the bracket, which is the content of the polarisation.

### The Scalars

**Theorem (the scalars).** For $\lambda\in\mathbb{C}$ and all $\tilde Q_1,\tilde Q_2$,

$$
(\lambda\tilde Q_1)\circ\tilde Q_2=\lambda(\tilde Q_1\circ\tilde Q_2)+\tfrac12\bigl(\overline{\lambda}-\lambda\bigr)\bigl(\tilde Q_2\star\tilde Q_1\bigr) ,
$$

and the same display with the two slots exchanged; the operations are therefore $\mathbb{R}$-bilinear and no more, $\mathbb{R}$ being the fixed field of the conjugation.

**Proof.** This is the scalar theorem of *The Sesquilinear Symmetrised Product*, §*The Scalar Rules*, and of *The Sesquilinear Commutator*, §*The Scalars and the Correction Term*, with $\varsigma$ the complex conjugation and the fixed ring $\mathbb{R}$; the correction carries the transposed product $\tilde Q_2\star\tilde Q_1$ because the scalar sits in the second slot of the transposed factor.

**Remark.** The correction term vanishes exactly on the real scalars, and it is the whole content of the semilinearity of the two operations: a genuinely sesquilinear product gives a bracket and a symmetrisation over $\mathbb{R}$ and not over $\mathbb{C}$. For the bilinear product $\tilde Q_1\tilde Q_2$ of *The 12 Products of the Biquaternion Complex Space* the correction is absent and the two operations are $\mathbb{C}$-bilinear, which is the first of the two differences between the two readings.

### The Other Exchange, and the Two Sesquilinear Halves

The split above is taken under the **plain** exchange of the two arguments, and the correction term is what the plain exchange costs. The exchange by a conjugation $c$, $f^{c}(\tilde Q_1,\tilde Q_2)=c(f(\tilde Q_2,\tilde Q_1))$, keeps the class of the two sesquilinear products, and its two halves $f^{c}_{\pm}=\tfrac12(f\pm f^{c})$ are sesquilinear over $\mathbb{C}$; the construction is *The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*.

With $c=\overline{\cdot}$ the four halves on the two products of this article are these: for $\tilde Q_1\tilde Q_2^{*}$,

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}+(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2}),\qquad
\tfrac12\bigl(\tilde Q_1\tilde Q_2^{*}-(\tilde Q_1\tilde Q_2^{*})^{\natural}\bigr)=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*}),
$$

the scalar part, central, and the vector part of the value; and for $\tilde Q_1^{\natural}\tilde Q_2^{*}$, since $\overline{\tilde Q_2^{\natural}}=\tilde Q_2^{*}$,

$$
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr),\qquad
\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}-\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr),
$$

the symmetrisation of $\tilde Q_1^{\natural}$ with $\tilde Q_2^{*}$ and half their commutator in the plain product. So each sesquilinear product carries **two** pairs of halves, one under each exchange, and the pair above is the one that stays in the class: the symmetrised product and the sesquilinear commutator of this article are the plain pair, and the scalar and the vector part of the value are the adapted pair of the first product.

## The Sesquilinear Commutator

### Definition and Antisymmetry

**Definition.** The **sesquilinear commutator** of $\tilde Q_1,\tilde Q_2$ is

$$
[\tilde Q_1,\tilde Q_2]_\varsigma=\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1=\tilde Q_1\tilde Q_2^{*}-\tilde Q_2\tilde Q_1^{*} .
$$

**Proposition (antisymmetry).** $[\tilde Q_2,\tilde Q_1]_\varsigma=-[\tilde Q_1,\tilde Q_2]_\varsigma$ and $[\tilde Q_1,\tilde Q_1]_\varsigma=0$ for every $\tilde Q_1$.

**Proof.** The antisymmetry of the subtraction applied to the two terms, as in *The Sesquilinear Commutator*, §*Definition and Antisymmetry*; it uses neither the involution nor the associativity.

**Remark.** Antisymmetry is the one property the bracket has without a hypothesis, and it is free. The Jacobi identity is not free, and the identity must fail, since the bracket is not $\mathbb{C}$-bilinear and there is no associativity to inherit; the failure is computed below.

### The Values in the Skew-Hermitian Half

**Proposition (the values).** For all $\tilde Q_1,\tilde Q_2$ the bracket is skew-Hermitian,

$$
[\tilde Q_1,\tilde Q_2]_\varsigma^{*}=-[\tilde Q_1,\tilde Q_2]_\varsigma ,
$$

so the bracket is a map $\mathbb{B}\times\mathbb{B}\to\mathbb{M}_-$ into the anti-Hermitian half.

**Proof.** The conjugate of a product reverses it, $(\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_2\star\tilde Q_1$, by the anti-multiplicativity of the involution; hence $[\tilde Q_1,\tilde Q_2]_\varsigma^{*}=[\tilde Q_2,\tilde Q_1]_\varsigma=-[\tilde Q_1,\tilde Q_2]_\varsigma$, which is the proposition of *The Sesquilinear Commutator*, §*The Values in the Skew-Hermitian Part*.

**Remark.** The image of the bracket therefore never meets the Hermitian half unless it vanishes, and this is a sharp difference from the ordinary commutator, which moves between the two halves according to the parities of its arguments: the commutator of two Hermitian elements is skew-Hermitian, of two skew-Hermitian elements is skew-Hermitian with the opposite sign, and of a Hermitian and a skew-Hermitian element is Hermitian. The sesquilinear bracket has only the first of these behaviours, and it has it on every pair.

### The Two Halves

**Theorem (the bracket on the two halves).** For $\tilde H_1,\tilde H_2\in\mathbb{M}_+$ and $\tilde Q_3,\tilde Q_4\in\mathbb{M}_-$,

$$
[\tilde H_1,\tilde H_2]_\varsigma=[\tilde H_1,\tilde H_2] , \qquad [\tilde Q_3,\tilde Q_4]_\varsigma=-[\tilde Q_3,\tilde Q_4] , \qquad [\tilde Q_3,\tilde H_1]_\varsigma=\tilde Q_3\tilde H_1+\tilde H_1\tilde Q_3 ,
$$

where the brackets on the right are the ordinary commutator of the algebra.

**Proof.** For Hermitian $\tilde H_1$ the derived operation is the algebra product in both slots, $\tilde H_1\star\tilde H_2=\tilde H_1\tilde H_2$, so the bracket is the ordinary commutator; for skew-Hermitian $\tilde Q_3$ the involution contributes a sign, $\tilde Q_3^{*}=-\tilde Q_3$, so $[\tilde Q_3,\tilde Q_4]_\varsigma=-(\tilde Q_3\tilde Q_4-\tilde Q_4\tilde Q_3)$; and for the mixed pair $[\tilde Q_3,\tilde H_1]_\varsigma=\tilde Q_3\tilde H_1^{*}-\tilde H_1\tilde Q_3^{*}=\tilde Q_3\tilde H_1+\tilde H_1\tilde Q_3$. This is the theorem of *The Sesquilinear Commutator*, §*The Two Halves*.

**Corollary (the Lie algebra of the skew-Hermitian half).** On the skew-Hermitian half the sesquilinear bracket is $\mathbb{R}$-bilinear, antisymmetric and satisfies the Jacobi identity, being the negative of the commutator of the associative envelope; the sesquilinear bracket and the ordinary commutator make $\mathbb{M}_-$ one and the same Lie algebra over $\mathbb{R}$, up to the sign of the bracket. That Lie algebra is the unitary Lie algebra of *The Unitary Group of the Biquaternion Algebra* and *Lie Algebras of Sesqualgebras*.

**Proof.** The theorem gives $[\tilde Q_3,\tilde Q_4]_\varsigma=-[\tilde Q_3,\tilde Q_4]$ on $\mathbb{M}_-$, and the commutator of an associative algebra is a Lie bracket; the sign carries through the three terms of the Jacobi identity.

### The Failure of the Jacobi Identity

**Theorem.** The Jacobi identity for the sesquilinear bracket fails on $\mathbb{B}$. With the three Hermitian elements

$$
\tilde\Pi_1(\vec u_z)=\tfrac12(e_t+i\vec e_z)=\tilde\Pi_+ , \qquad \tilde\Pi_2(\vec u_z)=\tfrac12(e_t-i\vec e_z)=\tilde\Pi_- , \qquad i\vec e_x ,
$$

the Jacobi sum is

$$
[[\tilde\Pi_+,\tilde\Pi_-]_\varsigma,i\vec e_x]_\varsigma+[[\tilde\Pi_-,i\vec e_x]_\varsigma,\tilde\Pi_+]_\varsigma+[[i\vec e_x,\tilde\Pi_+]_\varsigma,\tilde\Pi_-]_\varsigma=2\vec e_y\neq0 .
$$

**Proof.** The three elements are Hermitian: the two projections by *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, and $i\vec e_x$ because $\vec e_x^{*}=-\vec e_x$. The inner brackets are ordinary commutators by the half-theorem. The first vanishes, $[\tilde\Pi_+,\tilde\Pi_-]_\varsigma=\tilde\Pi_+\tilde\Pi_--\tilde\Pi_-\tilde\Pi_+=0$, because $\tilde\Pi_+\tilde\Pi_-=\tfrac14(e_t+i\vec e_z)(e_t-i\vec e_z)=\tfrac14(e_t-e_t)=0$ and likewise in the other order. The other two are

$$
[\tilde\Pi_-,i\vec e_x]_\varsigma=\tilde\Pi_-i\vec e_x-i\vec e_x\tilde\Pi_-=\tfrac12\bigl(\vec e_y+i\vec e_x\bigr)-\tfrac12\bigl(i\vec e_x-\vec e_y\bigr)=\vec e_y , \qquad
[i\vec e_x,\tilde\Pi_+]_\varsigma=i\vec e_x\tilde\Pi_+-\tilde\Pi_+i\vec e_x=\tfrac12\bigl(\vec e_y+i\vec e_x\bigr)-\tfrac12\bigl(i\vec e_x-\vec e_y\bigr)=\vec e_y ,
$$

where the basis products of *Introduction to the General Plain Sesqualgebra* give the two expansions. Both inner values are the skew-Hermitian $\vec e_y$, and the outer brackets read a skew-Hermitian element with a Hermitian one by the mixed rule $[\tilde Q_1,\tilde H_1]_\varsigma=\tilde Q_1\tilde H_1+\tilde H_1\tilde Q_1$:

$$
[\vec e_y,\tilde\Pi_+]_\varsigma=\vec e_y\tilde\Pi_++\tilde\Pi_+\vec e_y=\tfrac12\bigl(\vec e_y+i\vec e_x\bigr)+\tfrac12\bigl(\vec e_y-i\vec e_x\bigr)=\vec e_y , \qquad
[\vec e_y,\tilde\Pi_-]_\varsigma=\vec e_y\tilde\Pi_-+\tilde\Pi_-\vec e_y=\tfrac12\bigl(\vec e_y-i\vec e_x\bigr)+\tfrac12\bigl(\vec e_y+i\vec e_x\bigr)=\vec e_y .
$$

The Jacobi sum is therefore $0+\vec e_y+\vec e_y=2\vec e_y\neq0$. The same computation in the matrix model is the witness of *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity*, with $E_{11},E_{22},E_{12}+E_{21}$ and the value $2(E_{21}-E_{12})$, transported to $\mathbb{B}$ along the model of *Biquaternion $2\times2$ Matrix Element Representation*, whose inverse carries $E_{21}-E_{12}$ to $\vec e_y$.

**Remark.** Three Hermitian elements suffice, which is the sharp form of the failure: the outer brackets meet skew-Hermitian values, and there they obey the symmetrised rule rather than the commutator rule, so the reassociation that the Jacobi identity performs is performed with a different operation. The failure is produced by the noncommutativity of $\mathbb{B}$ and not by the semilinearity of the multiplication: on the sesquilinear field $\mathbb{C}$ over $(\mathbb{C},\varsigma)$ the bracket $[x,y]_\varsigma=x\overline{y}-y\overline{x}$ is a Lie bracket over $\mathbb{R}$, by *The Sesquilinear Commutator*, §*The Failure of the Jacobi Identity*.

### The Bracket and the Involution

**Proposition.** For all $\tilde Q_1,\tilde Q_2$,

$$
[\tilde Q_1,e_t]_\varsigma=\tilde Q_1-\tilde Q_1^{*} , \qquad [\tilde Q_1,\tilde Q_2]_\varsigma=0\text{ for all }\tilde Q_1,\tilde Q_2 \iff {}^{*}=\mathrm{id}\text{ and }\mathbb{B}\text{ is commutative} ,
$$

and the bracket does not commute with the involution: $[\tilde Q_1,\tilde Q_2]_\varsigma^{*}=[\tilde Q_2,\tilde Q_1]_\varsigma$, which differs from $[\tilde Q_1^{*},\tilde Q_2^{*}]_\varsigma$ in general.

**Proof.** The first display is the proposition of *The Sesquilinear Commutator*, §*The Vanishing and the Involution*, read on $\mathbb{B}$; its vanishing for all $\tilde Q_1$ is the criterion that the involution is trivial, which it is not here. For the last statement, the witness of that article in the matrix model is $\tfrac12(i\vec e_x-\vec e_y)$ and $\tfrac12(e_t+i\vec e_z)$: the bracket vanishes, while the bracket of the conjugates is $\vec e_y$.

**Remark.** The bracket therefore detects the involution on the diagonal, $[\tilde Q_1,e_t]_\varsigma=\tilde Q_1-\tilde Q_1^{*}$, and its vanishing is exactly the Hermitian condition; the bracket measures the asymmetry between the two slots that the involution produces, and it vanishes on the fixed field and on nothing else.

## The Symmetrised Product

### Definition and the Polarisation of the Square

**Definition.** The **symmetrised sesquilinear product** is

$$
\tilde Q_1\circ\tilde Q_2=\tfrac12\bigl(\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1\bigr) , \qquad\text{equivalently}\qquad \tilde Q_1\circ\tilde Q_2=\tilde Q_1\star\tilde Q_2-\tfrac12[\tilde Q_1,\tilde Q_2]_\varsigma .
$$

**Proposition (the polarisation).** For all $\tilde Q_1,\tilde Q_2$,

$$
\tilde Q_1\circ\tilde Q_2=\tfrac12\bigl((\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2)-\tilde Q_1\star\tilde Q_1-\tilde Q_2\star\tilde Q_2\bigr) \quad\text{or, with the complex scalars,}\quad \tilde Q_1\circ\tilde Q_2=\tfrac14\bigl((\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2)-(\tilde Q_1-\tilde Q_2)\star(\tilde Q_1-\tilde Q_2)\bigr) ,
$$

so the squares determine the symmetrised product.

**Proof.** This is the polarisation of *The Sesquilinear Symmetrised Product*, §*The Polarisation of the Square*, using the additivity of the multiplication in each variable; the two forms differ by the coefficient that the expansion requires, and each is the standard polarisation of a quadratic map.

**Remark.** The square $\tilde Q_1\mapsto\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$ therefore determines the symmetric half, and the antisymmetric half is exactly what the square cannot see: the bracket takes opposite values on the two products and cancels in every square. On the diagonal the symmetrised product is the square of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and the polarisation is the reason the square theory and the symmetrised product are the same subject off the diagonal.

### The Hermitian Value

**Theorem.** For all $\tilde Q_1,\tilde Q_2$ the symmetrised product is Hermitian,

$$
(\tilde Q_1\circ\tilde Q_2)^{*}=\tilde Q_1\circ\tilde Q_2 ,
$$

so the symmetrised product is a map $\mathbb{B}\times\mathbb{B}\to\mathbb{M}_+$ into the Hermitian half; its scalar part is the real part of the Hermitian form,

$$
\mathrm{Sc}(\tilde Q_1\circ\tilde Q_2)=\mathrm{Re}\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}=\mathrm{Re}\,\langle\tilde Q_1,\tilde Q_2\rangle_* .
$$

**Proof.** $(\tilde Q_1\star\tilde Q_2)^{*}=\tilde Q_2\star\tilde Q_1$, so $(\tilde Q_1\circ\tilde Q_2)^{*}=\tfrac12(\tilde Q_2\star\tilde Q_1+\tilde Q_1\star\tilde Q_2)=\tilde Q_1\circ\tilde Q_2$; for the scalar part, $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ and $\mathrm{Sc}(\tilde Q_2\star\tilde Q_1)=\overline{\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}}}$, and the half-sum is the real part. This is the theorem of *The Sesquilinear Symmetrised Product*, §*The Hermitian Value*.

**Remark.** The image of the symmetrised product is therefore contained in the Hermitian half whatever the two arguments, and the scalar part is real and equal to the real part of the Hermitian form. The plain symmetrisation $\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1$ of the algebra product has no such property: its value is Hermitian only when the two arguments lie in the right halves, and the comparison of the two is the next section.

### The Hermitian Half

**Theorem (the symmetrisation on the Hermitian half).** For $\tilde H_1,\tilde H_2\in\mathbb{M}_+$,

$$
\tilde H_1\circ\tilde H_2=\tfrac12\bigl(\tilde H_1\tilde H_2+\tilde H_2\tilde H_1\bigr) ,
$$

the plain symmetrisation, and with this product $\mathbb{M}_+$ is a commutative Jordan algebra over $\mathbb{R}$, with the Jordan identity

$$
(\tilde H_1\circ\tilde H_2)\circ(\tilde H_1\circ\tilde H_1)=\tilde H_1\circ\bigl(\tilde H_2\circ(\tilde H_1\circ\tilde H_1)\bigr) .
$$

**Proof.** For Hermitian $\tilde H_1$ the derived operation is the algebra product, $\tilde H_1\star\tilde H_2=\tilde H_1\tilde H_2$ and $\tilde H_2\star\tilde H_1=\tilde H_2\tilde H_1$; the two symmetrisations therefore agree on the half, and the symmetrisation of an associative product satisfies the Jordan identity, by *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*. This is the theorem of *The Sesquilinear Symmetrised Product*, §*On the Hermitian Part*.

**Remark.** The Jordan algebra is the Hermitian Jordan algebra of *The Hermitian Jordan Algebra* and of *The 12 Products of the Biquaternion Complex Space*, and it is the positive cone theory of *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*. The sesquilinear symmetrisation is therefore a Jordan product exactly on the Hermitian half, and there it is the same product as the one the algebra symmetrisation of the same article carries on that half.

### The Failure of the Jordan Identity

**Proposition (the identity fails off the Hermitian half).** On $\mathbb{B}$ there are elements with

$$
(\tilde Q_3\circ\tilde\Pi_-)\circ(\tilde Q_3\circ\tilde Q_3)\neq\tilde Q_3\circ\bigl(\tilde\Pi_-\circ(\tilde Q_3\circ\tilde Q_3)\bigr) .
$$

With

$$
\tilde Q_3=\tfrac12(i\vec e_x-\vec e_y) , \qquad \tilde\Pi_-=\tfrac12(e_t-i\vec e_z)=\tilde\Pi_2(\vec u_z) ,
$$

the two sides are

$$
(\tilde Q_3\circ\tilde\Pi_-)\circ(\tilde Q_3\circ\tilde Q_3)=\tfrac{i}{4}\vec e_x , \qquad \tilde Q_3\circ\bigl(\tilde\Pi_-\circ(\tilde Q_3\circ\tilde Q_3)\bigr)=0 ,
$$

and the first is not zero.

**Proof.** The computation is the one of *The Sesquilinear Symmetrised Product*, §*Off the Hermitian Part*, transported to $\mathbb{B}$ along the model of *Biquaternion $2\times2$ Matrix Element Representation*: the element $\tilde Q_3$ is the image of the matrix unit $E_{12}$ and the element $\tilde\Pi_-$ the image of $E_{22}$, whose symmetrised products are

$$
\tilde Q_3\circ\tilde Q_3=\tilde Q_3\tilde Q_3^{*}=\tfrac12(e_t+i\vec e_z) , \qquad \tilde Q_3\circ\tilde\Pi_-=\tfrac{i}{2}\vec e_x , \qquad \tilde\Pi_-\circ(\tilde Q_3\circ\tilde Q_3)=0 ,
$$

the last because $\tilde\Pi_-\tilde Q_3\tilde Q_3^{*}=0$; the two sides of the identity are then $\tfrac{i}{4}\vec e_x$ and $0$, as the transport of $\tfrac14(E_{12}+E_{21})$ and $0$ along the inverse of the model.

**Remark.** One of the two elements is Hermitian, $\tilde\Pi_-$, and one is not, $\tilde Q_3$; a single element off the Hermitian half is enough to break the identity, and the perturbation is exactly the failure of $\tilde Q_3$ to be Hermitian. The value $\tilde Q_3\circ\tilde Q_3=\tilde Q_3\tilde Q_3^{*}=\tfrac12(e_t+i\vec e_z)$ is Hermitian, as the Hermitian-value theorem promises, but the symmetry of the derived product with one slot off the half is the wrong one to carry the identity. The failure is the reason the Jordan structure of the sesqualgebra lives on the Hermitian half alone, and it is *Jordan Algebras of Sesqualgebras*, §*The Hermitian Part*, that locates it there.

## The Biquaternion Interpretation

### The Two Operations on the Basis

**Proposition (the symmetrised basis).** On the real basis $e_t,\vec e_x,\vec e_y,\vec e_z$,

$$
e_\mu\circ e_\nu=\delta_{\mu\nu}\,e_t ,
$$

so for elements with real coordinates the symmetrised product is $e_t$ times the Euclidean dot product of the coordinate vectors.

**Proof.** $e_\mu\circ e_\mu=e_\mu\star e_\mu=\varepsilon_\mu e_\mu^{2}$: for $\mu=0$ this is $e_t$, and for $\mu=k$ it is $(-1)(-e_t)=e_t$. For $\mu\neq\nu$ the two terms of the symmetrisation are $\varepsilon_\nu e_\mu e_\nu$ and $\varepsilon_\mu e_\nu e_\mu$, and the basis products anticommute, $e_\mu e_\nu=-e_\nu e_\mu$, with $\varepsilon_\mu=\varepsilon_\nu$ unless one of the indices is $0$; in every case the two terms cancel.

**Proposition (the commutator basis).** On the real basis,

$$
[e_t,\vec e_\mu]_\varsigma=-2\vec e_\mu , \qquad [\vec e_\mu,\vec e_\nu]_\varsigma=-2\,\vec e_\mu\times \vec e_\nu ,
$$

the second for the vector indices, so on the vector part the bracket is $-2$ times the cross product of the vector parts.

**Proof.** $[e_t,\vec e_\mu]_\varsigma=e_t \vec e_\mu^{*}-\vec e_\mu e_t^{*}=-\vec e_\mu-\vec e_\mu=-2\vec e_\mu$, using $\vec e_\mu^{*}=-\vec e_\mu$; for the vector indices, $[\vec e_\mu,\vec e_\nu]_\varsigma=\vec e_\mu \vec e_\nu^{*}-\vec e_\nu \vec e_\mu^{*}=-\vec e_\mu \vec e_\nu+\vec e_\nu \vec e_\mu=-2\vec e_\mu \vec e_\nu=-2\,\vec e_\mu\times \vec e_\nu$ for distinct $\mu,\nu$, and it vanishes for $\mu=\nu$.

**Remark.** The two tables are the extreme cases of the split: the symmetrised product of two distinct basis elements vanishes and the diagonal values are all $e_t$, so the symmetric half of the multiplication is the pairing that makes of the basis an orthogonal set with the constant square $e_t$; the bracket of two distinct basis elements is $-2$ times their cross product, so the antisymmetric half is the cross product of the vector part read with the coefficient $-2$, which is the negative of the ordinary commutator on the vector elements. The scalar part of the symmetrised product is $\mathrm{Re}\,\langle\tilde Q_1,\tilde Q_2\rangle_*$, and the scalar part of the bracket is $2i\,\mathrm{Im}\,\langle\tilde Q_1,\tilde Q_2\rangle_*$.

### The Comparison with the Two Bilinear Operations

The bilinear commutator $\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1$ and the bilinear symmetrisation $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of *The 12 Products of the Biquaternion Complex Space* are $\mathbb{C}$-bilinear and satisfy their identities on the whole algebra. The sesquilinear operations agree with them on the Hermitian half and fail off it.

| operation | bilinear or sesquilinear | Jacobi identity | Jordan identity |
|---|---|---|---|
| $\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1$ | bilinear | holds on $\mathbb{B}$ | not asked |
| $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | bilinear | not asked | holds on $\mathbb{B}$ |
| $[\tilde Q_1,\tilde Q_2]_\varsigma$ | sesquilinear | fails; holds on $\mathbb{M}_-$ | not asked |
| $\tilde Q_1\circ\tilde Q_2$ | sesquilinear | not asked | holds on $\mathbb{M}_+$, fails off it |

**Remark.** The table is the biquaternion form of the general dichotomy: the bilinear operations are $\mathbb{C}$-bilinear and carry their identities everywhere, the sesquilinear operations are $\mathbb{R}$-bilinear, and their identities survive exactly on the half where the derived operation coincides with the algebra product. On the Hermitian half the four rows collapse to two, the sesquilinear operations agreeing with the bilinear ones there; the failure of the Jordan identity of §*The Failure of the Jordan Identity* uses the element $\tilde Q_3$ off the half, and the failure of the Jacobi identity of §*The Failure of the Jacobi Identity* uses the symmetrised rule that the outer brackets obey on the skew-Hermitian values.

## Summary

The sesquilinear multiplication splits as $\tilde Q_1\star\tilde Q_2=\tilde Q_1\circ\tilde Q_2+\tfrac12[\tilde Q_1,\tilde Q_2]_\varsigma$ into the symmetrised product and the sesquilinear commutator, both $\mathbb{R}$-bilinear and no more, $\mathbb{R}$ being the fixed field of the conjugation. The commutator is antisymmetric, takes its values in the skew-Hermitian half, and is the negative of the ordinary commutator on that half, so the skew-Hermitian half is a Lie algebra over $\mathbb{R}$, the unitary Lie algebra; its Jacobi identity fails on the whole algebra, with the three-Hermitian-element witness $\tilde\Pi_1(\vec u_z),\tilde\Pi_2(\vec u_z),i\vec e_x$ giving $2\vec e_y$, because the outer brackets obey the symmetrised rule on the skew-Hermitian values.

The symmetrised product is the polarisation of the square, takes its values in the Hermitian half, has scalar part the real part of the Hermitian form, and agrees with the plain symmetrisation on the Hermitian half, where it is a Jordan algebra; off the half the Jordan identity fails, with the witness $\tilde Q_3=\tfrac12(i\vec e_x-\vec e_y)$, $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ giving $\tfrac{i}{4}\vec e_x$ against $0$. On the basis the symmetrised product is $\delta_{\mu\nu}e_t$ and the commutator of two vector basis elements is $-2$ times their cross product. The two bilinear operations of *The 12 Products of the Biquaternion Complex Space* are the $\mathbb{C}$-bilinear case, with their identities everywhere; the sesquilinear operations carry them on the two halves alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\circ\tilde Q_2=\tfrac12(\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1)$ | the symmetrised sesquilinear product, Hermitian-valued |
| $[\tilde Q_1,\tilde Q_2]_\varsigma=\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1$ | the sesquilinear commutator, skew-Hermitian-valued |
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\circ\tilde Q_2+\tfrac12[\tilde Q_1,\tilde Q_2]_\varsigma$ | the split of the multiplication |
| $\tilde Q_1\circ\tilde Q_1=\tilde Q_1\star\tilde Q_1=\tilde Q_1\tilde Q_1^{*}$ | the diagonal is the square |
| $\mathbb{R}=\mathbb{C}^{\varsigma}$ | the fixed field, the ring of scalars of the two operations |
| $[\tilde H_1,\tilde H_2]_\varsigma=[\tilde H_1,\tilde H_2]$ | the bracket on the Hermitian half |
| $[\tilde Q_1,\tilde Q_2]_\varsigma=-[\tilde Q_1,\tilde Q_2]$, $\tilde Q_1,\tilde Q_2\in\mathbb{M}_-$ | the bracket on the skew-Hermitian half, the unitary Lie algebra |
| $(\tilde H_1\circ\tilde H_2)\circ(\tilde H_1\circ\tilde H_1)=\tilde H_1\circ(\tilde H_2\circ(\tilde H_1\circ\tilde H_1))$ | the Jordan identity, on $\mathbb{M}_+$ |
| $\tilde\Pi_1(\vec u_z),\tilde\Pi_2(\vec u_z),i\vec e_x$ | the Hermitian triple whose Jacobi sum is $2\vec e_y$ |
| $\tfrac12(i\vec e_x-\vec e_y),\tfrac12(e_t-i\vec e_z)$ | the pair whose Jordan identity fails, $\tfrac{i}{4}\vec e_x$ against $0$ |
| $e_\mu\circ e_\nu=\delta_{\mu\nu}e_t$ | the symmetrised product on the basis |
| $[\vec e_\mu,\vec e_\nu]_\varsigma=-2\,\vec e_\mu\times \vec e_\nu$ | the commutator on the vector basis |
| $\mathrm{Sc}(\tilde Q_1\circ\tilde Q_2)=\mathrm{Re}\langle\tilde Q_1,\tilde Q_2\rangle_*$ | the scalar part of the symmetrised product |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the Jacobi identity, the Lie algebras of an associative algebra and the unitary Lie algebra.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the Jordan identity, the symmetrisation of an associative algebra and the Lie-admissible and Jordan-admissible algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan product, its powers and the Jordan identity.
- K. A. Zhevlakov, A. M. Slin'ko, I. P. Shestakov and A. I. Shirshov, *Rings That Are Nearly Associative* (Academic Press, 1982), for the identities of the Lie and the Jordan symmetrisations of a non-associative algebra.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the skew-symmetric elements, the commutator of an involutive ring and the Lie structure it carries.
