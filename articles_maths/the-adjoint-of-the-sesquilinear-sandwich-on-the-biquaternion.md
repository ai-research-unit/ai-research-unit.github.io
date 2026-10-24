
# __The Adjoint of the Sesquilinear Sandwich on the Biquaternion__

## Introduction

The sesquilinear sandwich $S_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\star\tilde Q_1\star\tilde Q_3=\tilde Q\tilde Q_1^{*}\tilde Q_3^{*}$ of *The Sesquilinear Sandwich on the Biquaternion* is a conjugate-linear operator, and the Hermitian form

$$
\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}=\tfrac12\,\mathrm{tr}\bigl(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger}\bigr)
$$

of *The Four Forms and the Four Algebraic Norms* is perfect and sesqui-symmetric. The two together give the **adjoint** of the sandwich: the conjugate-linear operator $S_{\tilde Q,\tilde Q_3}^{\dagger}$ characterised by

$$
\varphi\bigl(S_{\tilde Q,\tilde Q_3}\tilde Q_1,\tilde Q_2\bigr)=\overline{\varphi\bigl(\tilde Q_1,S_{\tilde Q,\tilde Q_3}^{\dagger}\tilde Q_2\bigr)} .
$$

The computation is one line in the coordinates, and its result is symmetric and memorable:

$$
S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q^{*}} , \qquad\text{equivalently}\qquad (\tilde Q\star\cdot\star\tilde Q_3)^{\dagger}=\tilde Q_3^{*}\star\cdot\star\tilde Q^{*} .
$$

The adjoint exchanges the two parameters and conjugates them; it is an involution on the sandwich family, and the **self-adjoint** sandwiches are those whose two parameters are a conjugate pair, $S_{\tilde Q,\tilde Q^{*}}$, the conjugate pair being the self-adjoint pairs up to the scalar ambiguity of the parametrisation. The quadratic representation of the ternary product, which is the sandwich $\tilde Q_3\tilde Q_2^{*}\tilde Q_3=S_{\tilde Q_3,\tilde Q_3^{*}}$, is therefore self-adjoint, and this is the operator form of the Hermitian symmetry of the ternary product.

The article is the seventh of the batch and reads the general article *The Sesquilinear Adjoint Operator*, whose definition for a conjugate-linear operator, twisted rule and computation for the standard model are quoted; the operator whose adjoint is taken is *The Sesquilinear Sandwich on the Biquaternion*, above in this group, and its relation to the ternary product is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*. The ternary forms of the adjoint are *The Adjoint of the Ternary Product* and *The Ternary Product as an Operator*, and the model in which the form becomes the trace is *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*. The two one-sided operators whose adjoints are computed below are those of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

The setting is that of *Introduction to the General Plain Sesqualgebra*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde Q\star\tilde Q_3=\tilde Q\tilde Q_3^{*}$. The sandwich is $S_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}\tilde Q_3^{*}$ and the ordinary two-sided multiplication is $T_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_3$.

## The Hermitian Form and the Adjoint

### The Form

**Recall.** The Hermitian form of *The Four Forms and the Four Algebraic Norms* is

$$
\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu}\overline{Q_{2\mu}} ,
$$

with the scalar part $\mathrm{Sc}$ of *Introduction to the General Plain Sesqualgebra*; it is $\mathbb{C}$-linear in the first argument, conjugate-linear in the second, sesqui-symmetric, $\varphi(\tilde Q_2,\tilde Q_1)=\overline{\varphi(\tilde Q_1,\tilde Q_2)}$, and nondegenerate.

**Proposition (the form is perfect).** If $\varphi(\tilde Q_1,\tilde Q_2)=0$ for every $\tilde Q_2$ then $\tilde Q_1=0$, and the same in the other argument; hence every conjugate-linear operator has a unique adjoint.

**Proof.** Taking $\tilde Q_2=e_\mu$ gives $\varphi(\tilde Q_1,e_\mu)=Q_{1\mu}$, so the vanishing for every $\mu$ gives the vanishing of $\tilde Q_1$; the other argument is the sesqui-symmetry. Uniqueness of the adjoint is the standard consequence of nondegeneracy.

**Remark.** The form is the pairing that the model renders as the trace pairing of *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*, $\varphi(\tilde Q_1,\tilde Q_2)=\tfrac12\mathrm{tr}(\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2)^{\dagger})$, and it is the form with respect to which the involution is the Hermitian conjugation. Its scalar part is the real part of the symmetrised product, by *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternion*.

### The Twisted Adjoint Rule

**Definition.** For a conjugate-linear operator $S$ the **adjoint** $S^{\dagger}$ is the conjugate-linear operator defined by

$$
\varphi(S\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,S^{\dagger}\tilde Q_2)}
$$

for all $\tilde Q_1,\tilde Q_2$. For a linear operator $T$ the adjoint is defined by $\varphi(T\tilde Q_1,\tilde Q_2)=\varphi(\tilde Q_1,T^{\dagger}\tilde Q_2)$; the two rules differ by the conjugation, which is the twist that the conjugate-linear case requires.

**Proposition.** The adjoint is well defined, conjugate-linear in the operator, and involutive: $S^{\dagger\dagger}=S$; a conjugate-linear operator is **self-adjoint** when $S^{\dagger}=S$.

**Proof.** The definitions are those of *The Sesquilinear Adjoint Operator*, §*The Definition*, on the sesqualgebra $\mathbb{B}$ with the form $\varphi$; the existence and the uniqueness are the perfection of §*The Form*, and the involution follows by applying the definition twice and using the sesqui-symmetry.

**Remark.** The twist is not a convention but a necessity: a conjugate-linear operator cannot be self-adjoint under the linear rule unless it vanishes, exactly as a nonzero left multiplication cannot be $\mathbb{C}$-linear, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*. The two rules are the two parities of the operator theory read through the form.

### The General Theorem

**Theorem.** For the standard model $a\star x\star b=ax^{*}b$ of *The Sesquilinear Adjoint Operator*, the adjoint of the sandwich $S_{a,b}(x)=ax^{*}b$ is $S_{a,b}^{\dagger}=S_{b,a}$; for the ordinary two-sided multiplication $T_{p,q}(x)=pxq$ the adjoint is $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$.

**Proof.** These are the two computations of *The Sesquilinear Adjoint Operator*, §*The Sandwich and the Two-Sided Multiplication*, with the trace functional $\tau$ of that article read as the scalar part $\mathrm{Sc}$ here, the datum $(\mathbb{C},\varsigma)$ being the conjugation on the scalars; the compatibility $\mathrm{Sc}(\tilde Q_5^{*})=\overline{\mathrm{Sc}(\tilde Q_5)}$ and the centrality $\mathrm{Sc}(\tilde Q_5\tilde Q_4)=\mathrm{Sc}(\tilde Q_4\tilde Q_5)$ are the properties of the scalar part, and the pairings are perfect by §*The Form*.

**Remark.** The translation between the general notation and the notation of this batch is the placement of the star: in the general article the sandwich is $ax^{*}b$, while the batch writes the sandwich of *The Sesquilinear Sandwich on the Biquaternion* as $\tilde Q\tilde Q_1^{*}\tilde Q_3^{*}$, that is $S_{\tilde Q,\tilde Q_3}=S_{\tilde Q,\tilde Q_3^{*}}$ in the general notation, with the second parameter conjugated. The next section translates the general theorem accordingly.

## The Adjoint of the Sandwich

### The Main Identity

**Theorem (the adjoint of the sandwich).** For all $\tilde Q,\tilde Q_3$,

$$
\boxed{\;S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q^{*}}\;},
$$

that is, $(\tilde Q\star\cdot\star\tilde Q_3)^{\dagger}=\tilde Q_3^{*}\star\cdot\star\tilde Q^{*}$; explicitly,

$$
\varphi\bigl(\tilde Q\tilde Q_1^{*}\tilde Q_3^{*},\tilde Q_2\bigr)=\overline{\varphi\bigl(\tilde Q_1,\tilde Q_3^{*}\tilde Q_2^{*}\tilde Q\bigr)} .
$$

**Proof.** The general sandwich of *The Sesquilinear Adjoint Operator*, §*The Sandwich and the Two-Sided Multiplication*, is $S_{a,b}(x)=ax^{*}b$ with the adjoint $S_{b,a}$; the batch sandwich is $S_{\tilde Q,\tilde Q_3}=S_{\tilde Q,\tilde Q_3^{*}}$ in that notation, so the general theorem gives $S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q}$, and $S_{\tilde Q_3^{*},\tilde Q}$ is the batch sandwich with the first parameter $\tilde Q_3^{*}$ and the second parameter $\tilde Q^{*}$, that is $S_{\tilde Q_3^{*},\tilde Q^{*}}$ because the batch writes the second parameter already starred. The explicit display is the resulting computation in the coordinates.

**Remark.** The adjoint therefore stars the two parameters and exchanges them, and it is again a sandwich. Applied twice it returns the original, $S_{\tilde Q,\tilde Q_3}^{\dagger\dagger}=S_{\tilde Q,\tilde Q_3}$, so the adjoint is an involution on the sandwich family; it is conjugate-linear in the sandwich and it exchanges the two parameters, which is the operator form of the exchange of the two outer slots of the ternary product.

### The Exchange Identity

**Corollary (the identity that exchanges the two).** For all $\tilde Q,\tilde Q_3,\tilde Q_1,\tilde Q_2$,

$$
\varphi\bigl(S_{\tilde Q,\tilde Q_3}\tilde Q_1,\tilde Q_2\bigr)=\overline{\varphi\bigl(\tilde Q_1,S_{\tilde Q_3^{*},\tilde Q^{*}}\tilde Q_2\bigr)} ,
$$

and with the Hermitian adjoint written $S^{\dagger}$ the identity is the definition of the adjoint of §*The Twisted Adjoint Rule*.

**Proof.** Immediate from the theorem and the definition; the interest is that the sandwich of the adjoint parameters is again a sandwich, so the family is stable under the adjoint.

**Remark.** The stability is not automatic: the adjoint of an arbitrary conjugate-linear operator is not a sandwich, and the theorem says that the sandwich family is closed under the adjoint. This is the operator analogue of the closure of the Hermitian half under the symmetrised product, and it is the reason the ternary operators of the batch carry adjoints inside the batch.

### The Self-Adjoint Sandwiches

**Theorem (the self-adjoint criterion).** The sandwich $S_{\tilde Q,\tilde Q_3}$ is self-adjoint if and only if $S_{\tilde Q_3^{*},\tilde Q^{*}}=S_{\tilde Q,\tilde Q_3}$; in particular every sandwich with conjugate parameters is self-adjoint,

$$
S_{\tilde Q,\tilde Q^{*}}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}\tilde Q ,
$$

and for two invertible parameters the criterion is equivalent to $\tilde Q_3=\bar c\,\tilde Q^{*}$ for a nonzero complex number $c$, so that the self-adjoint sandwiches with invertible parameters are the conjugate pairs up to that scalar ambiguity.

**Proof.** By the main identity, $S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q^{*}}$, so self-adjointness is the equality $S_{\tilde Q_3^{*},\tilde Q^{*}}=S_{\tilde Q,\tilde Q_3}$. The conjugate pair satisfies it, because $(\tilde Q_3^{*},\tilde Q^{*})=(\tilde Q,\tilde Q^{*})$ when $\tilde Q_3=\tilde Q^{*}$. Conversely the equality of two sandwiches is the equality of two parametrised two-sided operators, and the kernel of the parametrisation is the group of the central units $\tilde Q_6=c\,e_t$, by *The Sesquilinear Sandwich on the Biquaternion*, §*The Invertible Sandwiches*; for invertible parameters the equality therefore reads $(\tilde Q_3^{*},\tilde Q^{*})=(\tilde Q\tilde Q_6,\tilde Q_3\tilde Q_6^{-1*})$ with $\tilde Q_6=c\,e_t$ a central unit, $c\in\mathbb{C}^{\times}$, that is $\tilde Q_3^{*}=c\tilde Q$ and $\tilde Q^{*}=\bar c^{-1}\tilde Q_3$, which is the single equation $\tilde Q_3=\bar c\,\tilde Q^{*}$.

**Remark.** The self-adjoint sandwiches are therefore the sandwiches of the conjugate pairs, and they are parametrised by the elements $\tilde Q$ of the algebra together with the scalar ambiguity $\tilde Q_3=\bar c\,\tilde Q^{*}$, a four-dimensional complex family of operators. The adjoint is an involution on the sandwich family, so the self-adjoint sandwiches are the fixed points of that involution. The involution $S_{e_t,e_t}={}^{*}$ is the case $\tilde Q=e_t$, and it is self-adjoint; the quadratic representation of the ternary product is the general case, by the next section.

## The Special Cases

### The Involution

**Proposition.** The involution is self-adjoint, ${}^{*\dagger}={}^{*}$, so

$$
\varphi(\tilde Q_1^{*},\tilde Q_2)=\overline{\varphi(\tilde Q_1,\tilde Q_2^{*})} .
$$

**Proof.** The involution is the sandwich $S_{e_t,e_t}$, and $S_{e_t,e_t}^{\dagger}=S_{e_t^{*},e_t^{*}}=S_{e_t,e_t}$ by the main identity.

**Remark.** The involution is the unique sandwich that is also a two-sided multiplication with the identity parameters, and its self-adjointness is the starting case of the criterion. In the model it is the Hermitian transpose, which is self-adjoint for the trace form, by *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model*.

### The One-Sided and the Two-Sided Multiplications

**Theorem.** For the left multiplication, the right multiplication and the ordinary two-sided multiplication,

$$
\boxed{\;L_{\tilde Q}^{\dagger}=S_{e_t,\tilde Q^{*}} , \qquad R_{\tilde Q_3}^{\dagger}=T_{e_t,\tilde Q_3} , \qquad T_{\tilde Q,\tilde Q_3}^{\dagger}=T_{\tilde Q^{*},\tilde Q_3^{*}}\;}.
$$

**Proof.** The left multiplication is the sandwich $S_{\tilde Q,e_t}$, so the main identity gives $L_{\tilde Q}^{\dagger}=S_{e_t,\tilde Q^{*}}$. The right multiplication is linear and equals $T_{e_t,\tilde Q_3^{*}}$, so the second display is the general theorem for the two-sided multiplication; the third display is the same theorem.

**Remark.** The left multiplication is conjugate-linear and its adjoint is a sandwich with a unit in the first slot; the operator $S_{e_t,\tilde Q^{*}}$ is the map $\tilde Q_1\mapsto\tilde Q_1^{*}\tilde Q$, which is neither a left nor a right multiplication, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*, and it is the mixed composite $R_{\tilde Q^{*}}L_{e_t}$. The right multiplication is linear and its adjoint is again an ordinary multiplication on the other side. This is the operator form of the asymmetry of the two sides that the one-sided unit produces.

### The Quadratic Representation

**Corollary.** The quadratic representation of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*,

$$
\tilde Q_2\longmapsto\tilde Q_3\tilde Q_2^{*}\tilde Q_3=S_{\tilde Q_3,\tilde Q_3^{*}}(\tilde Q_2) ,
$$

is self-adjoint for every $\tilde Q_3$.

**Proof.** The quadratic representation is the sandwich $S_{\tilde Q_3,\tilde Q_3^{*}}$, whose two parameters are conjugate to each other, so the self-adjoint criterion applies.

**Remark.** The self-adjointness of the quadratic representation is the operator form of the Hermitian symmetry $\{x,y,z\}^{*}=\{z^{*},y^{*},x^{*}\}$ of the ternary product: the symmetry exchanges the two outer slots, and the adjoint exchanges the two parameters, so the two exchanges are the same statement. The adjoint of the ternary product with arbitrary parameters is *The Adjoint of the Ternary Product*, where the same identity is developed for the general algebraic $J^{*}$-triple.

## The Matrix Model Interpretation

**Proposition.** In the model of *The Biquaternion Sesqualgebra in the $2\times2$ Matrix Model* the sandwich is $S_{A,B}(X)=AX^{\dagger}B^{\dagger}$ and the form is $\varphi(X,Y)=\tfrac12\mathrm{tr}(XY^{\dagger})$, with $A=\mathsf{M}_2(\tilde Q)$ and $B=\mathsf{M}_2(\tilde Q_3)$ the matrices of the two parameters; the adjoint of the sandwich is

$$
\boxed{\;S_{A,B}^{\dagger}(X)=B^{\dagger}X^{\dagger}A\;},
$$

which is the sandwich of the adjoint parameters, the two matrices exchanged and each read with the Hermitian transpose.

**Proof.** In the model the involution is the Hermitian transpose, so $\Phi(S_{\tilde Q_3^{*},\tilde Q^{*}}(\tilde Q_1))=\mathsf{M}_2(\tilde Q_3^{*})\mathsf{M}_2(\tilde Q_1)^{\dagger}\mathsf{M}_2(\tilde Q^{*})^{\dagger}=B^{\dagger}X^{\dagger}(A^{\dagger})^{\dagger}=B^{\dagger}X^{\dagger}A$, which is the display; the trace form is the standard form of the matrix algebra, for which the adjoint of $X\mapsto AX^{\dagger}B^{\dagger}$ is $X\mapsto B^{\dagger}X^{\dagger}A$ by the theorem.

**Remark.** The model makes the adjoint an explicit operation on the two outer factors: the adjoint of the sandwich with the matrices $A$ and $B$ is the sandwich with the two matrices exchanged and Hermitian-transposed, that is the sandwich of the matrices of the adjoint elements $\tilde Q_3^{*}$ and $\tilde Q^{*}$. This is the matrix form of the exchange of the two outer slots of the ternary product, and it is the same exchange that the identity of §*The Exchange Identity* performs on the parameters.

## Summary

With respect to the Hermitian form $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ the adjoint of the sandwich $S_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}\tilde Q_3^{*}$ is $S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q^{*}}$: the adjoint stars the two parameters and exchanges them, satisfies the identity $\varphi(S_{\tilde Q,\tilde Q_3}\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,S_{\tilde Q_3^{*},\tilde Q^{*}}\tilde Q_2)}$, and is an involution on the sandwich family. The self-adjoint sandwiches are the sandwiches with conjugate parameters, $S_{\tilde Q,\tilde Q^{*}}=\tilde Q(\cdot)^{*}\tilde Q$, and the involution $S_{e_t,e_t}={}^{*}$ and the quadratic representation $S_{\tilde Q_3,\tilde Q_3^{*}}$ of the ternary product are the two distinguished cases. The left multiplication has the adjoint $S_{e_t,\tilde Q^{*}}$, the right multiplication the adjoint $T_{e_t,\tilde Q_3}$, and the ordinary two-sided multiplication the adjoint $T_{\tilde Q^{*},\tilde Q_3^{*}}$. In the model the adjoint of $X\mapsto AX^{\dagger}B^{\dagger}$ is $X\mapsto B^{\dagger}X^{\dagger}A$, the two factors exchanged and conjugated, and the form is the trace pairing.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the Hermitian form, perfect and sesqui-symmetric |
| $\varphi(S\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,S^{\dagger}\tilde Q_2)}$ | the twisted adjoint rule for a conjugate-linear operator |
| $S_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1^{*}\tilde Q_3^{*}$ | the sandwich |
| $S_{\tilde Q,\tilde Q_3}^{\dagger}=S_{\tilde Q_3^{*},\tilde Q^{*}}$ | the adjoint of the sandwich |
| $\varphi(S_{\tilde Q,\tilde Q_3}\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,S_{\tilde Q_3^{*},\tilde Q^{*}}\tilde Q_2)}$ | the identity that exchanges the two parameters |
| $S_{\tilde Q,\tilde Q^{*}}=\tilde Q(\cdot)^{*}\tilde Q$ | the self-adjoint sandwiches with conjugate parameters |
| $S_{e_t,e_t}={}^{*}$ | the involution, self-adjoint |
| $S_{\tilde Q_3,\tilde Q_3^{*}}(\tilde Q_2)=\tilde Q_3\tilde Q_2^{*}\tilde Q_3$ | the quadratic representation, self-adjoint |
| $L_{\tilde Q}^{\dagger}=S_{e_t,\tilde Q^{*}}$ | the adjoint of the left multiplication |
| $R_{\tilde Q_3}^{\dagger}=T_{e_t,\tilde Q_3}$ | the adjoint of the right multiplication |
| $T_{\tilde Q,\tilde Q_3}^{\dagger}=T_{\tilde Q^{*},\tilde Q_3^{*}}$ | the adjoint of the ordinary two-sided multiplication |
| $S_{A,B}^{\dagger}(X)=B^{\dagger}X^{\dagger}A$ | the adjoint in the matrix model |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the adjoint of a semilinear operator with respect to a sesquilinear form over a ring with involution.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutive rings, the Hermitian forms they carry and the adjoints they define.
- Sterling K. Berberian, *Baer \*-Rings* (Springer, 1972), for the involution and the adjoint operation, and for the conjugation of the adjoint of a semilinear map.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the Hermitian forms, the adjoint operation and the triple products associated with them.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the conjugate transpose, the trace form and the adjoint of a matrix product.
