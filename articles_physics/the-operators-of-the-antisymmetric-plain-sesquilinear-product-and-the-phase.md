# __The Operators of the Antisymmetric Plain Sesquilinear Product and the Phase__

## Introduction

The APS band reads the antisymmetric plain sesquilinear product as the phase structure of the framework. The product is
$$
\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)=\tfrac12\bigl(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural}\bigr)=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr),
$$
the **vector part** of the plain sesquilinear product of the probability band, so that one value splits into two halves,
$$
\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q,
$$
the central half $\tilde P\circledast\tilde Q=H(\tilde P,\tilde Q)e_0$ read as a probability and the vector half read as a phase. The split of a sesquilinear product into a symmetric and an antisymmetric part, and the class of each part, are *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the operation itself, its conjugate-alternation and its algebraic norm are *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* and *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*. The mathematics of the block writes the operation $\diamond$; this article writes it $\wedge_{*}$, the mark of the physics band's companion articles.

This article carries the operator layer of the band: the multiplication operators of this product, the form they are adjoint for, the sandwich the band owns, and the consequences of the adjoint. It answers the question the twelve bands ask, and for this band the answer has the parity asymmetry of the probability band with a twist the probability band does not have. As there, the left multiplication is **conjugate-linear** and the right multiplication is **$\mathbb{C}$-linear**. What is new here is that the **antisymmetry** relates the two families: the right multiplication is the negative of the conjugate of the left one,
$$
R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}},
$$
the **conjugate-alternation** of the operation read on its operators, so that a single $\mathbb{C}$-linear **companion** carries the whole operator theory of the block. The composition of the operators does **not** close, and that failure is the operator form of the failure of the operation to be a Lie bracket.

The article is the sibling of *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*, the operator article of the GPA band, and of *The Operators of the Plain Sesquilinear Product and the Born Pairing*, the operator article of the probability band. It shares the sesquilinear parity of the second and the antisymmetric job of the first, and it carries one new object that neither owns: the **sandwich** of the sesquilinear theory, $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$, whose first factor is the block's left multiplication. Three questions organise the article. The first is the **parity**: which family conjugates, and how the antisymmetry identifies the two families. The second is the **sandwich**: the two-sided operator the band owns, its adjoint and its composition law. The third is the **failure**: the composition does not close, no Lie algebra is raised from the block's own operators, and the surviving derivations are a small algebra of another kind.

**Boundaries.** The operation, its conjugate-alternation and its algebraic norm are *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* and *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the pairing of the values is *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*; the one-sided operators, their invariants and the sandwich are *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*; the general sandwich is *The Sesquilinear Sandwich Operator* and its biquaternion instance *The Sesquilinear Sandwich on the Biquaternions*; the general adjoint is *The Sesquilinear Adjoint Operator* and the biquaternion instance *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*; the one-sided operators of the row are *The Left and Right Multiplications of the Biquaternion Sesqualgebra*. The physical phase interpretations are the band's two articles *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* and *Interference without a Lie Algebra: the Jacobi Failure in the State Space*; the physical phases themselves are *The Path Integral in Biquaternionic Form*, *The Double-Slit Experiment in Biquaternionic Form*, *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form*, *The Berry Phase and Geometric Phases in Biquaternionic Form* and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. The crossing comparison of the twelve rows is *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve.

**Conventions.** As in the companion articles and in *Conventions in the Biquaternion Universe*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central $i$ with $i^{2}=-1$; a general element is $\tilde Q=Q_0e_0+\vec Q$ with complex coefficients $Q_\mu$. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$; the coefficientwise conjugation $\overline{\cdot}$ conjugates the four coefficients; the Hermitian conjugation is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The scalar part is $\mathrm{Sc}(\tilde X)=X_0$, the vector part $\mathrm{Vect}=\mathrm{id}-\mathrm{Sc}$, the trace $\mathrm{Tr}=2\,\mathrm{Sc}$, and the Hermitian form $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$, positive definite of Gram matrix the identity. The row product is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ with left and right multiplications $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$; the ordinary two-sided multiplication is $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$; the sesquilinear sandwich is $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$. The sectors are $\mathbb{M}_{\pm}=\{\tilde Q^{*}=\pm\tilde Q\}$, the unitary slice is $U=\{\tilde U:\tilde U\tilde U^{*}=e_0\}$, the spinor module is $S=\mathbb{B}\tilde\Pi_+$ with $\tilde\Pi_+=\tfrac12(e_0+ie_3)$, and the state side is $\mathbb{M}_{+}$. Here $ie_3$ is a root of $+1$, $(ie_3)^2=e_0$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Two Multiplication Operators and Their Parity

The product carries one multiplication operator for each slot, and the two are not of the same kind.

**Definition (the multiplication operators of the block).** For $\tilde A\in\mathbb{B}$ the **left multiplication** and the **right multiplication** of the antisymmetric plain sesquilinear product are
$$
L^{\wedge_{*}}_{\tilde A}(\tilde X)=\tilde A\wedge_{*}\tilde X=\mathrm{Vect}\bigl(\tilde A\tilde X^{*}\bigr),
\qquad
R^{\wedge_{*}}_{\tilde A}(\tilde X)=\tilde X\wedge_{*}\tilde A=\mathrm{Vect}\bigl(\tilde X\tilde A^{*}\bigr),
$$
the biquaternion instance of the two multiplication operators of a sesqualgebra, *The Left and Right Multiplication Operators of a Sesqualgebra*, in the realisation of *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. Both are additive in the parameter and homogeneous of degree one, and both are injective for a nonzero parameter off the centre; they are the operators of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, whose notation writes the operation $\diamond$.

**Proposition (the vector part of the row multiplication).** For every $\tilde A$,
$$
L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A},
\qquad
R^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ R_{\tilde A},
$$
where $L_{\tilde A}$ and $R_{\tilde A}$ are the two one-sided multiplications of the general plain sesqualgebra, $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$, of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

*Proof.* The identity $\mathrm{Vect}(\tilde Y)=\tilde Y-\mathrm{Sc}(\tilde Y)e_0$ and the definitions; the block is the projection of the row onto its vector values.

**Read as a physical statement.** The block keeps the vector value and discards the central one, so its operators are the row's operators read through a projection. This is an interpretation: it says that the phase operator is the probability operator with the probability dropped, and it is why the two bands of one value have their operators built from the same pair.

**Theorem (the opposite parities).** For every $\lambda\in\mathbb{C}$ and every $\tilde X\in\mathbb{B}$,
$$
L^{\wedge_{*}}_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L^{\wedge_{*}}_{\tilde A}(\tilde X),
\qquad
L^{\wedge_{*}}_{\lambda\tilde A}=\lambda\,L^{\wedge_{*}}_{\tilde A},
\qquad
R^{\wedge_{*}}_{\tilde A}(\lambda\tilde X)=\lambda\,R^{\wedge_{*}}_{\tilde A}(\tilde X),
\qquad
R^{\wedge_{*}}_{\lambda\tilde A}=\overline{\lambda}\,R^{\wedge_{*}}_{\tilde A}.
$$
The left multiplication is conjugate-linear in the variable and $\mathbb{C}$-linear in the parameter; the right multiplication is $\mathbb{C}$-linear in the variable and conjugate-linear in the parameter.

*Proof.* The involution ${}^{*}$ is conjugate-linear and the coefficients are central, so $L^{\wedge_{*}}_{\tilde A}(\lambda\tilde X)=\mathrm{Vect}(\tilde A\overline{\lambda}\tilde X^{*})=\overline{\lambda}L^{\wedge_{*}}_{\tilde A}(\tilde X)$; the variable is read plainly on the right, so $R^{\wedge_{*}}_{\tilde A}(\lambda\tilde X)=\lambda R^{\wedge_{*}}_{\tilde A}(\tilde X)$. For the parameters, $\mathrm{Vect}(\lambda\tilde A\tilde X^{*})=\lambda L^{\wedge_{*}}_{\tilde A}(\tilde X)$ and $\mathrm{Vect}(\tilde X\overline{\lambda}\tilde A^{*})=\overline{\lambda}R^{\wedge_{*}}_{\tilde A}(\tilde X)$.

**Read as a physical statement.** The two slots of the phase pairing have opposite polarity, and the multiplication operators inherit it: attaching on the left conjugates the variable, attaching on the right conjugates the parameter. This is an interpretation, and it is the operator form of the statement that the phase is carried by the antisymmetric half of a sesquilinear pairing and not by a bilinear product.

**Theorem (the conjugate-alternation on the operators).** For every $\tilde A$,
$$
R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}},
\qquad\text{equivalently}\qquad
T^{\wedge_{*}}_{\tilde A}:=\overline{L^{\wedge_{*}}_{\tilde A}}=-R^{\wedge_{*}}_{\tilde A},
$$
where the bar is the coefficientwise conjugation of the value. The assignment $\tilde A\mapsto T^{\wedge_{*}}_{\tilde A}$ is the **companion**, it is $\mathbb{C}$-**linear** in the parameter, and the left operator is its conjugate, $L^{\wedge_{*}}_{\tilde A}=\overline{T^{\wedge_{*}}_{\tilde A}}$.

*Proof.* The conjugate-alternation of the operation gives $\tilde X\wedge_{*}\tilde A=-\overline{\tilde A\wedge_{*}\tilde X}=-\overline{L^{\wedge_{*}}_{\tilde A}(\tilde X)}$, which is the first display; the coefficientwise conjugation of a conjugate-linear operator is $\mathbb{C}$-linear, since the conjugation is conjugate-linear and the operator is conjugate-linear.

**Read as a physical statement.** The two families of the block are not independent: the right family is the negative of the mirror image of the left family, one mirror image apiece for the operation's conjugation. This is an interpretation of the conjugate-alternation, and it says that the phase operator has one handedness and that reading the other slot merely mirrors it.

**Corollary (a single companion carries the block).** Because $R^{\wedge_{*}}_{\tilde A}$ is the negative of the companion of $L^{\wedge_{*}}_{\tilde A}$, the whole operator theory of the block is the theory of the single $\mathbb{C}$-linear companion $T^{\wedge_{*}}_{\tilde A}=\overline{L^{\wedge_{*}}_{\tilde A}}$, the left and the right being recovered from it.

*Proof.* Immediate from the theorem; the companion is the honest linear object of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, whose characteristic polynomial is the characteristic polynomial of the real matrix of the left multiplication.

**Read as a physical statement.** The block needs a single linear operator to describe its action, where the row needs two. This is an interpretation: the price of the antisymmetry is the loss of a second independent family, and the gain is that a single matrix carries the phase operator's invariants.

**Proposition (the invariants of the left operator).** In the real basis $(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ the matrix $M_{\tilde A}$ of $L^{\wedge_{*}}_{\tilde A}$ has its two scalar rows zero, its **trace vanishes** for every $\tilde A$, its **rank** is six for a unit and four for a zero divisor, and its characteristic polynomial is even,
$$
\chi_{M_{\tilde A}}(\lambda)=\lambda^{2}P(\lambda),
$$
with $P$ an even polynomial of degree six. On the basis, $\chi_{M_{e_0}}=\lambda^{2}(\lambda^{2}-1)^{3}$, $\chi_{M_{e_k}}=\lambda^{4}(\lambda^{2}+1)^{2}$ and $\chi_{M_{e_1+ie_2}}=\lambda^{4}(\lambda^{2}+2)^{2}$. The kernel is $\ker L^{\wedge_{*}}_{\tilde A}=\{\tilde X:\tilde A\tilde X^{*}\in\mathbb{C}_{\mathbb{B}}\}$, the centre for $\tilde A=e_0$ and the complex line $\mathbb{C}e_k$ for $\tilde A=e_k$.

*Proof.* These are the coordinate rule, the kernel, the rank, the trace and the characteristic polynomial of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, computed in the real basis; the scalar rows vanish because the value is a vector part.

**Read as a physical statement.** The phase operator is traceless and it kills two directions, the centre when the parameter is the unit. This is an interpretation: the trace is the classical shadow of an operator, and a phase operator has none, which is another way to say that a phase is a relative datum and not a quantity.

## The Composition of the Operators

The composition of two operators of the block records exactly where the projection $\mathrm{Vect}$ intervenes twice, and the two conjugations of the row no longer cancel.

**Theorem (the composition laws).** For all $\tilde A,\tilde B\in\mathbb{B}$ and every $\tilde X$,
$$
L^{\wedge_{*}}_{\tilde A}L^{\wedge_{*}}_{\tilde B}(\tilde X)=\mathrm{Vect}\bigl(\tilde A\tilde X\tilde B^{*}\bigr)-\overline{H(\tilde B,\tilde X)}\,\mathrm{Vect}(\tilde A),
$$
$$
R^{\wedge_{*}}_{\tilde A}R^{\wedge_{*}}_{\tilde B}(\tilde X)=\mathrm{Vect}\bigl(\tilde X\tilde B^{*}\tilde A^{*}\bigr)-H(\tilde X,\tilde B)\,\mathrm{Vect}(\tilde A^{*}),
$$
the two laws of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*.

*Proof.* For the left law, write $\tilde B\tilde X^{*}=H(\tilde B,\tilde X)e_0+L^{\wedge_{*}}_{\tilde B}(\tilde X)$, so that $\tilde A\tilde X\tilde B^{*}=\tilde A(\tilde B\tilde X^{*})^{*}=H(\tilde B,\tilde X)\tilde A+\tilde A\,L^{\wedge_{*}}_{\tilde B}(\tilde X)^{*}$, and apply $\mathrm{Vect}$ using that $L^{\wedge_{*}}_{\tilde B}(\tilde X)$ is a vector; the right law is the same computation with the two sides exchanged.

**Read as a physical statement.** The composite of two phase operators is not a phase operator: the projection leaves a scalar defect proportional to the alignment $H(\tilde B,\tilde X)$ of the parameter and the argument. This is an interpretation, and it says that two phase operations do not compose into a third, the obstruction being the central alignment that the block has already discarded.

**Corollary (no multiplicativity, no monoid).** Neither family is multiplicative: $L^{\wedge_{*}}_{\tilde A}L^{\wedge_{*}}_{\tilde B}\neq L^{\wedge_{*}}_{\tilde A\wedge_{*}\tilde B}$ and likewise on the right. The block therefore has **no monoid of one-sided operators and no regular representation**.

*Proof.* The witness is $\tilde A=\tilde B=e_1$, $\tilde X=e_2$: the composite sends $e_2$ to $-e_2$, since $L^{\wedge_{*}}_{e_1}(e_2)=-e_3$ and $L^{\wedge_{*}}_{e_1}(-e_3)=-e_2$, while $L^{\wedge_{*}}_{e_1\wedge_{*}e_1}=L^{\wedge_{*}}_{0}=0$; the failure is the general one of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*.

**Read as a physical statement.** The phase operators do not form a semigroup, so there is no regular representation to speak of and no algebra generated by the multiplications. This is an interpretation: the phase structure composes nowhere, not merely on one side, against the probability band which composes on one side.

**Remark (the contrast with the row).** For the general plain sesqualgebra the two composites close, $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$ and $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*. The block is the projection $\mathrm{Vect}$ of each of those operators, the projection is not an algebra map, and the correction terms $-\overline{H(\tilde B,\tilde X)}\mathrm{Vect}(\tilde A)$ and $-H(\tilde X,\tilde B)\mathrm{Vect}(\tilde A^{*})$ are what the second application of the projection leaves behind.

**Corollary (the companion composes into the right family).** Since $T^{\wedge_{*}}_{\tilde A}=-R^{\wedge_{*}}_{\tilde A}$, the companions compose as $T^{\wedge_{*}}_{\tilde A}T^{\wedge_{*}}_{\tilde B}=R^{\wedge_{*}}_{\tilde A}R^{\wedge_{*}}_{\tilde B}$, so the $\mathbb{C}$-linear companion family composes into the right family and not into itself, and the companion is not multiplicative either.

*Proof.* The first display of the theorem and the definition of the companion.

**Read as a physical statement.** The one linear object of the block does not reproduce itself; it composes into the other family. This is an interpretation of the failure of a single linear representation, the subject of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*.

## The Sandwich of the Block

The block is the vector part of the row, and the two-sided operator one degree above the row is the object the band owns.

**Definition (the sandwich).** For $\tilde P,\tilde Q\in\mathbb{B}$ the **sesquilinear sandwich** is
$$
S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\star\tilde X\star\tilde Q=\tilde P\tilde X^{*}\tilde Q^{*}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*},
$$
the two-sided operator of the product, of *The Sesquilinear Sandwich on the Biquaternions* and, in general form $S_{a,b}(x)=ax^{*}b$, of *The Sesquilinear Sandwich Operator*. It is conjugate-linear in the middle variable, $\mathbb{C}$-linear in the first parameter and conjugate-linear in the second, and the block's left multiplication is its first special case,
$$
S_{\tilde A,e_0}=L_{\tilde A},
\qquad
L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0},
\qquad
S_{\tilde A,\tilde B}=R_{\tilde B}\circ L_{\tilde A}.
$$

*Proof.* The definition, the involution in the middle, and the two identities $T_{\tilde P,\tilde Q^{*}}\circ{}^{*}=S_{\tilde P,\tilde Q}$ and $R_{\tilde Q}L_{\tilde P}=S_{\tilde P,\tilde Q}$ of *The Sesquilinear Sandwich on the Biquaternions*, §*The Sandwich*, with the parameters read in the order of the display.

**Read as a physical statement.** The sandwich is the two-sided completion of the one-sided phase operators, and the block's operator is the sandwich with the unit in the second slot, projected onto the vector values. This is an interpretation: the phase operator is one end of a two-sided operation, and the other end is what makes the operation two-sided.

**Theorem (the composition table).** For all $\tilde A,\tilde B,\tilde C,\tilde D,\tilde P,\tilde Q$,
$$
S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\ \tilde A^{*}\tilde D^{*}},
\qquad
T_{\tilde P,\tilde Q}S_{\tilde A,\tilde B}=S_{\tilde P\tilde A,\ \tilde Q^{*}\tilde B},
$$
$$
S_{\tilde C,\tilde D}T_{\tilde P,\tilde Q}=S_{\tilde C\tilde Q^{*},\ \tilde D\tilde P},
\qquad
S_{\tilde A,\tilde B}^{2}=T_{\tilde A\tilde B,\ \tilde A^{*}\tilde B^{*}},
$$
the composition table of *The Sesquilinear Sandwich on the Biquaternions*, §*The Two Families Together*, in the convention of the batch that writes the second parameter already starred; the general table of *The Sesquilinear Sandwich Operator* is transported to it by the substitution $S_{\tilde P,\tilde Q}=S_{\tilde P,\tilde Q^{*}}$. The sandwiches and the two-sided multiplications together form a monoid under composition with identity $T_{e_0,e_0}=\mathrm{id}$, in which the sandwiches are the conjugate-linear elements and the two-sided multiplications the linear ones.

*Proof.* The first law is the direct computation $S_{\tilde C,\tilde D}(S_{\tilde A,\tilde B}(\tilde X))=\tilde C(\tilde A\tilde X^{*}\tilde B^{*})^{*}\tilde D^{*}=\tilde C\tilde B\tilde X\tilde A^{*}\tilde D^{*}$; the others are the same computation with one involution and one two-sided multiplication in each order, and the last display is $S_{\tilde A,\tilde B}^{2}$ of *The Sesquilinear Sandwich on the Biquaternions*, §*The Square and the Involution*.

**Read as a physical statement.** The composite of two sandwiches is a linear two-sided multiplication, so two conjugate-linear phase operators compose into a linear one: the parity is multiplicative and the conjugation cancels in pairs. This is an interpretation, and it says that a doubled phase operation is a phase-free transport.

**Theorem (the adjoint of the sandwich).** For all $\tilde P,\tilde Q$ and with $H$ the Hermitian form,
$$
S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}},
\qquad\text{explicitly}\qquad
H\bigl(S_{\tilde P,\tilde Q}\tilde X,\tilde Y\bigr)=\overline{H\bigl(\tilde X,S_{\tilde Q^{*},\tilde P^{*}}\tilde Y\bigr)},
$$
so the adjoint **stars the two parameters and exchanges them**, and it is an involution on the sandwich family.

*Proof.* This is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, §*The Main Identity*; the general theorem is $S_{a,b}^{\dagger}=S_{b,a}$ of *The Sesquilinear Adjoint Operator*, whose second parameter is conjugated in the notation of this batch.

**Read as a physical statement.** Transporting a two-sided phase operation across the Hermitian form exchanges its two ends and conjugates both parameters, so the sandwich and its mirror image are adjoint. This is an interpretation of the operator form of the exchange of the two outer slots of the ternary product.

**Corollary (the self-adjoint sandwiches).** The sandwich $S_{\tilde P,\tilde Q}$ is self-adjoint if and only if $S_{\tilde Q^{*},\tilde P^{*}}=S_{\tilde P,\tilde Q}$; in particular **every sandwich with conjugate parameters is self-adjoint**,
$$
S_{\tilde P,\tilde P^{*}}(\tilde X)=\tilde P\tilde X^{*}\tilde P,
$$
and for two invertible parameters the criterion is $\tilde Q=\bar c\,\tilde P^{*}$ for a nonzero complex number $c$. No nonzero sandwich is skew-adjoint.

*Proof.* The criterion is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, §*The Self-Adjoint Sandwiches*, with the kernel of the parametrisation the central units; the conjugate pair satisfies it because $(\tilde Q^{*},\tilde P^{*})=(\tilde P,\tilde P^{*})$ when $\tilde Q=\tilde P^{*}$. For the skew class, $-S_{\tilde P,\tilde Q}=S_{-\tilde P,\tilde Q}$, so a skew-adjoint sandwich reads $S_{\tilde Q^{*},\tilde P^{*}}=S_{-\tilde P,\tilde Q}$, which by the same kernel gives $\tilde Q^{*}=-c\tilde P$ and $\tilde P^{*}=\bar c^{-1}\tilde Q$, that is $\tilde Q=\bar c\tilde P^{*}$ and $\tilde Q=-\bar c\tilde P^{*}$ at once; hence $\bar c\tilde P^{*}=0$, impossible for a nonzero sandwich.

**Read as a physical statement.** The self-adjoint two-sided phase operators are exactly the quadratic representations $\tilde X\mapsto\tilde P\tilde X^{*}\tilde P$ of the ternary product, and among them the sandwich of a unitary parameter and its conjugate is the reflection of the block. This is a reading, and it is the operator form of the Hermitian symmetry of the ternary product.

## The Form and the Adjoint: the Side Is Kept and the Parameter Conjugated

The block has a positive definite form, its scalar part before the projection, and the adjoint is taken for it.

**The form.** The **Hermitian form** is
$$
H(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)=\sum_{\mu=0}^{3}P_{\mu}\overline{Q_{\mu}},
$$
$\mathbb{C}$-linear in the first argument and conjugate-linear in the second, of Gram matrix the identity in the basis $e_0,e_1,e_2,e_3$, and **positive definite**. It is the form of the probability band, the canonical Hermitian form of the regular module, *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*, and it is the same form as $\varphi=\mathrm{Sc}(\tilde X\tilde Y^{*})$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

**Definition (the adjoint).** For a $\mathbb{C}$-linear operator $T$ the **adjoint** is defined by $H(T\tilde P,\tilde Q)=H(\tilde P,T^{\dagger}\tilde Q)$ for all $\tilde P,\tilde Q$. For a conjugate-linear operator $S$ the linear rule has no solution, and the **twisted adjoint** is used instead,
$$
H\bigl(S\tilde P,\tilde Q\bigr)=\overline{H\bigl(\tilde P,S^{\dagger}\tilde Q\bigr)},
$$
under which the adjoint of a conjugate-linear operator is again conjugate-linear. Both rules are *The Sesquilinear Adjoint Operator*; the form is positive definite, hence non-degenerate, so the adjoint exists and is unique.

**Theorem (the adjoint of the two families).** For every $\tilde A\in\mathbb{B}$,
$$
\bigl(L^{\wedge_{*}}_{\tilde A}\bigr)^{\dagger}(\tilde Y)=\bigl(\mathrm{Vect}(\tilde Y)\bigr)^{*}\tilde A,
\qquad
\bigl(R^{\wedge_{*}}_{\tilde A}\bigr)^{\dagger}(\tilde Y)=\bigl(\mathrm{Vect}(\tilde Y)\bigr)\tilde A .
$$
The right family **keeps the side and conjugates the parameter**: $R^{\wedge_{*}}_{\tilde A}$ attaches the star of the parameter on the right, and its adjoint attaches the parameter itself on the right. The left family does **not** keep its family: its twisted adjoint is a sandwich, $S_{e_0,\tilde A^{*}}$ preceded by the projection.

*Proof.* The projection $\mathrm{Vect}$ is self-adjoint for $H$, $H(\mathrm{Vect}\tilde X,\tilde Y)=H(\tilde X,\mathrm{Vect}\tilde Y)$, because the scalar and the vector directions are orthogonal and the form is diagonal in the basis; with $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A}$ and $(L_{\tilde A})^{\dagger}=S_{e_0,\tilde A^{*}}$ this gives $(L^{\wedge_{*}}_{\tilde A})^{\dagger}=S_{e_0,\tilde A^{*}}\circ\mathrm{Vect}$, which is $(\mathrm{Vect}\tilde Y)^{*}\tilde A$. For the right family, $(R_{\tilde A})^{\dagger}=R_{\tilde A^{*}}$ with $R_{\tilde A^{*}}(\tilde Y)=\tilde Y\tilde A$, so $(R^{\wedge_{*}}_{\tilde A})^{\dagger}=R_{\tilde A^{*}}\circ\mathrm{Vect}$, which is $(\mathrm{Vect}\tilde Y)\tilde A$.

**Read as a physical statement.** Transporting a phase operation across the Hermitian form conjugates its parameter and does not move it to the other side; a right attachment stays a right attachment. This is an interpretation of a proof, and it is the physical hermiticity that the phase operators inherit from the probability band: the parameter is read as a phase, and the adjoint reverses it. The left attachment is the exception, its adjoint leaving the family for a two-sided operation.

**Corollary (the contrast with the composition band).** The adjoint of this band is a **Hermitian adjoint** for a positive definite form: it conjugates the parameter and keeps the side. The adjoint of the composition band is a **transpose** for the indefinite plain bilinear form: it keeps the parameter and swaps the sides, $(L_{\tilde A})^{\approx}=R_{\tilde A}$, of *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich*. The block-by-block comparison is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve.

**Read as a physical statement.** Two adjoints of one framework point in opposite directions: the phase adjoint reverses a phase in place, the material adjoint exchanges the sides and leaves the parameter. This is an interpretation of the pair of blocks.

## The Types of the Operators: Self-Adjoint, Skew-Adjoint and Unitary

The type criteria, as in the probability band, are criteria on the parameter; what changes is that no one-sided operator of the block can be unitary, because the projection has a kernel.

**Theorem (the one-sided types).** For $\tilde A\in\mathbb{B}$,
$$
L^{\wedge_{*}}_{\tilde A}\ \text{twisted-self-adjoint}\iff\tilde A\in\mathbb{C}_{\mathbb{B}},
\qquad
L^{\wedge_{*}}_{\tilde A}\ \text{twisted-skew-adjoint}\iff\tilde A=0,
$$
and the same two criteria hold for the right multiplication $R^{\wedge_{*}}_{\tilde A}$ under the ordinary rule. Neither $L^{\wedge_{*}}_{\tilde A}$ nor $R^{\wedge_{*}}_{\tilde A}$ is ever an isometry of $H$ for a nonzero parameter.

*Proof.* By the adjoint theorem, twisted-self-adjointness of $L^{\wedge_{*}}_{\tilde A}$ reads $(\mathrm{Vect}\tilde Y)^{*}\tilde A=\mathrm{Vect}(\tilde A\tilde Y^{*})$ for every $\tilde Y$; at $\tilde Y=e_0$ this forces $\mathrm{Vect}(\tilde A)=0$, and then the identity is centrality; for the right multiplication self-adjointness reads $(\mathrm{Vect}\tilde Y)\tilde A=\mathrm{Vect}(\tilde Y\tilde A^{*})$, which at $\tilde Y=e_0$ forces $\mathrm{Vect}(\tilde A^{*})=0$, that is centrality. Skew-adjointness at $\tilde Y=e_0$ gives $\mathrm{Vect}(\tilde A)=0$, and then the sign cannot reverse unless $\tilde A=0$. The isometry statements are the ranks six and four of the invariants proposition, a non-invertible operator being no isometry of a definite form.

**Read as a physical statement.** The only self-adjoint one-sided phase operator is the central one, which is a multiple of the projection times its parameter, and no one-sided phase operator is an isometry. This is an interpretation: observables and isometries do not live in this family, because the phase is projectively defined and the projection is not injective.

**Theorem (the sandwich types).** Let $\tilde P\in\mathbb{B}$ be nonzero. Then $S_{\tilde P,\tilde Q}$ is self-adjoint exactly when $\tilde Q$ is a conjugate of $\tilde P$ up to a central phase, the conjugate pairs $S_{\tilde P,\tilde P^{*}}$ being the self-adjoint family, and $S_{\tilde P,\tilde Q}$ is skew-adjoint only when it vanishes. For a **unitary** parameter $\tilde u\in U$ the sandwiches
$$
S_{\tilde u,\tilde u^{*}}\ \text{is self-adjoint and unitary},
\qquad
S_{\tilde u,\tilde u}\ \text{is the inner involution}\ \sigma_{\tilde u}(\tilde X)=\tilde u\tilde X^{*}\tilde u^{*}.
$$

*Proof.* The self-adjoint criterion is the corollary of the sandwich section; the skew class is empty by the same corollary. For unitary $\tilde u$, $S_{\tilde u,\tilde u^{*}}^{\dagger}=S_{\tilde u,\tilde u^{*}}$ by the criterion, and $H(S\tilde X,S\tilde Y)=\overline{H(\tilde X,\tilde Y)}$ because $S$ is conjugate-linear and $\tilde u$ is unitary, so $S$ is unitary in the twisted sense; $S_{\tilde u,\tilde u}(\tilde X)=\tilde u\tilde X^{*}\tilde u^{*}$ is by definition the inner involution.

**Read as a physical statement.** The two-sided phase operators that are observables are the quadratic representations, and the unitary ones are the squared amplitudes; the two-sided operators that are isometries are exactly those of the unitary slice, and they preserve the form up to the conjugation that a conjugate-linear map must carry. This is an interpretation of the pair of criteria.

## The Symmetries of the Form and of the Product

The symmetries split, as in every band, into the isometries of the form and the automorphisms of the product.

**Theorem (the isometries of the form).** The complex-linear transformations
$$
T_R\bigl(Q_0e_0+\vec U+i\vec V\bigr)=Q_0e_0+R\vec U+iR\vec V,
\qquad
R^{\mathsf T}R=I,\ \det R=1,
$$
acting on the complex vector subspace by the same real orthogonal matrix of determinant one in both real components, **preserve the form $H$ and the product $\wedge_{*}$**, and are exactly the $\mathbb{C}$-linear automorphisms of the block that preserve $H$. The coefficientwise conjugation $\overline{\cdot}$ preserves $\wedge_{*}$ as well, and it is a **twisted** isometry, $H(\overline{\tilde X},\overline{\tilde Y})=\overline{H(\tilde X,\tilde Y)}$.

*Proof.* The form is the Euclidean square of the eight real coordinates, and $T_R$ acts on the two real vector components by the same orthogonal $R$, so it is an isometry; it preserves the dot and the cross products of the vector parts, hence the product, by the structure-group theorem of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, §*The Structure Group*, which also proves that the linear automorphisms of the block are exactly these and that the conjugation is the only other one, conjugate-linear. The conjugation preserves the block by the proposition of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, §*Conjugate-Alternation*, and it reverses the form because $H(\overline{\tilde X},\overline{\tilde Y})=\overline{H(\tilde X,\tilde Y)}$.

**Read as a physical statement.** The compact rotations of the material frame are the isometries of the phase form, and the conjugation is the mirror that preserves the phase and reverses the form. This is an interpretation: the phase structure has a rotation symmetry and a reflection, and it has no boost isometry, because the block reads only the vector directions.

**Theorem (the multiplicative operators).** The block's own one-sided operators are **not** multiplicative, $L^{\wedge_{*}}_{\tilde A}L^{\wedge_{*}}_{\tilde B}\neq L^{\wedge_{*}}_{\tilde A\wedge_{*}\tilde B}$; the multiplicative operators of the block are the **structure group**, which contains the coefficientwise conjugation and the transformations $T_R$, and it does not contain the natural conjugation.

*Proof.* The failure of multiplicativity is the corollary of the composition section; the structure group is *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, §*The Structure Group*, whose theorem lists the two kinds of elements and proves that the natural conjugation reverses the cross term on the witness $(e_1,e_2)$.

**Read as a physical statement.** The product is preserved by a rotation of the vector frame and by a conjugation, and by nothing that moves the centre; and the product's own operators preserve it not at all. This is an interpretation, and it says that the phase structure is a vector structure with a mirror, not a transformation group of one algebra.

**Corollary (the derivations).** For a **real** vector $\vec a=\sum_k a_ke_k$ the operator
$$
D_{\vec a}(\tilde X)=[0,\ \vec a\times\tilde{\vec X}]
$$
is a derivation of the block, and these are exactly the derivations; they form the three-dimensional real Lie algebra
$$
[D_{\vec a},D_{\vec b}]=D_{\vec a\times\vec b},
$$
isomorphic to $\mathbb{R}^{3}$ with the cross product; it is the Lie algebra of the identity component of the structure group.

*Proof.* The Leibniz defect vanishes exactly for a real $\vec a$, and the bracket is the vector triple identity, of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, §*The Derivations*.

**Read as a physical statement.** The infinitesimal symmetry of the phase structure is the cross product with a real vector, the algebra of the rotations of the material frame, and the central direction is dead. This is an interpretation, and it locates the block's only Lie algebra in the rotations of the vector part and not in its own multiplication.

## The Operators Acting on the State Space: the Bloch Vector as the Phase

The operators act on the state side, and there the block's value is the coherence of a state.

**The state space.** The state side is the **Hermitian subspace** $\mathbb{M}_{+}$, whose generic element is $\tilde\rho=\tfrac12(e_0+i\vec r)$ with $\vec r$ real, of $H(\tilde\rho,\tilde\rho)=\tfrac14(1+\lvert\vec r\rvert^{2})$, on the trace-one slice the **Bloch ball**; its pure elements are the idempotents $\tilde\Pi_{\pm}(\hat{\mu})=\tfrac12(e_0\pm i\hat{\mu})$, the states of *The Bloch Ball as the Trace-One Slice of the Future Light Cone* and *Mass, Rank and the Positivity of the Dagger*. The spinor module on which the algebra acts is $S=\mathbb{B}\tilde\Pi_+$, *The Spinor Space as a Module and as a Hilbert Space*.

**Proposition (the algebraic norm is the Bloch vector).** For a state $\tilde\rho=\tfrac12(e_0+i\vec r)$ on the state side, $\tilde\rho^{*}=\tilde\rho$, and the block's value at the two equal arguments is
$$
\tilde\rho\wedge_{*}\tilde\rho=\mathrm{Vect}\bigl(\tilde\rho\tilde\rho^{*}\bigr)=\tfrac12\,i\vec r,
$$
the **Bloch vector** of the state, while the companion band's value on the same algebraic norm is the purity $\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0$.

*Proof.* The idempotence of the Hermitian square gives $\tilde\rho\tilde\rho^{*}=\tilde\rho^{2}=\tfrac14(1+\lvert\vec r\rvert^{2})e_0+\tfrac12 i\vec r$, whose vector part is $\tfrac12 i\vec r$; the companion statement is the symmetric half of the same value.

**Read as a physical statement.** On a state the phase operator returns the state's coherence direction; the probability half returns the purity. This is an interpretation of *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*, where the same display is the state-side statement of the phase: one value, one state, a central number and an imaginary vector.

**Corollary (how the operators act).** On the state side the block's left multiplication is the map
$$
L^{\wedge_{*}}_{\tilde A}(\tilde\rho)=\mathrm{Vect}\bigl(\tilde A\tilde\rho^{*}\bigr)=\mathrm{Vect}\bigl(\tilde A\tilde\rho\bigr),
$$
which reads a state through the parameter and keeps the vector part, so its scalar coordinate is zero and its image lies in $\mathrm{Vect}(\mathbb{B})$, the vector subspace; the right multiplication is its conjugate-alternated mirror, $R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}}$. On the pure states the value is purely imaginary, while the pairing of two distinct states carries a real part as well.

*Proof.* The first display is the definition and the Hermiticity of a state; the purity of the imaginary character at the two equal arguments, and its failure away from the two equal arguments, are *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*, §*The Value*.

**Read as a physical statement.** The state-side phase operator reads the parameter against a state and returns a vector, and it never returns a central number, because a phase is not a scalar. This is an interpretation; the operators do not measure a phase, they produce the vector a phase is read from.

## The Sandwich and the Inner Involution

The framework attaches a conjugation to a unitary element in two ways, and the two agree on the states.

**Proposition (two parametrisations of one conjugation).** For every unitary $\tilde u\in U$,
$$
S_{\tilde u,\tilde u}(\tilde X)=\tilde u\tilde X^{*}\tilde u^{*}=\sigma_{\tilde u}(\tilde X),
\qquad
S_{\tilde u,\tilde u^{*}}(\tilde X)=\tilde u\tilde X^{*}\tilde u ,
$$
the **inner involution** $\sigma_{\tilde u}$ of the algebra and the **reflection** of the block. The two agree exactly when $\tilde u^{*}=\tilde u$, that is on the Hermitian unitary parameters, and there alone.

*Proof.* The displays are the definition of $S_{\tilde P,\tilde Q}$ at the two parameters and the unitary identity $\tilde u^{*}=\tilde u^{-1}$; the agreement is the coincidence of the two right parameters.

**Read as a physical statement.** The inner involution conjugates by the conjugate of a unitary and the reflection by the unitary itself, and the two merge on the Hermitian unitary elements, the central signs $\pm e_0$ and the pure imaginary unit vectors $i\hat v$, and there alone. This is an interpretation of the block's two conjugations.

**Theorem (the involution is not an automorphism of the block).** The inner involution $\sigma_{\tilde u}$ is a **conjugate-linear anti-automorphism of the algebra**, $\sigma_{\tilde u}(\tilde X\tilde Y)=\sigma_{\tilde u}(\tilde Y)\sigma_{\tilde u}(\tilde X)$, and it is **not** an automorphism of the antisymmetric product for a general unitary $\tilde u$, the automorphisms of the block being the structure group of the previous section.

*Proof.* The anti-automorphism property is $\tilde u(\tilde X\tilde Y)^{*}\tilde u^{*}=\tilde u\tilde Y^{*}\tilde X^{*}\tilde u^{*}=(\tilde u\tilde Y^{*}\tilde u^{*})(\tilde u\tilde X^{*}\tilde u^{*})$; the failure of automorphy is the theorem of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, §*The Structure Group*, whose list of automorphisms contains the coefficientwise conjugation and the $T_R$ and does not contain $\sigma_{\tilde u}$.

**Read as a physical statement.** The unitary sandwich mirrors the algebra order and does not preserve the phase product, so it is a symmetry of the form and not of the product. This is an interpretation: the isometry of the phase form and the automorphism of the phase product are different groups, and the rotations $T_R$ are the only operators that are both, the conjugation being an automorphism of the product and a twisted isometry of the form.

**Corollary (the agreement on the state side).** The inner involution and the linear inner automorphism $\mathrm{Ad}_{\tilde u}(\tilde X)=\tilde u\tilde X\tilde u^{*}$ agree on the Hermitian subspace, the state side:
$$
\sigma_{\tilde u}(\tilde X)=\mathrm{Ad}_{\tilde u}(\tilde X)\quad\text{for every }\tilde X\in\mathbb{M}_{+},
$$
and there alone.

*Proof.* The two operators differ by the involution in the middle, $\sigma_{\tilde u}=\mathrm{Ad}_{\tilde u}\circ{}^{*}$, so they agree exactly on the fixed points of ${}^{*}$, which are $\mathbb{M}_{+}$.

**Read as a physical statement.** On a state, the mirror conjugation and the ordinary one are the same operation, and off the states they separate. This is an interpretation, and it says that the phase action on a state is unambiguous, the ambiguity of the block's two conjugations being invisible to the state side.

## The Failure of the Closure: No Lie Structure on the Operators

The composition of the operators does not close, and the operation itself supplies no bracket; both failures are one.

**Proposition (what fails).** The block's one-sided operators are not multiplicative, so the composite of two of them is not an operator of the block and the families generate no monoid; and the operation $\wedge_{*}$ fails the Jacobi identity, so no Lie bracket is raised from the block's own product. The cyclic sum
$$
\mathrm{cyc}\,\wedge_{*}(\tilde X,\tilde Y,\tilde Z)=\wedge_{*}\bigl(\wedge_{*}(\tilde X,\tilde Y),\tilde Z\bigr)+\wedge_{*}\bigl(\wedge_{*}(\tilde Y,\tilde Z),\tilde X\bigr)+\wedge_{*}\bigl(\wedge_{*}(\tilde Z,\tilde X),\tilde Y\bigr)
$$
does not vanish. At the real triple $(e_0,e_1,e_2)$ its value is $e_3\neq0$, and at the conjugated triple $(e_1,e_1,ie_2)$ it is $-2ie_2$.

*Proof.* The witness of the failure of multiplicativity is the composition corollary; the cyclic sum is computed from the basis table $e_0\wedge_{*}e_1=-e_1$, $e_1\wedge_{*}e_2=-e_3$, $e_2\wedge_{*}e_0=e_2$, $e_2\wedge_{*}e_1=e_3$, of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*, where the failure and its mechanism are owned.

**Read as a physical statement.** The phase structure carries no symmetry algebra of its own. This is an interpretation of the sibling article of the band, *Interference without a Lie Algebra: the Jacobi Failure in the State Space*, where the failure is read as the statement that an interference term is a relational datum and not an infinitesimal transformation.

**Remark (what survives).** The multiplication does not close and the bracket does not close, and the block keeps two structures of another kind: the **Hermitian form** $H$, positive definite on the values, so the phase vector has a definite length even though it names no symmetry; and the **derivation algebra** $\mathbb{R}^{3}$ of the real cross products, which is a Lie algebra but not one raised from the block's own operators. The pairing of the values, conjugate-linear in the last two slots and definite, is *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*; its interpretations are the sibling's.

**Read as a physical statement.** The form survives where the algebra does not, and the one Lie algebra of the block is the rotation algebra of the material frame, not a phase algebra. This is an interpretation; it is the exact boundary between what the phase structure is and what it is not.

## A Worked Case

Take first a **state** parameter,
$$
\tilde\rho=\tfrac12\bigl(e_0+ie_1\bigr),\qquad
\tilde\rho^{*}=\tilde\rho\in\mathbb{M}_{+},\qquad
H(\tilde\rho,\tilde\rho)=\tfrac12,\qquad
\tilde\rho\wedge_{*}\tilde\rho=\tfrac12\,ie_1 .
$$
The value is the Bloch vector, and the left operator reads the state through itself,
$$
L^{\wedge_{*}}_{\tilde\rho}(\tilde\rho)=\mathrm{Vect}\bigl(\tilde\rho\tilde\rho^{*}\bigr)=\tfrac12\,ie_1 .
$$
The two halves of the same value separate on this state: the companion band gives the purity $\tilde\rho\circledast\tilde\rho=\tfrac12\mathrm{Tr}(\tilde\rho^{2})e_0=\tfrac12 e_0$, and the phase band gives the coherence direction $\tfrac12 ie_1$.

Take next a **phase pair**,
$$
\tilde P=e_0+ie_1,\qquad \tilde Q=e_0+e_1,\qquad
H(\tilde P,\tilde Q)=1+i,\qquad
\tilde P\wedge_{*}\tilde Q=(-1+i)e_1 .
$$
The Hermitian form has a real part $1$, the alignment of the two amplitudes, and an imaginary part $1$, the relative phase; the value of the operation is a pure vector, and the sandwich on the unit splits into the two halves of the parent value,
$$
S_{\tilde P,\tilde Q}(e_0)=\tilde P\tilde Q^{*}=(1+i)e_0+(-1+i)e_1 .
$$
The conjugate sandwich is self-adjoint, $S_{\tilde P,\tilde P^{*}}^{\dagger}=S_{\tilde P,\tilde P^{*}}$, and on the unit it is the square of the parameter, $S_{\tilde P,\tilde P^{*}}(e_0)=\tilde P^{2}=2e_0+2ie_1$.

Take finally the **composition witness**,
$$
\tilde A=\tilde B=e_1,\qquad \tilde X=e_2,\qquad
L^{\wedge_{*}}_{e_1}L^{\wedge_{*}}_{e_1}(e_2)=-e_2,\qquad
L^{\wedge_{*}}_{e_1\wedge_{*}e_1}=L^{\wedge_{*}}_{0}=0 ,
$$
so the composite is not an operator of the block. The correction term is visible on a central parameter: with $\tilde A=e_1$, $\tilde B=e_0$, $\tilde X=e_0$ the naive value $\mathrm{Vect}(\tilde A\tilde X\tilde B^{*})=e_1$ is cancelled exactly by the alignment term $-\overline{H(e_0,e_0)}\mathrm{Vect}(e_1)=-e_1$, and the composite vanishes, as $L^{\wedge_{*}}_{e_1}L^{\wedge_{*}}_{e_0}(e_0)=0$ requires. The two-band contrast closes the case: the algebraic norm of the companion band is the purity $\tfrac12 e_0$ and the algebraic norm of this band is the coherence $\tfrac12 ie_1$, one value read twice.

**A numerical check.** Recomputation with biquaternions to machine precision over random elements and over the displayed cases gives: the three definitions of the operation agree, $\mathrm{Vect}(\tilde P\tilde Q^{*})=\tfrac12(\tilde P\tilde Q^{*}-(\tilde P\tilde Q^{*})^{\natural})=\tfrac12(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}})$, and the conjugate-alternation holds; the left multiplication is conjugate-linear, the right one $\mathbb{C}$-linear and $R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}}$; the two composition laws of the block hold, the witness $L^{\wedge_{*}}_{e_1}L^{\wedge_{*}}_{e_1}(e_2)=-e_2$ is reproduced against $L^{\wedge_{*}}_{e_1\wedge_{*}e_1}=0$, and the correction term cancels the naive value on the central parameter; the sandwich composition table holds, $S_{\tilde A,e_0}=L_{\tilde A}$ and $S_{\tilde A,\tilde B}=R_{\tilde B}L_{\tilde A}$; the adjoints hold, $(S_{\tilde P,\tilde Q})^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$, $(L^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$ and $(R^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)\tilde A$; the type criteria hold exactly on the central parameters and the sandwich criterion exactly on the conjugate pairs; the unitary sandwiches are anti-isometries, $H(S\tilde X,S\tilde Y)=\overline{H(\tilde X,\tilde Y)}$; the trace of $L^{\wedge_{*}}_{\tilde A}$ vanishes, its rank is six for random parameters and four for the zero divisor $e_1+ie_2$, and the characteristic polynomials $\lambda^{2}(\lambda^{2}-1)^{3}$, $\lambda^{4}(\lambda^{2}+1)^{2}$ and $\lambda^{4}(\lambda^{2}+2)^{2}$ are reproduced; the cyclic sum is nonzero on sixty of sixty random triples; the derivation bracket $[D_{\vec a},D_{\vec b}]=D_{\vec a\times\vec b}$ holds; and the worked case was checked coefficient by coefficient.

## The Bound

The article states one cell of the grid of the twelve operator rows, and the boundary of the cell is what it must declare.

- **The operation is not re-defined here.** Its conjugate-alternation, its algebraic norm and its quadric are *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* and *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the split of a sesquilinear value into its two halves is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.
- **The operators and the sandwich are not re-proved here.** They are *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, whose general matrix, rank, kernel, characteristic polynomial, adjoint and derivations are quoted; the general sandwich and its composition table are *The Sesquilinear Sandwich Operator* and *The Sesquilinear Sandwich on the Biquaternions*.
- **The adjoint is not re-proved here.** The general twisted rule and the model adjoints $S_{a,b}^{\dagger}=S_{b,a}$, $L_{a}^{\dagger}=S_{1,a}$ and $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$ are *The Sesquilinear Adjoint Operator*; the biquaternion instance of the sandwich adjoint is *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*.
- **The physical phases are not read here.** They are *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* and *Interference without a Lie Algebra: the Jacobi Failure in the State Space*, with the physical phases of *The Path Integral in Biquaternionic Form*, *The Double-Slit Experiment in Biquaternionic Form*, *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form*, *The Berry Phase and Geometric Phases in Biquaternionic Form* and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*. This article reads the operator half and does not trespass.
- **The comparison of the twelve rows is not this article.** It is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, which is not one of the twelve.

**What the framework does not claim.** The interpretation does not derive interference, a phase angle or a measurement rule from the operator calculus; it reads the vector half of a sesquilinear value as a phase and names the operators that produce it. It does not claim that the failing composition is repaired by the derivations, the derivations being an algebra of another kind; and it does not claim that the operator theory of the twelve rows is one theory, the phase row being one of the four sesquilinear rows that share a parity and no enveloping algebra.

## The Ledger

**Proved.** The antisymmetric plain sesquilinear product $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ has two multiplication operators, $L^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X^{*})$ and $R^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde X\tilde A^{*})$, conjugate-linear and $\mathbb{C}$-linear respectively, with opposite parity in the variable and in the parameter, and related by the conjugate-alternation $R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}}$, so that a single $\mathbb{C}$-linear companion $T^{\wedge_{*}}_{\tilde A}=\overline{L^{\wedge_{*}}_{\tilde A}}$ carries the block; the left operator is the vector part of the row left multiplication, $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A}$, and the sandwich with the unit, $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$; the composition laws $L^{\wedge_{*}}_{\tilde A}L^{\wedge_{*}}_{\tilde B}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X\tilde B^{*})-\overline{H(\tilde B,\tilde X)}\mathrm{Vect}(\tilde A)$ and $R^{\wedge_{*}}_{\tilde A}R^{\wedge_{*}}_{\tilde B}(\tilde X)=\mathrm{Vect}(\tilde X\tilde B^{*}\tilde A^{*})-H(\tilde X,\tilde B)\mathrm{Vect}(\tilde A^{*})$ hold, neither family is multiplicative, and the block has no monoid of one-sided operators; the sandwich $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ composes by the table $S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$, $T_{\tilde P,\tilde Q}S_{\tilde A,\tilde B}=S_{\tilde P\tilde A,\tilde Q^{*}\tilde B}$, $S_{\tilde C,\tilde D}T_{\tilde P,\tilde Q}=S_{\tilde C\tilde Q^{*},\tilde D\tilde P}$ and $S_{\tilde A,\tilde B}^{2}=T_{\tilde A\tilde B,\tilde A^{*}\tilde B^{*}}$, and its adjoint is $S_{\tilde Q^{*},\tilde P^{*}}$; the form $H$ is positive definite and the adjoint for it conjugates the parameter and keeps the side, $(R^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)\tilde A$, while the left operator leaves the family, $(L^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$; the type criteria are $L^{\wedge_{*}}_{\tilde A}$ and $R^{\wedge_{*}}_{\tilde A}$ self-adjoint exactly for a central parameter, skew-adjoint only for the zero parameter, and never unitary, and a sandwich self-adjoint exactly on a conjugate pair and skew only when it vanishes; the isometries of the form that preserve the block are the real rotations $T_R$, the automorphisms of the product are the structure group of $T_R$ and the coefficientwise conjugation, and the natural conjugation is not one; the derivations are $D_{\vec a}(\tilde X)=[0,\vec a\times\tilde{\vec X}]$ with $\vec a$ real, the Lie algebra $\mathbb{R}^{3}$ of the cross product; the algebraic norm on the state side is the Bloch vector, $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\vec r$; the sandwich at a unitary parameter is the inner involution $\sigma_{\tilde u}$, a conjugate-linear anti-automorphism of the algebra and not an automorphism of the block, and it agrees with the inner automorphism exactly on the state side; and the cyclic sum of the block does not vanish, the witnesses being $\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3$ and $\mathrm{cyc}\,\wedge_{*}(e_1,e_1,ie_2)=-2ie_2$. The worked case gives $\tilde\rho=\tfrac12(e_0+ie_1)$ with $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 ie_1$ against the purity $\tfrac12 e_0$, the phase pair $H(e_0+ie_1,e_0+e_1)=1+i$ with $\tilde P\wedge_{*}\tilde Q=(-1+i)e_1$, and the composition witness $L^{\wedge_{*}}_{e_1}L^{\wedge_{*}}_{e_1}(e_2)=-e_2$ against $L^{\wedge_{*}}_{e_1\wedge_{*}e_1}=0$.

**Interpretations.** That the left family is conjugate-linear and the right one $\mathbb{C}$-linear, so the two slots of the phase pairing have opposite polarity; that the antisymmetry makes the right family the negative mirror of the left, so a single linear companion carries the block; that the adjoint conjugates the phase and keeps the side, so the observables of the block are the central parameters and the unitary ones are the sandwiches of the unitary slice; that the two-sided phase operator is the sandwich, whose adjoint exchanges its ends; that the composition does not close and no Lie algebra is raised from the block, the surviving algebra being the cross product of the real rotations; that the phase vector has a definite length because the form survives where the algebra does not; and that the algebraic norm on a state is the coherence direction, one value of the pairing read twice. Each is the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

The antisymmetric plain sesquilinear product is the framework's phase structure, and its operators read as the two ways of attaching a phase to an amplitude. The left attachment conjugates the variable and the right attachment conjugates the parameter, and the antisymmetry ties the two together: the right family is the negative mirror of the left, so the phase operator has one handedness and the other slot is read by mirroring. This is the exact point at which the phase band separates from the probability band, where the two families are independent. The adjoint of the band is the Hermitian adjoint of the positive form, and it conjugates the phase of the parameter without moving the operation to the other side; the only self-adjoint one-sided phase operators are the central ones, and the two-sided ones are the quadratic representations $S_{\tilde P,\tilde P^{*}}$. The composition of the operators does not close, and the operation itself fails the Jacobi identity, so the phase structure carries a **pairing and no symmetry algebra**; the framework reads that as the statement that an interference term is assembled from two amplitudes and is a relational datum, not an infinitesimal transformation, and the readings are those of *Interference without a Lie Algebra: the Jacobi Failure in the State Space*. What survives is the positive form, so the phase vector has a definite length, and the cross-product algebra of the real rotations, so the block does have an infinitesimal symmetry of another kind.

Read on the states, the phase operator returns the coherence direction. For a state $\tilde\rho=\tfrac12(e_0+i\vec r)$ the algebraic norm of the block is the Bloch vector $\tfrac12 i\vec r$, while the algebraic norm of the companion band is the purity, so one value read on one state splits into a central number and a vector, the probability and the axis of the phase. The unitary sandwich mirrors the algebra order, and on the state side that mirror agrees with the ordinary conjugation, so the phase action on a state is unambiguous; the ambiguity of the block's two conjugations lives off the states. Read on the clock, the phase is carried by a vector and not by a scalar, and the central generator of the absolute phase is elsewhere: the block reads the relative phase, which carries no current, and the absolute, central phase is the material generator of the corpus, *The Harmonic Oscillator in Biquaternionic Form* and *The Scalar Fock Space in Biquaternionic Form*. The physical phases, the interference experiment and their measure are *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product*, *The Double-Slit Experiment in Biquaternionic Form*, *Geometric Phases of Non-Relativistic Spin in Biquaternionic Form*, *The Berry Phase and Geometric Phases in Biquaternionic Form* and *Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form*, and are not re-read here.

## Summary

The operators of the antisymmetric plain sesquilinear product are the left and the right multiplications $L^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X^{*})$ and $R^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde X\tilde A^{*})$. The left one is conjugate-linear and the right one $\mathbb{C}$-linear, and the two families have opposite parity in the variable and in the parameter at once, exactly as in the probability band. What is new is the **conjugate-alternation on the operators**, $R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}}$, which makes the right family the negative mirror of the left, so a single $\mathbb{C}$-linear companion $T^{\wedge_{*}}_{\tilde A}=\overline{L^{\wedge_{*}}_{\tilde A}}$ carries the whole block. The left operator is the vector part of the row left multiplication, $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A}$, and also the projected sandwich with the unit, $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$. The **sandwich** $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ is the two-sided operator the band owns; it composes by $S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$ and its adjoint is $S_{\tilde Q^{*},\tilde P^{*}}$, so the self-adjoint sandwiches are the conjugate pairs $S_{\tilde P,\tilde P^{*}}$ and only the zero sandwich is skew. The composition of the block's one-sided operators does **not** close, the composite of two left operators being the vector part of a two-sided multiplication corrected by the alignment term $-\overline{H(\tilde B,\tilde X)}\mathrm{Vect}(\tilde A)$, so the block has no monoid and no regular representation. The form is the positive definite Hermitian form $H$, and the adjoint for it **keeps the side and conjugates the parameter**, $(R^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)\tilde A$, while the left operator leaves the family; the one-sided type criteria are centrality for self-adjointness and triviality for skewness, and no one-sided operator is an isometry. The isometries of the form that preserve the product are the real rotations $T_R$, the automorphisms of the product are those together with the coefficientwise conjugation, which preserves the product and reverses the form, and the derivations are the cross products with a real vector, the Lie algebra $\mathbb{R}^{3}$. On the state side the algebraic norm is the Bloch vector, $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\vec r$; the unitary sandwich is the inner involution, a conjugate-linear anti-automorphism of the algebra and not an automorphism of the block, and it agrees with the inner automorphism exactly on the states. The operation fails the Jacobi identity, the witnesses being $\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3$ and $\mathrm{cyc}\,\wedge_{*}(e_1,e_1,ie_2)=-2ie_2$, so the phase structure carries **a pairing and no symmetry algebra**, and the definite form survives where the algebra does not. The reading is that a phase is read from the vector half of a sesquilinear value, that the operators producing it are the projected probability operators, and that the phase structure composes nowhere and generates nothing, the infinitesimal symmetry being the rotations of the material frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\wedge_{*}\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ | The antisymmetric plain sesquilinear product (APS); the phase operation |
| $\tilde P\tilde Q^{*}=\tilde P\circledast\tilde Q+\tilde P\wedge_{*}\tilde Q$ | The split of one value into the central and the vector half |
| $L^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X^{*})$ | Left multiplication; conjugate-linear in the variable |
| $R^{\wedge_{*}}_{\tilde A}(\tilde X)=\mathrm{Vect}(\tilde X\tilde A^{*})$ | Right multiplication; $\mathbb{C}$-linear in the variable |
| $R^{\wedge_{*}}_{\tilde A}=-\overline{L^{\wedge_{*}}_{\tilde A}}$ | The conjugate-alternation; the right family is the negative mirror |
| $T^{\wedge_{*}}_{\tilde A}=\overline{L^{\wedge_{*}}_{\tilde A}}=-R^{\wedge_{*}}_{\tilde A}$ | The $\mathbb{C}$-linear companion; the honest linear object |
| $L^{\wedge_{*}}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$ | The operator as a projection of the row and of the sandwich |
| $L^{\wedge_{*}}_{\tilde A}L^{\wedge_{*}}_{\tilde B}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X\tilde B^{*})-\overline{H(\tilde B,\tilde X)}\mathrm{Vect}(\tilde A)$ | The composition law of the block; not multiplicative |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}=T_{\tilde P,\tilde Q^{*}}\circ{}^{*}$ | The sesquilinear sandwich; the two-sided operator of the band |
| $S_{\tilde C,\tilde D}S_{\tilde A,\tilde B}=T_{\tilde C\tilde B,\tilde A^{*}\tilde D^{*}}$ | The sandwich composition law |
| $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$ | The adjoint of the sandwich; stars and exchanges the parameters |
| $H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ | The Hermitian form; positive definite, Gram identity |
| $T^{\dagger}$ | The adjoint for $H$; twisted rule for a conjugate-linear operator |
| $(R^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)\tilde A$ | The adjoint keeps the side and conjugates the parameter |
| $(L^{\wedge_{*}}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$ | The adjoint of the left operator leaves the family |
| Self-adjoint $\iff$ central; skew $\iff$ zero; never unitary | The one-sided type criteria of the block |
| $S_{\tilde P,\tilde P^{*}}$ self-adjoint; skew only for the zero sandwich | The two-sided type criteria |
| $T_R$, $\overline{\cdot}$ | The automorphisms of the product; the structure group |
| $D_{\vec a}(\tilde X)=[0,\vec a\times\tilde{\vec X}]$, $[D_{\vec a},D_{\vec b}]=D_{\vec a\times\vec b}$ | The derivations; the Lie algebra $\mathbb{R}^{3}$ of the cross product |
| $\tilde\rho=\tfrac12(e_0+i\vec r)$, $\tilde\rho\wedge_{*}\tilde\rho=\tfrac12 i\vec r$ | A state and its Bloch vector; the algebraic norm on the state side |
| $S_{\tilde u,\tilde u}=\sigma_{\tilde u}$, $S_{\tilde u,\tilde u^{*}}$ | The inner involution and the reflection at a unitary parameter |
| $\mathrm{cyc}\,\wedge_{*}(e_0,e_1,e_2)=e_3$, $\mathrm{cyc}\,\wedge_{*}(e_1,e_1,ie_2)=-2ie_2$ | The failing cyclic sums; no Lie bracket |
| $\mathbb{M}_{+}$, $U$, $S=\mathbb{B}\tilde\Pi_+$ | The state side, the unitary slice, the spinor module |

## Further Reading

- *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.md`), which owns the one-sided operators, the companion, the matrix, the rank, the kernel, the characteristic polynomial, the adjoint, the derivations and the structure group of the block.
- *The Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-sesquilinear-sandwich-on-the-biquaternions.md`), for $S_{\tilde P,\tilde Q}$, the composition table, the rank and the invertibility criterion.
- *The Sesquilinear Sandwich Operator* (`articles_maths/the-sesquilinear-sandwich-operator.md`), for the general sandwich and its table.
- *The Adjoint of the Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-adjoint-of-the-sesquilinear-sandwich-on-the-biquaternions.md`), for $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}$ and the self-adjoint criterion.
- *The Sesquilinear Adjoint Operator* (`articles_maths/the-sesquilinear-adjoint-operator.md`), for the twisted adjoint rule and the model adjoints $S_{a,b}^{\dagger}=S_{b,a}$, $L_{a}^{\dagger}=S_{1,a}$ and $T_{p,q}^{\dagger}=T_{p^{*},q^{*}}$.
- *The Left and Right Multiplications of the Biquaternion Sesqualgebra* (`articles_maths/the-left-and-right-multiplications-of-the-biquaternion-sesqualgebra.md`), for the row one-sided operators, the mixed composites and the obstruction to a single linear representation.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, the conjugate-alternation and the coefficientwise automorphism.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the algebraic norm, the quadric and the Jacobi failure.
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairing of the values.
- *The Operators of the Plain Sesquilinear Product and the Born Pairing* (`articles_physics/the-operators-of-the-plain-sesquilinear-product-and-the-born-pairing.md`), the probability band sibling, for the form and the parity asymmetry.
- *The Operators of the General Plain Bilinear Product: One-Sided, Two-Sided and the Sandwich* (`articles_physics/the-operators-of-the-general-plain-bilinear-product-one-sided-two-sided-and-the-sandwich.md`), the composition band sibling, for the adjoint that swaps the sides.
- *The Imaginary Part of the Born Pairing: the Antisymmetric Sesquilinear Product* (`articles_physics/the-imaginary-part-of-the-born-pairing-the-antisymmetric-sesquilinear-product.md`) and *Interference without a Lie Algebra: the Jacobi Failure in the State Space* (`articles_physics/interference-without-a-lie-algebra-the-jacobi-failure-in-the-state-space.md`), the two articles of the band, which own the phase interpretation and the failure's interpretation.
- *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader, for the comparison of the twelve rows.
