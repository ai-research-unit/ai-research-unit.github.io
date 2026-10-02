# __Reflections as Signed Two-Sided Operators on a Hilbert Space__

## Introduction

A reflection is an order-two symmetry, and on the algebra $B(H)$ of a Hilbert space the symmetries are the automorphisms. The reflections that $B(H)$ carries with respect to the grade involution $\alpha(T)=\Gamma T\Gamma$ are the automorphisms of order two of the form

$$
\rho_U(T)=U\,\alpha(T)\,U^{-1},
$$

one for each operator $U$ whose product $U\alpha(U)$ with its twist is central, that is, a scalar. Each such $\rho_U$ is the signed sandwich $S_{U,U^{-1}}$ of *The Signed Sandwich on a Hilbert Space*, and the present article studies the correspondence between these reflections and the operators that produce them, computes the fixed part and the negated part, records the isometry and unitarity properties that the Hilbert structure makes available, and isolates the cases in which the correspondence degenerates.

The algebra $B(H)$ and the involution are *Bounded Operators on a Hilbert Space*; the signed sandwich, its composition table and its invertibility are *The Signed Sandwich on a Hilbert Space*; the algebraic correspondence, of which the present article is the Hilbert-space reading, is *Reflections as Signed Two-Sided Operators on an Algebra* (Part I). The graded modules and the adjoint theory of the reflections are *The Graded Action on a Module over a Hilbert Space* and *The Signed Adjoint of the Reflection on a Hilbert Space*.

Throughout, $H=H^0\oplus H^1$ is a graded Hilbert space, $\Gamma$ is the parity operator, $\alpha(T)=\Gamma T\Gamma$ is the grade involution of $B(H)$, and $\rho_U(T)=U\alpha(T)U^{-1}$ is the signed conjugation by an invertible $U$. The reflectors are the invertible $U$ with $U\alpha(U)$ central, the set of reflections is written $\mathrm{Ref}(H,\alpha)$, and the group of invertible operators is $B(H)^\times$.

## The Reflector and the Reflection

**Definition.** A **reflector** of the graded Hilbert space is an invertible $U\in B(H)^\times$ with

$$
U\,\alpha(U)=\lambda I,\qquad \lambda\in\mathbb{K},
$$

that is, an invertible operator whose product with its twist is a scalar. The **reflection** determined by a reflector $U$ is

$$
\rho_U:B(H)\longrightarrow B(H),\qquad \rho_U(T)=U\,\alpha(T)\,U^{-1}=S_{U,U^{-1}}(T).
$$

The set of reflectors is $R^\times(H,\alpha)$ and the set of reflections is $\mathrm{Ref}(H,\alpha)$.

**Proposition (the scalar is unimodular).** If $U$ is a reflector with $U\alpha(U)=\lambda I$ then $|\lambda|=1$, and $\lambda$ is real only when $U\alpha(U)$ is self-adjoint. In particular $\rho_U$ is determined by the reflector $U$, and distinct scalars give distinct signed products but the same type of reflection.

*Proof.* $U\alpha(U)$ is a product of unitaries when $U$ is unitary and is invertible in general; its scalar value has modulus $\|U\alpha(U)\|$ when $U$ is unitary, hence $|\lambda|=1$; the reality statement is $\lambda I=(\lambda I)^*=\overline{\lambda}I$, that is $\lambda=\bar\lambda$.

**Proposition (the identity and the grade involution).** The identity operator is a reflector and $\rho_I=\alpha$, so the grade involution is always among the reflections; a scalar multiple $\lambda U$ of a reflector is again a reflector, with $\lambda^2 U\alpha(U)$ in place of $U\alpha(U)$, and it determines the same reflection.

*Proof.* $I\alpha(I)=I$ is central; $\rho_I(T)=\alpha(T)$; $(\lambda U)\alpha(\lambda U)=\lambda^2U\alpha(U)$ is central, and the conjugation by $\lambda U$ equals the conjugation by $U$.

## The Reflection Is an Involutive Automorphism

**Theorem.** For every reflector $U$ the signed conjugation $\rho_U$ is a $*$-automorphism of $B(H)$ with

$$
\rho_U^2=\mathrm{id},
$$

so $\rho_U$ is an involutive automorphism of $B(H)$. Conversely, if the signed conjugation $\rho_U$ is involutive, then $U$ is a reflector.

*Proof.* The map is the composite of the automorphisms $\alpha$ and $\iota_U$, hence an automorphism, and it preserves the adjoint because both factors do. Its square is $\rho_U^2(T)=U\alpha(U)\,T\,(U\alpha(U))^{-1}=\iota_{U\alpha(U)}(T)$, the inner automorphism by $U\alpha(U)$, which is the identity exactly when $U\alpha(U)$ is central; the centre of $B(H)$ is the scalar operators, so this is the reflector condition. The converse is the same computation read backwards.

**Corollary (the eigenvalue decomposition).** Let $U$ be a reflector and $\rho=\rho_U$. Then

$$
B(H)=B(H)^+_\rho\oplus B(H)^-_\rho,\qquad
B(H)^\pm_\rho=\{T:\rho(T)=\pm T\},
$$

the summands are the fixed part and the negated part, they are closed in the operator norm and in the Hilbert–Schmidt norm, and

$$
B(H)^+_\rho B(H)^+_\rho\subseteq B(H)^+_\rho,\quad
B(H)^+_\rho B(H)^-_\rho\subseteq B(H)^-_\rho,\quad
B(H)^-_\rho B(H)^+_\rho\subseteq B(H)^-_\rho,\quad
B(H)^-_\rho B(H)^-_\rho\subseteq B(H)^+_\rho .
$$

*Proof.* An involutive automorphism has eigenvalues $\pm1$ and its eigenspaces give the decomposition; the multiplication table is the multiplicativity of $\rho$, applied to the four combinations of signs.

**Corollary (the reflection is determined by its mirror).** A reflection is determined by its fixed subalgebra: if two involutive $*$-automorphisms have the same fixed subalgebra then they are equal.

*Proof.* An order-two automorphism is determined by its action on the two eigenspaces, and the $\pm1$ eigenspaces determine each other by the direct sum decomposition.

## The Correspondence

**Theorem.** The assignment $U\mapsto\rho_U$ is a map from the reflectors onto the reflections, and it is constant exactly on the cosets of the centre: for invertible $U,V$,

$$
\rho_U=\rho_V \qquad\Longleftrightarrow\qquad V^{-1}U=\lambda I\ \text{for a scalar}\ \lambda\neq0 .
$$

Hence the reflections are parametrised by the reflectors modulo the scalars,

$$
\mathrm{Ref}(H,\alpha)\;\cong\;R^\times(H,\alpha)/\mathbb{K}^\times ,
$$

and the reflection $\rho_I=\alpha$ is the class of the scalar operators.

*Proof.* If $\rho_U=\rho_V$ then $U\alpha(T)U^{-1}=V\alpha(T)V^{-1}$ for every $T$, whence $(V^{-1}U)\alpha(T)=\alpha(T)(V^{-1}U)$ for every $T$, so $V^{-1}U$ commutes with all of $B(H)$ and is scalar; conversely a scalar is absorbed by the conjugation. The image of the scalars is $\alpha$.

**Proposition (the reflector acts on itself by its twist).** For a reflector $U$ with reflection $\rho=\rho_U$,

$$
\rho(U)=\alpha(U),
$$

so $U$ acts on $B(H)$ through the inner automorphism that corrects the grade involution to the reflection, $\rho_U=\iota_U\circ\alpha$.

*Proof.* Since $U\alpha(U)$ is central, $U$ commutes with it, so $\rho_U(U)=U\alpha(U)U^{-1}=\alpha(U)$; the composite form is the definition $\iota_U(\alpha(T))=U\alpha(T)U^{-1}$.

## Isometry, Unitarity and the Form

**Proposition (the reflection is an isometry).** Every $\rho_U$ is isometric for the operator norm, $\|\rho_U(T)\|=\|T\|$, and isometric for the Hilbert–Schmidt norm when $U$ is unitary, $\|\rho_U(T)\|_{\mathrm{HS}}=\|T\|_{\mathrm{HS}}$.

*Proof.* The automorphism $\rho_U$ is a composite of isometries when $U$ is unitary: the conjugation by a unitary and the grade involution are both isometric on $B(H)$ and on $S_2(H)$.

**Proposition (unitary reflections and the geometric reflection).** When $U$ is unitary the reflection $\rho_U$ is implemented on the Hilbert–Schmidt space by the unitary $L_U$ of *The Left and Right Multiplication Operators on a Hilbert Space*, and it is the inner automorphism of $B(H)$ by the unitary $U\Gamma$: since $\alpha(T)=\Gamma T\Gamma$, one has

$$
\rho_U(T)=U\Gamma\,T\,\Gamma U^{-1}=(U\Gamma)\,T\,(U\Gamma)^{-1},
$$

so a unitary reflector produces the conjugation by the unitary $U\Gamma$, and every conjugation by a unitary is a reflection for the appropriate sign of $\Gamma$. In particular a unitary reflector with $U\Gamma$ self-adjoint has $\rho_U$ an involutive $*$-automorphism implemented by a self-adjoint unitary, the operator form of the geometric reflection in a hyperplane.

*Proof.* The composite of the conjugations by $U$ and by $\Gamma$ is the conjugation by $U\Gamma$, and the product is unitary because both factors are; self-adjointness of $U\Gamma$ makes the implementing unitary a reflection operator in the geometric sense.

**Remark (the fixed part of a unitary reflection).** For a unitary reflector $U$ the fixed part $B(H)^+_\rho$ is the commutant of the implementing unitary $U\Gamma$, and the negated part is spanned by the operators $T$ with $\rho_U(T)=-T$; when $U\Gamma$ is the geometric reflection $x\mapsto x-2\langle x,u\rangle u$ in the hyperplane orthogonal to a unit vector $u$, the fixed part is the algebra of operators commuting with that reflection, the operator counterpart of the mirror of the reflection.

## Failure in Degenerate Cases

**Proposition (the trivial grading).** If $H^1=0$ then $\alpha=\mathrm{id}$ and every invertible $U$ is a reflector; the reflections are the inner automorphisms $\iota_U$, and the correspondence $\mathrm{Ref}\cong B(H)^\times/\mathbb{K}^\times$ is the standard identification of the inner automorphism group. No reflection beyond the inner automorphisms is produced.

*Proof.* $\Gamma=I$, so $\alpha=\mathrm{id}$ and $U\alpha(U)=U^2$ is central only via the scalar condition; the signed sandwich reduces to the inner automorphism by $U$.

**Proposition (the non-reflector).** An invertible $U$ fails to be a reflector exactly when $U\alpha(U)$ is not a scalar, and then $\rho_U$ is an automorphism of infinite order in general; the signed conjugation is not a reflection, and the family $B(H)^\pm$ is not defined.

*Proof.* The square of $\rho_U$ is the inner automorphism by $U\alpha(U)$; the inner automorphism group of $B(H)$ is the group of invertible scalars modulo the scalars, which is trivial, so an inner automorphism is the identity exactly when the implementing element is central; thus the square is nontrivial exactly when $U\alpha(U)$ is non-central, and the order of $\rho_U$ is the order of the class of $U\alpha(U)$.

**Proposition (the split grading and the block form).** When $H^0$ and $H^1$ have different dimensions the parity operator is not scalar and the centre of the parity-invariant subalgebra may be larger than the scalars; in that case the reflector condition is more than $U\alpha(U)$ scalar, and the correspondence acquires extra parameters.

*Proof.* The commutant of $\Gamma$ is $B(H^0)\oplus B(H^1)$, whose centre is the pair of scalars; for $U$ commuting with $\Gamma$ the product $U\alpha(U)=U^2$ is central in the commutant but not necessarily scalar in $B(H)$, and such a $U$ gives an involutive automorphism of the commutant not detected by the scalar criterion.

## Summary

On a graded Hilbert space with grade involution $\alpha(T)=\Gamma T\Gamma$, the signed conjugations $\rho_U(T)=U\alpha(T)U^{-1}=S_{U,U^{-1}}$ are automorphisms of $B(H)$; they are involutive exactly when $U\alpha(U)$ is central, that is for the **reflectors** $U$, and then they are the reflections of the algebra, with the fixed part and the negated part giving a direct sum decomposition of $B(H)$ and with $\rho_U(U)=\alpha(U)$ and $\rho_U=\iota_U\alpha$. The assignment $U\mapsto\rho_U$ maps the reflectors onto the reflections and is constant exactly on the cosets of the scalars, so $\mathrm{Ref}(H,\alpha)\cong R^\times(H,\alpha)/\mathbb{K}^\times$ and the grade involution is the class of the scalars. Every reflection is isometric, and for a unitary reflector it is implemented on the Hilbert–Schmidt space by the unitary $L_U$ and is the operator form of the geometric reflection; the correspondence degenerates when the grading is trivial, in which case only the inner automorphisms remain, when a factor $U\alpha(U)$ is non-central, in which case the signed conjugation has infinite order and is not a reflection, and when the two graded summands have different dimensions, in which case the centre of the parity-invariant subalgebra is larger than the scalars and the reflector condition acquires extra parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(T)=\Gamma T\Gamma$ | the grade involution of $B(H)$ |
| $\rho_U(T)=U\alpha(T)U^{-1}$ | the signed conjugation, a reflection for a reflector |
| $R^\times(H,\alpha)$ | the reflectors, $U\alpha(U)$ scalar |
| $\mathrm{Ref}(H,\alpha)$ | the reflections of $B(H)$ |
| $\rho_U^2=\iota_{U\alpha(U)}$ | the square is the inner automorphism by the twist |
| $\rho_U=\iota_U\circ\alpha$ | reflection as inner automorphism after the twist |
| $\rho_U(U)=\alpha(U)$ | the action of the reflector on itself |
| $\mathrm{Ref}\cong R^\times/\mathbb{K}^\times$ | the correspondence up to scalars |
| $B(H)^\pm_\rho$ | the fixed part and the negated part |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the automorphisms of $B(H)$ and the inner automorphism group.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the conjugations of operators and their fixed points.
- Percy Deift, *Orthogonal Polynomials and Random Matrices: A Riemann–Hilbert Approach*, Courant Lecture Notes 3 (American Mathematical Society, 1999), for the reflection of the Hilbert space in a hyperplane and its role in the theory of groups.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry", in *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the graded conjugations and the sign rule.
