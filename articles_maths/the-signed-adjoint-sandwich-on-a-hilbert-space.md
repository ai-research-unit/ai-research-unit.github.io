# __The Signed Adjoint Sandwich on a Hilbert Space__

## Introduction

The signed sandwich of a graded Hilbert space is the two-sided operator $\mathcal{T}_{A,B}(T)=A\,\alpha(T)\,B$, with $\alpha(T)=\Gamma T\Gamma$ the grade involution, and its adjoint with respect to the Hilbert–Schmidt form has a closed expression,

$$
(\mathcal{T}_{A,B})^*=\mathcal{T}_{\alpha(A^*),\,\alpha(B^*)},\qquad \alpha(A^*)=\alpha(A)^* ,
$$

so the adjoint of a signed sandwich is again a signed sandwich, obtained by adjoining the two parameters and applying the grade involution to each. The same computation for the unsigned sandwich gives $(L_{A}R_{B})^*=L_{A^*}R_{B^*}$, and the two formulas together show that the adjunction of the two-sided operators is an involution of the algebra they generate. From the adjoint come the criteria that this article computes: self-adjointness of the signed sandwich, its isometry, and the **unitarity condition**, which turns out to be the condition that the parameters be unitary up to central scalars rather than unitary outright. The adjoint is the object from which the signed adjoint of the reflection and the signed adjoint of the one-sided multiplications are read, and those are the subjects of the two companion articles.

This article fixes the Hilbert–Schmidt form, the adjoint of the unsigned and signed sandwiches, the adjoint of the product and its compatibility with the composition table, the self-adjointness, isometry and unitarity criteria, and the relation of the sandwich adjoint to the one-sided adjoints. The signed sandwich, its composition table and its invertibility are *The Signed Sandwich on a Hilbert Space*; the one-sided multiplications and their adjoints are *The Left and Right Multiplication Operators on a Hilbert Space* and *The Adjoint of the Left Multiplication on a Hilbert Space*; the reflections are *Reflections as Signed Two-Sided Operators on a Hilbert Space*, and their adjoints are *The Signed Adjoint of the Reflection on a Hilbert Space*; the graded-module version is *The Graded Adjoint Action on a Module over a Hilbert Space*.

Throughout, $H=H^0\oplus H^1$ is a $\mathbb{Z}/2$-graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with parity operator $\Gamma$ and grade involution $\alpha(T)=\Gamma T\Gamma$; the Hilbert–Schmidt form on $S_2(H)$ is $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$, and the adjoint is taken with respect to it. The two-sided operators are $L_{A}R_{B}(T)=ATB$ (unsigned) and $\mathcal{T}_{A,B}(T)=A\,\alpha(T)\,B$ (signed), and $A^*$ is the Hilbert adjoint.

## The Adjoint of the Unsigned Sandwich

**Theorem (the unsigned case).** For all $A,B\in B(H)$,

$$
(L_{A}R_{B})^*=L_{A^*}R_{B^*},
$$

so the adjoint of an unsigned sandwich is the unsigned sandwich of the adjoints, and the map $A\mapsto L_A$ together with $B\mapsto R_B$ gives a $*$-representation of $B(H)\times B(H)_{\mathrm{opp}}$.

*Proof.* $\langle L_{A}R_{B}X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(AXBY^*)=\operatorname{tr}(XA^*YB^*)=\langle X,A^*YB^*\rangle_{\mathrm{HS}}=\langle X,L_{A^*}R_{B^*}Y\rangle_{\mathrm{HS}}$, using the ciclicity of the trace; uniqueness of the adjoint gives the identity.

**Corollary (self-adjointness of the unsigned sandwich).** If $A$ and $B$ are self-adjoint then $L_{A}R_{B}$ is self-adjoint; conversely, if $A$ and $B$ are invertible, $L_{A}R_{B}$ is self-adjoint exactly when $A^*=kA$ and $B^*=k^{-1}B$ for a nonzero scalar $k$, the scalar expressing the ambiguity $L_{kA}R_{k^{-1}B}=L_{A}R_{B}$. In particular $L_{A}R_{B}$ is positive if $A$ and $B$ are positive, and $L_{A}R_{B}$ is an orthogonal projection exactly when $A$ and $B$ are orthogonal projections with $AB=I$.

*Proof.* The adjoint formula and the two-sided identity $L_{C}R_{D}=I\iff C,D$ reciprocal central show that $L_{A^*}R_{B^*}=L_{A}R_{B}$ is equivalent, for invertible parameters, to $A^*=kA$, $B^*=k^{-1}B$; positivity for self-adjoint positive $A,B$ is $\langle L_{A}R_{B}X,X\rangle_{\mathrm{HS}}=\operatorname{tr}(AXBX^*)\ge0$, and the projection statement is the idempotence $L_{A}R_{B}^2=L_{A^2}R_{B^2}$ together with positivity.

## The Adjoint of the Signed Sandwich

**Theorem (the signed case).** For all $A,B\in B(H)$,

$$
\boxed{\;(\mathcal{T}_{A,B})^*=\mathcal{T}_{\alpha(A^*),\,\alpha(B^*)}\;},
$$

and since $\alpha$ is a $*$-automorphism, $\alpha(A^*)=\alpha(A)^*$; the adjoint of the signed sandwich is the signed sandwich of the $\alpha$-adjoined parameters, so the signed sandwiches form a family closed under the adjunction.

*Proof.* $\langle \mathcal{T}_{A,B}X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(A\alpha(X)BY^*)=\operatorname{tr}(\alpha(X)BY^*A)=\operatorname{tr}(X\,\alpha(BY^*A))=\operatorname{tr}(X\,\alpha(B)\alpha(Y^*)\alpha(A))=\operatorname{tr}(X\,\alpha(A^*)\alpha(Y)\alpha(B^*))=\langle X,\mathcal{T}_{\alpha(A^*),\alpha(B^*)}Y\rangle_{\mathrm{HS}}$, using $\alpha(Y^*)=\alpha(Y)^*$, the ciclicity of the trace and the self-adjointness of the substitution $\alpha$ for the form.

**Corollary (compatibility with the composition table).** The adjunction is compatible with the products of the signed sandwich:

$$
(L_{A}R_{B}L_{C}R_{D})^*=(L_{AC}R_{DB})^*=L_{C^*A^*}R_{\,B^*D^*},
\qquad
(\mathcal{T}_{A,B}\mathcal{T}_{C,D})^*=(L_{A\alpha(C)}R_{\alpha(D)B})^*=L_{\alpha(C^*)\alpha(A^*)}R_{\,\alpha(B^*)\alpha(D^*)},
$$

both sides being the reversal of the order together with the adjunction of the parameters; the adjunction is therefore an anti-automorphism of the algebra generated by the two-sided operators, of order two.

*Proof.* Each identity is the product rule $(PQ)^*=Q^*P^*$ applied to the composition table of *The Signed Sandwich on a Hilbert Space*, with the adjoint formulas of the two theorems.

**Proposition (the sandwich adjoint and the one-sided adjoints).** Since $\mathcal{T}_{A,B}=L_A\varrho_B=\ell_AR_{\alpha(B)}$ and the one-sided adjoints are $L_A^*=L_{A^*}$, $R_B^*=R_{B^*}$, $\ell_A^*=\ell_{\alpha(A^*)}$ and $\varrho_B^*=\varrho_{\alpha(B^*)}$, the adjoint of the signed sandwich is also the composite

$$
(\mathcal{T}_{A,B})^*=(\ell_AR_{\alpha(B)})^*=R_{\alpha(B)}^*\ell_A^*=R_{\alpha(B^*)}\ell_{\alpha(A^*)},
$$

and $R_{\alpha(B^*)}\ell_{\alpha(A^*)}(X)=\alpha(A^*)\alpha(X)\alpha(B^*)$, which is the closed form; the two computations are the same identity read through the two decompositions of the sandwich.

*Proof.* The composite reverses the order of $\mathcal{T}_{A,B}=\ell_AR_{\alpha(B)}$; the one-sided adjoints are *The Adjoint of the Left Multiplication on a Hilbert Space* and its signed companion, $\alpha^*=\alpha$, and the evaluation is associativity together with the multiplicativity of $\alpha$.

## Self-Adjointness, Isometry and the Unitarity Condition

**Theorem (self-adjointness).** If $\alpha(A^*)=A$ and $\alpha(B^*)=B$ then the signed sandwich is self-adjoint, $(\mathcal{T}_{A,B})^*=\mathcal{T}_{A,B}$; conversely, if $A$ and $B$ are invertible, self-adjointness forces $\alpha(A^*)=kA$ and $\alpha(B^*)=k^{-1}B$ for a nonzero scalar $k$, the scalar expressing the ambiguity $\mathcal{T}_{kA,k^{-1}B}=\mathcal{T}_{A,B}$. In particular, if $A$ and $B$ are self-adjoint and even then $\mathcal{T}_{A,B}$ is self-adjoint.

*Proof.* The closed form $(\mathcal{T}_{A,B})^*=\mathcal{T}_{\alpha(A^*),\alpha(B^*)}$ gives the sufficiency; for the converse, equality of two signed sandwiches with invertible parameters forces the parameters to be reciprocal scalar multiples of one another, as in the unsigned case, and substituting the adjoint parameters gives the display; the last statement is $\alpha(A^*)=\alpha(A)^*=A^*=A$ for self-adjoint even $A$.

**Theorem (isometry).** The signed sandwich is an isometry of $S_2(H)$ if and only if

$$
\boxed{\;\alpha(A^*A)=\lambda I,\qquad \alpha(BB^*)=\lambda^{-1}I\;}
$$

for a nonzero scalar $\lambda$; when $A$ and $B$ are unitary the condition holds with $\lambda=1$, and the adjoint is an isometry with the reciprocal data.

*Proof.* By the composition table, $\mathcal{T}_{A,B}^*\mathcal{T}_{A,B}=\mathcal{T}_{\alpha(A^*),\alpha(B^*)}\mathcal{T}_{A,B}=L_{\alpha(A^*)\alpha(A)}R_{\,\alpha(B)\alpha(B^*)}=L_{\alpha(A^*A)}R_{\,\alpha(BB^*)}$; a two-sided operator $L_{C}R_{D}$ is the identity exactly when $C$ and $D$ are reciprocal central elements, since $CXD=X$ for all $X$ forces, at $X=I$, $CD=I$ and then $CX=XC$; substituting $C=\alpha(A^*A)$, $D=\alpha(BB^*)$ gives the condition. The next computation $\mathcal{T}_{A,B}\mathcal{T}_{A,B}^*=L_{AA^*}R_{\,B^*B}$ gives the co-isometry with the roles of the parameters exchanged, and unitarity is the two together.

**Theorem (the unitarity condition).** The signed sandwich $\mathcal{T}_{A,B}$ is unitary on $S_2(H)$ if and only if there are nonzero scalars $\lambda,\mu$ with

$$
\boxed{\;\alpha(A^*A)=\lambda I,\quad \alpha(BB^*)=\lambda^{-1}I,\quad AA^*=\mu I,\quad B^*B=\mu^{-1}I\;} ;
$$

in particular, if $A$ and $B$ are unitary then $\lambda=\mu=1$ and $\mathcal{T}_{A,B}$ is unitary, and conversely $\mathcal{T}_{A,B}$ unitary with $A$ and $B$ invertible makes the four general products central scalars, so each parameter is unitary up to a central scalar.

*Proof.* Unitarity is the isometry together with the co-isometry; the isometry gives $\alpha(A^*A)$ and $\alpha(BB^*)$ reciprocal central scalars, the co-isometry gives $AA^*$ and $B^*B$ reciprocal central scalars, and the two pairs give the display. Sufficiency for unitary $A,B$ is immediate since $A^*A=AA^*=I$ and the same for $B$; the converse reads the centrality off the two-sided identities.

**Corollary (the reflection case, flagged).** For $B=A^{-1}$ the sandwich is the reflection $\rho_A=\mathcal{T}_{A,A^{-1}}$, and the unitarity condition becomes the condition on $A$ alone; the adjoint $(\rho_A)^*=\mathcal{T}_{\alpha(A^*),\,\alpha((A^*)^{-1})}=\rho_{\alpha(A^*)}$ and the self-adjointness of the reflection are *The Signed Adjoint of the Reflection on a Hilbert Space*. The reflections themselves are *Reflections as Signed Two-Sided Operators on a Hilbert Space*.

## Examples and Computations

**Example (the finite-dimensional blocks).** For $H=\mathbb{K}^{p+q}$ with $\Gamma=\operatorname{diag}(I_p,-I_q)$ and matrices $A=\begin{pmatrix}A_0&A_1\\A_1'&A_0'\end{pmatrix}$, $B=\begin{pmatrix}B_0&B_1\\B_1'&B_0'\end{pmatrix}$ in even-odd block form, the sign enters only on the odd part of the argument, and the adjoint formula is the conjugate transposition of the blocks combined with the sign reversal of the odd blocks; the self-adjointness condition is that the even blocks be self-adjoint and the odd blocks be skew in the $\alpha$-signed sense.

**Proposition (the adjoint of the signed sandwich on rank-one operators).** On a rank-one operator the signed sandwich acts by $\mathcal{T}_{A,B}(\zeta\otimes\bar\eta)=A\,\alpha(\zeta\otimes\bar\eta)\,B$, with $\alpha(\zeta\otimes\bar\eta)=\Gamma\zeta\otimes\overline{\Gamma\eta}$, so the parity operator acts on both vectors; the pairing identity $\langle \mathcal{T}_{A,B}T,T'\rangle_{\mathrm{HS}}=\langle T,\mathcal{T}_{\alpha(A^*),\alpha(B^*)}T'\rangle_{\mathrm{HS}}$ is the rank-one form of the theorem, and it exhibits the two occurrences of the parity operator.

*Proof.* The action of the sandwich on a rank-one operator is associativity, $\alpha(\zeta\otimes\bar\eta)=\Gamma(\zeta\otimes\bar\eta)\Gamma$ is the conjugated rank-one operator with both vectors twisted by $\Gamma$, and the adjoint pairing is the trace of the product of two rank-one operators, as in *The Left and Right Multiplication Operators on a Hilbert Space*.

**Example (the sign is invisible at $\alpha=\mathrm{id}$).** When $H^1=0$ the grade involution is the identity, the signed and unsigned sandwiches agree, and the adjoint formula reduces to $(L_{A}R_{B})^*=L_{A^*}R_{B^*}$; the signed theory is the unsigned theory, and the unitarity condition is the plain unitarity of the two parameters.

## Summary

With respect to the Hilbert–Schmidt form, the unsigned sandwich $L_{A}R_{B}(T)=ATB$ has adjoint $L_{A^*}R_{B^*}$ and the signed sandwich $\mathcal{T}_{A,B}(T)=A\alpha(T)B$ has adjoint $\mathcal{T}_{\alpha(A^*),\alpha(B^*)}$, so both families are closed under adjunction and the adjunction is an anti-automorphism of the algebra they generate; when the grading is trivial the second formula reduces to the first. The adjoint of $\mathcal{T}_{A,B}$ is also the composite of the one-sided adjoints, $\alpha$ being self-adjoint for the form, and the two computations agree. The signed sandwich is self-adjoint exactly when $\alpha(A^*)=A$ and $\alpha(B^*)=B$; it is an isometry exactly when $\alpha(A^*A)$ and $\alpha(BB^*)$ are reciprocal central scalars; and it is unitary exactly when the additional conditions $AA^*=\lambda I$, $B^*B=\lambda^{-1}I$ hold, so that the unitarity of the sandwich is the unitarity of the parameters up to central scalars, and unitary parameters give a unitary sandwich. The reflection is the case $B=A^{-1}$, whose adjoint is $\rho_{\alpha(A^*)}$, and its self-adjointness is *The Signed Adjoint of the Reflection on a Hilbert Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$ | the Hilbert–Schmidt form |
| $L_{A}R_{B}(T)=ATB$ | the unsigned sandwich |
| $\mathcal{T}_{A,B}(T)=A\alpha(T)B$ | the signed sandwich |
| $(L_{A}R_{B})^*=L_{A^*}R_{B^*}$ | adjoint of the unsigned sandwich |
| $(\mathcal{T}_{A,B})^*=\mathcal{T}_{\alpha(A^*),\alpha(B^*)}$ | adjoint of the signed sandwich |
| $\alpha(A^*)=\alpha(A)^*$ | the involution commutes with the grade involution |
| $\mathcal{T}_{A,B}^*\mathcal{T}_{A,B}=L_{\alpha(A^*A)}R_{\alpha(BB^*)}$ | isometry condition |
| $\alpha(A^*A)=\lambda I$, $\alpha(BB^*)=\lambda^{-1}I$ | the isometry data |
| $(\rho_A)^*=\rho_{\alpha(A^*)}$ | the reflection case |
| $\alpha=\mathrm{id}\Leftrightarrow H^1=0$ | degenerate case, signed equals unsigned |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the two-sided operators and their adjoints.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the elementary operators and the trace identities.
- Barry Simon, *Trace Ideals and Their Applications*, Mathematical Surveys and Monographs 120 (American Mathematical Society, 2nd ed. 2005), for the Hilbert–Schmidt form and the rank-one computations.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the adjoints of elementary operators and the self-adjointness criteria.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the $*$-automorphisms and the anti-automorphisms of the adjunction.
