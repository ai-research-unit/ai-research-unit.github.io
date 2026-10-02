# __Sesquilinear Forms and the Lax–Milgram Theorem__

## Introduction

Many operators of analysis are defined not by a formula but by a form: a sesquilinear pairing $B(x,y)$ from which the operator is recovered by $B(x,y)=\langle Ax,y\rangle$. The pair of conditions that make this recovery possible and useful are **boundedness**, which bounds the form by a multiple of the two norms, and **coercivity**, which bounds the diagonal $B(x,x)$ below by a positive multiple of $\|x\|^2$. Under these two conditions the **Lax–Milgram theorem** produces a unique bounded operator $A$ representing the form, and it produces the operator's inverse with the bound controlled by the coercivity constant; the theorem is the variational entry point to the theory of elliptic equations, and its Hermitian specialisation is the positivity and self-adjointness of the represented operator.

This article fixes the bounded sesquilinear forms, the operator they represent, the Lax–Milgram theorem with its inverse bound, the Hermitian forms and the associated self-adjoint operators, and the equivalent inner products that a coercive Hermitian form defines. The Hilbert-space structure is *Hilbert Spaces*; the Riesz representation theorem is there and in *Banach and Hilbert Spaces*; the self-adjointness and positivity of the represented operator are *Self-Adjoint Operators and the Spectral Theorem* and *Positive Operators and the Square Root*; the form-theoretic version for a form that is only semi-bounded is *The Friedrichs Extension of a Hermitian Form*; the Dirichlet form is *Dirichlet Forms and the Hermitian Dirichlet Principle*.

Throughout, $H$ is a Hilbert space over $\mathbb{K}=\mathbb{C}$ (or a real Hilbert space over $\mathbb{R}$), $\langle\cdot,\cdot\rangle$ is linear in the first argument and conjugate-linear in the second, and $\|\cdot\|$ is the induced norm. A **sesquilinear form** is a map $B:H\times H\to\mathbb{K}$ linear in the first argument and conjugate-linear in the second; it is **bounded** if $\|B\|=\sup_{\|x\|,\|y\|\le1}|B(x,y)|<\infty$ and **coercive** if there is $c>0$ with $\operatorname{Re}B(x,x)\ge c\|x\|^2$ for all $x$.

## Bounded Sesquilinear Forms

**Definition.** A **bounded sesquilinear form** on $H$ is a sesquilinear $B$ with $\|B\|<\infty$. It is **Hermitian** if $B(x,y)=\overline{B(y,x)}$ for all $x,y$, and **symmetric** in the real case if $B(x,y)=B(y,x)$.

**Proposition (the form norm and the polarisation).** For a bounded sesquilinear form,

$$
|B(x,y)|\le\|B\|\,\|x\|\,\|y\| ,
$$

the quantity $\|B\|$ is a norm on the space of bounded forms, and the form is determined by its diagonal values through the polarisation identity

$$
B(x,y)=\tfrac14\bigl(B(x+y,x+y)-B(x-y,x-y)+i\,B(x+iy,x+iy)-i\,B(x-iy,x-iy)\bigr) .
$$

A form is Hermitian exactly when its diagonal $B(x,x)$ is real for every $x$.

*Proof.* The bound is the definition of the supremum; the polarisation identity is the expansion of the four squares, valid because the form is sesquilinear; the Hermitian condition is equivalent to the reality of the diagonal, as the identity shows by exchanging the arguments.

**Proposition (the adjoint form).** The **adjoint form** is $B^*(x,y)=\overline{B(y,x)}$; it is sesquilinear and bounded with $\|B^*\|=\|B\|$, the operation $B\mapsto B^*$ is a conjugate-linear involution, and $B$ is Hermitian exactly when $B^*=B$.

*Proof.* Conjugating the arguments reverses the linearity, so $B^*$ is sesquilinear; the norm identity is the exchange of the two variables in the supremum; the involution and the criterion are immediate from the definitions.

## The Represented Operator

**Theorem (representation of a bounded form).** For every bounded sesquilinear form $B$ there is a unique $A\in B(H)$ with

$$
B(x,y)=\langle Ax,y\rangle\quad(x,y\in H),\qquad \|A\|=\|B\| .
$$

Conversely every $A\in B(H)$ represents the bounded form $B_A(x,y)=\langle Ax,y\rangle$, and the correspondence $B\leftrightarrow A$ is a conjugate-linear isometry that carries the adjoint form to the adjoint operator: $B^*\leftrightarrow A^*$.

*Proof.* For fixed $x$ the map $y\mapsto\overline{B(x,y)}$ is a bounded linear functional, so by the Riesz representation theorem there is a unique $Ax$ with $B(x,y)=\langle Ax,y\rangle$; the map $x\mapsto Ax$ is linear because $B$ is linear in its first argument, and $\|A\|=\|B\|$ is the equality of the two suprema. The converse and the adjoint statement are immediate from the definitions.

**Corollary (Hermitian forms and self-adjoint operators).** The form $B$ is Hermitian exactly when the represented operator $A$ is self-adjoint, and then $B(x,x)=\langle Ax,x\rangle$ is real; the form is positive definite exactly when $A$ is a positive operator, and coercive exactly when $A$ is positive with $\langle Ax,x\rangle\ge c\|x\|^2$, equivalently when $A$ is positive and invertible with $A\ge cI$.

*Proof.* $B(x,y)=\langle Ax,y\rangle$ and $\overline{B(y,x)}=\langle x,Ay\rangle=\langle A^*x,y\rangle$, so Hermitian symmetry is $A=A^*$; the positivity statements are the translation of the inequalities through the representation.

## The Lax–Milgram Theorem

**Theorem (Lax–Milgram).** Let $B$ be a bounded coercive sesquilinear form on $H$ with coercivity constant $c>0$. Then the represented operator $A$ is boundedly invertible and

$$
\|A^{-1}\|\le\frac1c .
$$

Equivalently, for every $f\in H$ there is a unique $x\in H$ with

$$
B(x,y)=\langle f,y\rangle\qquad(y\in H),
$$

and it satisfies $\|x\|\le\frac1c\|f\|$.

*Proof.* Coercivity gives $c\|x\|^2\le\operatorname{Re}\langle Ax,x\rangle\le\|Ax\|\|x\|$, hence $\|Ax\|\ge c\|x\|$; so $A$ is injective with closed range. The adjoint form $\bar B$ is also coercive with the same constant, so $A^*$ has closed range, and the range of $A$ is the orthogonal complement of the kernel of $A^*$, which is zero; hence $A$ is surjective. The estimate for $A^{-1}$ is the same inequality read backwards, and the solvability statement is the representation $f=A^{-1}f$ of the equation.

**Corollary (stability of the solution).** The solution $x$ of the variational equation depends continuously on $f$, and if the form is represented by a self-adjoint coercive $A$ then $A$ is positive with spectrum contained in $[c,\|A\|]$; in particular the smallest spectral value is at least the coercivity constant.

*Proof.* Continuity is the bound $\|x\|\le\|f\|/c$; for self-adjoint $A$ the coercivity inequality and the bound $|\langle Ax,x\rangle|\le\|A\|\|x\|^2$ confine the numerical range to $[c,\|A\|]$, and the spectrum lies in the closure of the numerical range.

**Remark.** The two hypotheses are independent: the form $B(x,y)=i\langle x,y\rangle$ is bounded and not coercive, the diagonal form $\langle Ax,y\rangle$ with $A$ unbounded is coercive on its form domain and not bounded, and the form $B(x,y)=\langle x,y\rangle$ is both. The coercive Hermitian bounded case is the case in which $A$ is a positive invertible operator, and it is the case in which the form gives a new inner product equivalent to the old one.

## Hermitian Forms and Equivalent Inner Products

**Proposition (a coercive Hermitian form is an inner product).** Let $B$ be a Hermitian bounded form with $B(x,x)\ge c\|x\|^2$ for a constant $c>0$. Then

$$
\langle x,y\rangle_B=B(x,y)
$$

is an inner product on $H$ whose norm is equivalent to the original norm,

$$
\sqrt{c}\,\|x\|\le\|x\|_B\le\sqrt{\|B\|}\,\|x\| ,
$$

and $H$ is complete for $\|\cdot\|_B$; the two norms induce the same topology.

*Proof.* The form is sesquilinear, Hermitian and positive definite, hence an inner product; the two inequalities are the coercivity and the boundedness, and completeness follows from the equivalence of the norms.

**Proposition (the operator that changes the inner product).** With $B$ and $A$ as above, $A$ is positive and invertible, and the new inner product is

$$
\langle x,y\rangle_B=\langle Ax,y\rangle=\langle A^{1/2}x,A^{1/2}y\rangle ;
$$

hence $A^{1/2}$ is an isometry from $(H,\langle\cdot,\cdot\rangle_B)$ onto $(H,\langle\cdot,\cdot\rangle)$, and the self-adjoint operators of the two Hilbert structures are related by conjugation with $A^{1/2}$.

*Proof.* The square-root factorisation is the self-adjointness and positivity of $A$; the isometry statement is the second display, and the conjugation statement follows from the change of the inner product by an isometry.

**Example (the Dirichlet form).** For an open set $\Omega$ the form

$$
B(u,v)=\int_\Omega\nabla u\cdot\nabla\bar v
$$

is bounded and coercive on the Sobolev space $H^1_0(\Omega)$ by the Poincaré inequality, so the Lax–Milgram theorem represents it by a bounded operator on that space; the operator is the Dirichlet Laplacian, and the variational equation $B(u,v)=\langle f,v\rangle$ is the weak formulation of $-\Delta u=f$ with homogeneous boundary values.

**Example (the weak formulation of an elliptic problem).** For a uniformly elliptic coefficient matrix $a(x)$ the form

$$
B(u,v)=\int_\Omega a(x)\nabla u\cdot\nabla\bar v
$$

is bounded and coercive on $H^1_0(\Omega)$, so the boundary-value problem $\operatorname{div}(a\nabla u)=f$ has a unique weak solution for every $f\in H^{-1}(\Omega)$; the coercivity constant is the ellipticity constant, and the Lax–Milgram bound is the standard energy estimate.

## Summary

A bounded sesquilinear form $B$ on a Hilbert space satisfies $|B(x,y)|\le\|B\|\|x\|\|y\|$, is determined by its diagonal through the polarisation identity, and is Hermitian exactly when the diagonal is real; the adjoint form $B^*(x,y)=\overline{B(y,x)}$ is a conjugate-linear involution of the space of forms. Every bounded form is represented by a unique bounded operator, $B(x,y)=\langle Ax,y\rangle$ with $\|A\|=\|B\|$, and the correspondence carries the adjoint form to the adjoint operator, so Hermitian forms correspond to self-adjoint operators and coercive forms to positive invertible ones. The Lax–Milgram theorem states that a bounded coercive form represents a boundedly invertible operator with $\|A^{-1}\|\le1/c$, equivalently that the variational equation $B(x,y)=\langle f,y\rangle$ has a unique solution with $\|x\|\le\|f\|/c$. A coercive Hermitian form is itself an inner product equivalent to the given one, the equivalence being implemented by $A^{1/2}$, and the Dirichlet form and the weak formulation of an elliptic problem are the standard examples of the theorem in analysis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(x,y)$ | sesquilinear form, linear in the first argument |
| $\|B\|$ | bound of the form, $|B(x,y)|\le\|B\|\|x\|\|y\|$ |
| $B^*(x,y)=\overline{B(y,x)}$ | adjoint form, $B^*\leftrightarrow A^*$ |
| $B(x,y)=\langle Ax,y\rangle$ | the represented operator |
| $\|A\|=\|B\|$ | isometry of the correspondence |
| coercive | $\operatorname{Re}B(x,x)\ge c\|x\|^2$ |
| $\|A^{-1}\|\le1/c$ | Lax–Milgram inverse bound |
| $\langle x,y\rangle_B=B(x,y)$ | equivalent inner product of a coercive Hermitian form |
| $A^{1/2}$ | the isometry between the two inner products |
| Dirichlet form | $\int\nabla u\cdot\nabla\bar v$ on $H^1_0$ |

## Further Reading

- Peter D. Lax and Arthur N. Milgram, "Parabolic Equations", in *Contributions to the Theory of Partial Differential Equations*, Annals of Mathematics Studies 33 (Princeton University Press, 1954), 167–190, for the original theorem.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the weak formulation and the energy estimates.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the sesquilinear forms and the representation theorem.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the forms associated with unbounded operators and the sectorial forms.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the Lax–Milgram theorem and its operator form.
