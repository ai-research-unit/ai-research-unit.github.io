
# __The Adjoint of the Sesquilinear Sandwich on the Biquaternions__

## Introduction

The sesquilinear sandwich $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*}$ of *The Sesquilinear Sandwich on the Biquaternions* is a conjugate-linear operator, and the Hermitian form

$$
\varphi(\tilde X,\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y^{*})=\sum_\mu X_\mu\overline{Y_\mu}=\tfrac12\,\mathrm{tr}\bigl(\Phi(\tilde X)\Phi(\tilde Y)^{\dagger}\bigr)
$$

of *Biquaternion Norm and Invertibility* is perfect and sesqui-symmetric. The two together give the **adjoint** of the sandwich: the conjugate-linear operator $S_{\tilde P,\tilde Q}^{\dagger}$ characterised by

$$
\varphi\bigl(S_{\tilde P,\tilde Q}\tilde X,\tilde Y\bigr)=\overline{\varphi\bigl(\tilde X,S_{\tilde P,\tilde Q}^{\dagger}\tilde Y\bigr)} .
$$

The computation is one line in the coordinates, and its result is symmetric and memorable:

$$
S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}} , \qquad\text{equivalently}\qquad (\tilde P\star\cdot\star\tilde Q)^{\dagger}=\tilde Q^{*}\star\cdot\star\tilde P^{*} .
$$

The adjoint exchanges the two parameters and conjugates them; it is an involution on the sandwich family, and the **self-adjoint** sandwiches are those whose two parameters are a conjugate pair, $S_{\tilde P,\tilde P^{*}}$, the conjugate pair being the self-adjoint pairs up to the scalar ambiguity of the parametrisation. The quadratic representation of the ternary product, which is the sandwich $\tilde Z\tilde Y^{*}\tilde Z=S_{\tilde Z,\tilde Z^{*}}$, is therefore self-adjoint, and this is the operator form of the Hermitian symmetry of the ternary product.

The article is the seventh of the batch and reads the general article *The Sesquilinear Adjoint Operator*, whose definition for a conjugate-linear operator, twisted rule and computation for the standard model are quoted; the operator whose adjoint is taken is *The Sesquilinear Sandwich on the Biquaternions*, above in this group, and its relation to the ternary product is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*. The ternary forms of the adjoint are *The Adjoint of the Ternary Product* and *The Ternary Product as an Operator*, and the model in which the form becomes the trace is *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*. The two one-sided operators whose adjoints are computed below are those of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

The setting is that of *Introduction to the General Plain Sesqualgebra of Biquaternions*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The sandwich is $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ and the ordinary two-sided multiplication is $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$.

## The Hermitian Form and the Adjoint

### The Form

**Recall.** The Hermitian form of *Biquaternion Norm and Invertibility* is

$$
\varphi(\tilde X,\tilde Y)=\mathrm{Sc}\bigl(\tilde X\tilde Y^{*}\bigr)=\sum_{\mu=0}^{3}X_\mu\overline{Y_\mu} ,
$$

with the scalar part $\mathrm{Sc}$ of *Introduction to the General Plain Sesqualgebra of Biquaternions*; it is $\mathbb{C}$-linear in the first argument, conjugate-linear in the second, sesqui-symmetric, $\varphi(\tilde Y,\tilde X)=\overline{\varphi(\tilde X,\tilde Y)}$, and nondegenerate.

**Proposition (the form is perfect).** If $\varphi(\tilde X,\tilde Y)=0$ for every $\tilde Y$ then $\tilde X=0$, and the same in the other argument; hence every conjugate-linear operator has a unique adjoint.

**Proof.** Taking $\tilde Y=e_\mu$ gives $\varphi(\tilde X,e_\mu)=X_\mu$, so the vanishing for every $\mu$ gives the vanishing of $\tilde X$; the other argument is the sesqui-symmetry. Uniqueness of the adjoint is the standard consequence of nondegeneracy. $\square$

**Remark.** The form is the pairing that the model renders as the trace pairing of *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*, $\varphi(\tilde X,\tilde Y)=\tfrac12\mathrm{tr}(\Phi(\tilde X)\Phi(\tilde Y)^{\dagger})$, and it is the form with respect to which the involution is the Hermitian conjugation. Its scalar part is the real part of the symmetrised product, by *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions*.

### The Twisted Adjoint Rule

**Definition.** For a conjugate-linear operator $S$ the **adjoint** $S^{\dagger}$ is the conjugate-linear operator defined by

$$
\varphi(S\tilde X,\tilde Y)=\overline{\varphi(\tilde X,S^{\dagger}\tilde Y)}
$$

for all $\tilde X,\tilde Y$. For a linear operator $T$ the adjoint is defined by $\varphi(T\tilde X,\tilde Y)=\varphi(\tilde X,T^{\dagger}\tilde Y)$; the two rules differ by the conjugation, which is the twist that the conjugate-linear case requires.

**Proposition.** The adjoint is well defined, conjugate-linear in the operator, and involutive: $S^{\dagger\dagger}=S$; a conjugate-linear operator is **self-adjoint** when $S^{\dagger}=S$.

**Proof.** The definitions are those of *The Sesquilinear Adjoint Operator*, §*The Definition*, on the sesqualgebra $\mathbb{B}$ with the form $\varphi$; the existence and the uniqueness are the perfection of §*The Form*, and the involution follows by applying the definition twice and using the sesqui-symmetry. $\square$

**Remark.** The twist is not a convention but a necessity: a conjugate-linear operator cannot be self-adjoint under the linear rule unless it vanishes, exactly as a nonzero left multiplication cannot be $\mathbb{C}$-linear, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*. The two rules are the two parities of the operator theory read through the form.

### The General Theorem

**Theorem.** For the standard model $a\star x\star b=ax^{*}b$ of *The Sesquilinear Adjoint Operator*, the adjoint of the sandwich $S_{a,b}(x)=ax^{*}b$ is $S_{a,b}^{\dagger}=S_{b,a}$; for the ordinary two-sided multiplication $T_{p,q}(x)=pxq$ the adjoint is $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$.

**Proof.** These are the two computations of *The Sesquilinear Adjoint Operator*, §*The Sandwich and the Two-Sided Multiplication*, with the trace functional $\tau$ of that article read as the scalar part $\mathrm{Sc}$ here, the datum $(\mathbb{C},\varsigma)$ being the conjugation on the scalars; the compatibility $\mathrm{Sc}(\tilde U^{*})=\overline{\mathrm{Sc}(\tilde U)}$ and the centrality $\mathrm{Sc}(\tilde U\tilde V)=\mathrm{Sc}(\tilde V\tilde U)$ are the properties of the scalar part, and the pairings are perfect by §*The Form*. $\square$

**Remark.** The translation between the general notation and the notation of this batch is the placement of the star: in the general article the sandwich is $ax^{*}b$, while the batch writes the sandwich of *The Sesquilinear Sandwich on the Biquaternions* as $\tilde P\tilde X^{*}\tilde Q^{*}$, that is $S_{\tilde P,\tilde Q}=S_{\tilde P,\tilde Q^{*}}$ in the general notation, with the second parameter conjugated. The next section translates the general theorem accordingly.

## The Adjoint of the Sandwich

### The Main Identity

**Theorem (the adjoint of the sandwich).** For all $\tilde P,\tilde Q$,

$$
S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}} ,
$$

that is, $(\tilde P\star\cdot\star\tilde Q)^{\dagger}=\tilde Q^{*}\star\cdot\star\tilde P^{*}$; explicitly,

$$
\varphi\bigl(\tilde P\tilde X^{*}\tilde Q^{*},\tilde Y\bigr)=\overline{\varphi\bigl(\tilde X,\tilde Q^{*}\tilde Y^{*}\tilde P\bigr)} .
$$

**Proof.** The general sandwich of *The Sesquilinear Adjoint Operator*, §*The Sandwich and the Two-Sided Multiplication*, is $S_{a,b}(x)=ax^{*}b$ with the adjoint $S_{b,a}$; the batch sandwich is $S_{\tilde P,\tilde Q}=S_{\tilde P,\tilde Q^{*}}$ in that notation, so the general theorem gives $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P}$, and $S_{\tilde Q^{*},\tilde P}$ is the batch sandwich with the first parameter $\tilde Q^{*}$ and the second parameter $\tilde P^{*}$, that is $S_{\tilde Q^{*},\tilde P^{*}}$ because the batch writes the second parameter already starred. The explicit display is the resulting computation in the coordinates. $\square$

**Remark.** The adjoint therefore stars the two parameters and exchanges them, and it is again a sandwich. Applied twice it returns the original, $S_{\tilde P,\tilde Q}^{\dagger\dagger}=S_{\tilde P,\tilde Q}$, so the adjoint is an involution on the sandwich family; it is conjugate-linear in the sandwich and it exchanges the two parameters, which is the operator form of the exchange of the two outer slots of the ternary product.

### The Exchange Identity

**Corollary (the identity that exchanges the two).** For all $\tilde P,\tilde Q,\tilde X,\tilde Y$,

$$
\varphi\bigl(S_{\tilde P,\tilde Q}\tilde X,\tilde Y\bigr)=\overline{\varphi\bigl(\tilde X,S_{\tilde Q^{*},\tilde P^{*}}\tilde Y\bigr)} ,
$$

and with the Hermitian adjoint written $S^{\dagger}$ the identity is the definition of the adjoint of §*The Twisted Adjoint Rule*.

**Proof.** Immediate from the theorem and the definition; the interest is that the sandwich of the adjoint parameters is again a sandwich, so the family is stable under the adjoint. $\square$

**Remark.** The stability is not automatic: the adjoint of an arbitrary conjugate-linear operator is not a sandwich, and the theorem says that the sandwich family is closed under the adjoint. This is the operator analogue of the closure of the Hermitian half under the symmetrised product, and it is the reason the ternary operators of the batch carry adjoints inside the batch.

### The Self-Adjoint Sandwiches

**Theorem (the self-adjoint criterion).** The sandwich $S_{\tilde P,\tilde Q}$ is self-adjoint if and only if $S_{\tilde Q^{*},\tilde P^{*}}=S_{\tilde P,\tilde Q}$; in particular every sandwich with conjugate parameters is self-adjoint,

$$
S_{\tilde P,\tilde P^{*}}(\tilde X)=\tilde P\tilde X^{*}\tilde P ,
$$

and for two invertible parameters the criterion is equivalent to $\tilde Q=\bar c\,\tilde P^{*}$ for a nonzero complex number $c$, so that the self-adjoint sandwiches with invertible parameters are the conjugate pairs up to that scalar ambiguity.

**Proof.** By the main identity, $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$, so self-adjointness is the equality $S_{\tilde Q^{*},\tilde P^{*}}=S_{\tilde P,\tilde Q}$. The conjugate pair satisfies it, because $(\tilde Q^{*},\tilde P^{*})=(\tilde P,\tilde P^{*})$ when $\tilde Q=\tilde P^{*}$. Conversely the equality of two sandwiches is the equality of two parametrised two-sided operators, and the kernel of the parametrisation is the group of the central units $\tilde Z=c\,e_0$, by *The Sesquilinear Sandwich on the Biquaternions*, §*The Invertible Sandwiches*; for invertible parameters the equality therefore reads $(\tilde Q^{*},\tilde P^{*})=(\tilde P\tilde Z,\tilde Q\tilde Z^{-1*})$ with $\tilde Z=c\,e_0$ a central unit, $c\in\mathbb{C}^{\times}$, that is $\tilde Q^{*}=c\tilde P$ and $\tilde P^{*}=\bar c^{-1}\tilde Q$, which is the single equation $\tilde Q=\bar c\,\tilde P^{*}$. $\square$

**Remark.** The self-adjoint sandwiches are therefore the sandwiches of the conjugate pairs, and they are parametrised by the elements $\tilde P$ of the algebra together with the scalar ambiguity $\tilde Q=\bar c\,\tilde P^{*}$, a four-dimensional complex family of operators. The adjoint is an involution on the sandwich family, so the self-adjoint sandwiches are the fixed points of that involution. The involution $S_{e_0,e_0}={}^{*}$ is the case $\tilde P=e_0$, and it is self-adjoint; the quadratic representation of the ternary product is the general case, by the next section.

## The Special Cases

### The Involution

**Proposition.** The involution is self-adjoint, ${}^{*\dagger}={}^{*}$, so

$$
\varphi(\tilde X^{*},\tilde Y)=\overline{\varphi(\tilde X,\tilde Y^{*})} .
$$

**Proof.** The involution is the sandwich $S_{e_0,e_0}$, and $S_{e_0,e_0}^{\dagger}=S_{e_0^{*},e_0^{*}}=S_{e_0,e_0}$ by the main identity. $\square$

**Remark.** The involution is the unique sandwich that is also a two-sided multiplication with the identity parameters, and its self-adjointness is the starting case of the criterion. In the model it is the Hermitian transpose, which is self-adjoint for the trace form, by *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*.

### The One-Sided and the Two-Sided Multiplications

**Theorem.** For the left multiplication, the right multiplication and the ordinary two-sided multiplication,

$$
L_{\tilde P}^{\dagger}=S_{e_0,\tilde P^{*}} , \qquad R_{\tilde Q}^{\dagger}=T_{e_0,\tilde Q} , \qquad T_{\tilde P,\tilde Q}^{\dagger}=T_{\tilde P^{*},\tilde Q^{*}} .
$$

**Proof.** The left multiplication is the sandwich $S_{\tilde P,e_0}$, so the main identity gives $L_{\tilde P}^{\dagger}=S_{e_0,\tilde P^{*}}$. The right multiplication is linear and equals $T_{e_0,\tilde Q^{*}}$, so the second display is the general theorem for the two-sided multiplication; the third display is the same theorem. $\square$

**Remark.** The left multiplication is conjugate-linear and its adjoint is a sandwich with a unit in the first slot; the operator $S_{e_0,\tilde P^{*}}$ is the map $\tilde X\mapsto\tilde X^{*}\tilde P$, which is neither a left nor a right multiplication, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*, and it is the mixed composite $R_{\tilde P^{*}}L_{e_0}$. The right multiplication is linear and its adjoint is again an ordinary multiplication on the other side. This is the operator form of the asymmetry of the two sides that the one-sided unit produces.

### The Quadratic Representation

**Corollary.** The quadratic representation of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*,

$$
\tilde Y\longmapsto\tilde Z\tilde Y^{*}\tilde Z=S_{\tilde Z,\tilde Z^{*}}(\tilde Y) ,
$$

is self-adjoint for every $\tilde Z$.

**Proof.** The quadratic representation is the sandwich $S_{\tilde Z,\tilde Z^{*}}$, whose two parameters are conjugate to each other, so the self-adjoint criterion applies. $\square$

**Remark.** The self-adjointness of the quadratic representation is the operator form of the Hermitian symmetry $\{x,y,z\}^{*}=\{z^{*},y^{*},x^{*}\}$ of the ternary product: the symmetry exchanges the two outer slots, and the adjoint exchanges the two parameters, so the two exchanges are the same statement. The adjoint of the ternary product with arbitrary parameters is *The Adjoint of the Ternary Product*, where the same identity is developed for the general algebraic $J^{*}$-triple.

## The Matrix Model Reading

**Proposition.** In the model of *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model* the sandwich is $S_{P,Q}(X)=PX^{\dagger}Q^{\dagger}$ and the form is $\varphi(X,Y)=\tfrac12\mathrm{tr}(XY^{\dagger})$, with $P=\Phi(\tilde P)$ and $Q=\Phi(\tilde Q)$ the matrices of the two parameters; the adjoint of the sandwich is

$$
S_{P,Q}^{\dagger}(X)=Q^{\dagger}X^{\dagger}P ,
$$

which is the sandwich of the adjoint parameters, the two matrices exchanged and each read with the Hermitian transpose.

**Proof.** In the model the involution is the Hermitian transpose, so $\Phi(S_{\tilde Q^{*},\tilde P^{*}}(\tilde X))=\Phi(\tilde Q^{*})\Phi(\tilde X)^{\dagger}\Phi(\tilde P^{*})^{\dagger}=Q^{\dagger}X^{\dagger}(P^{\dagger})^{\dagger}=Q^{\dagger}X^{\dagger}P$, which is the display; the trace form is the standard form of the matrix algebra, for which the adjoint of $X\mapsto PX^{\dagger}Q^{\dagger}$ is $X\mapsto Q^{\dagger}X^{\dagger}P$ by the theorem. $\square$

**Remark.** The model makes the adjoint an explicit operation on the two outer factors: the adjoint of the sandwich with the matrices $P$ and $Q$ is the sandwich with the two matrices exchanged and Hermitian-transposed, that is the sandwich of the matrices of the adjoint elements $\tilde Q^{*}$ and $\tilde P^{*}$. This is the matrix form of the exchange of the two outer slots of the ternary product, and it is the same exchange that the identity of §*The Exchange Identity* performs on the parameters.

## Summary

With respect to the Hermitian form $\varphi(\tilde X,\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y^{*})$ the adjoint of the sandwich $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ is $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$: the adjoint stars the two parameters and exchanges them, satisfies the identity $\varphi(S_{\tilde P,\tilde Q}\tilde X,\tilde Y)=\overline{\varphi(\tilde X,S_{\tilde Q^{*},\tilde P^{*}}\tilde Y)}$, and is an involution on the sandwich family. The self-adjoint sandwiches are the sandwiches with conjugate parameters, $S_{\tilde P,\tilde P^{*}}=\tilde P(\cdot)^{*}\tilde P$, and the involution $S_{e_0,e_0}={}^{*}$ and the quadratic representation $S_{\tilde Z,\tilde Z^{*}}$ of the ternary product are the two distinguished cases. The left multiplication has the adjoint $S_{e_0,\tilde P^{*}}$, the right multiplication the adjoint $T_{e_0,\tilde Q}$, and the ordinary two-sided multiplication the adjoint $T_{\tilde P^{*},\tilde Q^{*}}$. In the model the adjoint of $X\mapsto PX^{\dagger}Q^{\dagger}$ is $X\mapsto Q^{\dagger}X^{\dagger}P$, the two factors exchanged and conjugated, and the form is the trace pairing.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varphi(\tilde X,\tilde Y)=\mathrm{Sc}(\tilde X\tilde Y^{*})=\sum_\mu X_\mu\overline{Y_\mu}$ | the Hermitian form, perfect and sesqui-symmetric |
| $\varphi(S\tilde X,\tilde Y)=\overline{\varphi(\tilde X,S^{\dagger}\tilde Y)}$ | the twisted adjoint rule for a conjugate-linear operator |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ | the sandwich |
| $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$ | the adjoint of the sandwich |
| $\varphi(S_{\tilde P,\tilde Q}\tilde X,\tilde Y)=\overline{\varphi(\tilde X,S_{\tilde Q^{*},\tilde P^{*}}\tilde Y)}$ | the identity that exchanges the two parameters |
| $S_{\tilde P,\tilde P^{*}}=\tilde P(\cdot)^{*}\tilde P$ | the self-adjoint sandwiches with conjugate parameters |
| $S_{e_0,e_0}={}^{*}$ | the involution, self-adjoint |
| $S_{\tilde Z,\tilde Z^{*}}(\tilde Y)=\tilde Z\tilde Y^{*}\tilde Z$ | the quadratic representation, self-adjoint |
| $L_{\tilde P}^{\dagger}=S_{e_0,\tilde P^{*}}$ | the adjoint of the left multiplication |
| $R_{\tilde Q}^{\dagger}=T_{e_0,\tilde Q}$ | the adjoint of the right multiplication |
| $T_{\tilde P,\tilde Q}^{\dagger}=T_{\tilde P^{*},\tilde Q^{*}}$ | the adjoint of the ordinary two-sided multiplication |
| $S_{P,Q}^{\dagger}(X)=Q^{\dagger}X^{\dagger}P$ | the adjoint in the matrix model |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the adjoint of a semilinear operator with respect to a sesquilinear form over a ring with involution.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutive rings, the Hermitian forms they carry and the adjoints they define.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for the involution and the adjoint operation, and for the conjugation of the adjoint of a semilinear map.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the Hermitian forms, the adjoint operation and the triple products associated with them.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the conjugate transpose, the trace form and the adjoint of a matrix product.
