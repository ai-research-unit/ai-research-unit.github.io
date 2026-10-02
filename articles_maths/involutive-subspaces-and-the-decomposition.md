# __Involutive Subspaces and the Decomposition__

## Introduction

An involution of a linear space singles out the subspaces it preserves, and their structure is completely determined by the decomposition $V = V_+ \oplus V_-$ into its fixed and negated parts: a subspace is preserved exactly when it is the direct sum of a subspace of $V_+$ and a subspace of $V_-$, and the preserved subspaces therefore form a lattice isomorphic to the product of the lattices of subspaces of the two parts. This article develops that correspondence, the induced involution on a preserved subspace and on a quotient, the projectors that compute the decomposition, and the special case of a reflection, whose preserved subspaces are those lying inside its fixed hyperplane or containing its negated line.

*Involutive Linear Spaces* constructs the decomposition, the type and the projectors, and classifies the involutions by their type; the present article is the companion in the same `*`-theory group and it owns the subspaces: the stable ones, their lattice, and the induced involutions. The involution induced on the dual of a stable subspace and on a quotient through annihilators is *Involutions of the Dual Space*; the graded reading of the same decomposition is *Involutions of a Graded Linear Space*; the pairing-based adjoint, the unitary elements and the operator adjoints are the `*`-operator group. The forms are Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, and $T$ is a linear involution of $V$ of type $(p,q)$, so that $V = V_+ \oplus V_-$, $V_+ = \ker(T-\mathrm{id})$ has dimension $p$ and $V_- = \ker(T+\mathrm{id})$ has dimension $q$. No form, no norm and no topology is used.

## Stable Subspaces

**Definition.** A subspace $U \subseteq V$ is **stable** under $T$ when $T(U) \subseteq U$; equivalently, since $T$ is bijective, when $T(U) = U$.

**Proposition (stable subspaces are the pairs).** A subspace $U$ is stable under $T$ if and only if

$$
U = (U \cap V_+) \oplus (U \cap V_-) ,
$$

and the assignment $U \mapsto (U \cap V_+, U \cap V_-)$ is a bijection between the stable subspaces of $V$ and the pairs of subspaces $(U_+,U_-)$ with $U_+ \subseteq V_+$ and $U_- \subseteq V_-$; the inverse is $(U_+,U_-) \mapsto U_+ \oplus U_-$. Under this bijection the lattice of stable subspaces is isomorphic to the product of the lattices of subspaces of $V_+$ and of $V_-$.

**Proof.** If $U$ is stable and $u \in U$, write $u = u_+ + u_-$ with $u_\pm \in V_\pm$; then $Tu = u_+ - u_- \in U$, so $u_+ = \tfrac12(u+Tu)$ and $u_- = \tfrac12(u-Tu)$ lie in $U$, whence $u_\pm \in U \cap V_\pm$ and the sum is direct. Conversely, a sum $U_+ \oplus U_-$ with $U_\pm \subseteq V_\pm$ is stable because $T$ is the identity on $U_+$ and minus the identity on $U_-$. Intersections and sums are computed componentwise, so the lattices are isomorphic to the product of the two subspace lattices.

**Corollary (the type of a stable subspace).** For a stable $U$ the restriction $T|_U$ is a linear involution of $U$ of type $(\dim_F(U\cap V_+), \dim_F(U\cap V_-))$, and the quotient $V/U$ carries the induced involution $T_{V/U}$ of type $(p-\dim_F(U\cap V_+), q-\dim_F(U\cap V_-))$.

**Proof.** The restriction fixes $U\cap V_+$ and negates $U\cap V_-$, and these are its eigenspaces in $U$; on the quotient the involution is well defined because $U$ is stable, and its eigenspaces are the images of $V_+$ and $V_-$, of the stated dimensions.

**Example.** For $T = \operatorname{diag}(1,-1)$ on $F^2$ with $V_+ = Fe_1$ and $V_- = Fe_2$, the stable subspaces are $0$, $V_+$, $V_-$ and $V$, and the lattice is the product of the two two-element chains; there are no others, and the two lines $F(e_1+e_2)$ and $F(e_1-e_2)$ are not stable.

## The Projectors

**Definition.** The **projectors** of the involution are

$$
P_+ = \tfrac12(\mathrm{id}_V + T), \qquad P_- = \tfrac12(\mathrm{id}_V - T) .
$$

**Proposition.** $P_+$ and $P_-$ are idempotent endomorphisms with $P_+ + P_- = \mathrm{id}_V$, $P_+P_- = P_-P_+ = 0$, and $T = P_+ - P_-$; they commute with $T$ and with every endomorphism commuting with $T$; a subspace $U$ is stable under $T$ if and only if it is preserved by both projectors, $P_\pm(U) \subseteq U$.

**Proof.** The idempotence and the relations are $P_\pm^2 = \tfrac14(\mathrm{id} \pm 2T + T^2) = P_\pm$ and $P_+P_- = \tfrac14(\mathrm{id}-T^2) = 0$; the sum is the identity and the difference is $T$. Commutation with $T$ is $TP_\pm = \tfrac12(T \pm \mathrm{id}) = \pm P_\pm$, and a map commuting with $T$ commutes with $\mathrm{id}\pm T$, hence with the projectors. If $P_\pm(U)\subseteq U$ then $T = P_+ - P_-$ preserves $U$; conversely if $T$ preserves $U$ then $U$ decomposes as $U\cap V_+ \oplus U\cap V_-$ and the projectors are the projections onto the two parts, so they preserve $U$.

**Corollary (the decomposition is canonical).** The decomposition $V = V_+ \oplus V_-$ is the eigenspace decomposition of $T$, and it is recovered from $T$ alone; the two parts are the images of $P_+$ and $P_-$, $\operatorname{im}P_\pm = V_\pm$ and $\ker P_\pm = V_\mp$.

## Reflections

**Definition.** A **reflection** of $V$ is a linear involution of type $(n-1,1)$; its fixed hyperplane is $V_+$ and its negated line is $V_-$.

**Proposition.** A reflection is determined by its fixed hyperplane together with a nonzero vector spanning the negated line, and over a field with $2 \neq 0$ it is determined by the hyperplane together with the requirement that it negate exactly one line; the stable subspaces of a reflection are exactly the subspaces contained in the fixed hyperplane together with the subspaces containing the negated line, and the two families meet at the subspaces of the hyperplane that contain the line.

**Proof.** A reflection of type $(n-1,1)$ fixes $V_+$ pointwise and negates $V_-$ pointwise, so it is determined by the pair $(V_+,V_-)$ with $V = V_+\oplus V_-$; a hyperplane and a complementary line give such a pair, and the requirement of type $(n-1,1)$ fixes the dimension of the negated part. Stability is the pair description of the previous section: a subspace $U$ is stable when $U = (U\cap V_+)\oplus(U\cap V_-)$, which happens exactly when either $U \subseteq V_+$ (the second part is $0$) or $V_- \subseteq U$ (the second part is all of $V_-$) or both; the intersection of the two families is the set of subspaces containing $V_-$ and contained in $V_+$, which is empty unless the point $V_-$ lies in $V_+$, that is unless $V_- = 0$.

**Remark (reflection needs no form).** The definition uses only the type, not a bilinear pairing: an involution of type $(n-1,1)$ is what a reflection is, and the orthogonal reflection of a space with a form is the special reflection that also preserves the form. The form, the norm and the isometry it defines are Part II, and *Hilbert Algebras* owns them; the reflections as signed two-sided operators of the operator group use only the type fixed here.

## Summary

For a linear involution $T$ of a finite-dimensional space $V$ of type $(p,q)$, a subspace is stable under $T$ exactly when it is the direct sum of a subspace of $V_+$ and a subspace of $V_-$, and the stable subspaces form a lattice isomorphic to the product of the subspace lattices of the two parts; the restriction of $T$ to a stable subspace has the type given by the two components, and the induced involution on the quotient has the complementary type. The projectors $P_\pm = \tfrac12(\mathrm{id}\pm T)$ are idempotent, sum to the identity, satisfy $P_+P_-=0$ and recover $T = P_+-P_-$, and a subspace is stable exactly when both preserve it. A reflection is an involution of type $(n-1,1)$, determined by its fixed hyperplane together with the negated line, and its stable subspaces are those contained in the hyperplane together with those containing the negated line; the definition uses no form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the field of scalars, of characteristic not two |
| $V$, $n$ | the space and its dimension |
| $T$ | a linear involution, $T^2=\mathrm{id}_V$, of type $(p,q)$ |
| $V_+=\ker(T-\mathrm{id})$, $V_-=\ker(T+\mathrm{id})$ | fixed and negated parts |
| $P_\pm = \tfrac12(\mathrm{id}\pm T)$ | the projectors |
| $U$ stable | $T(U)\subseteq U$, equivalently $U=(U\cap V_+)\oplus(U\cap V_-)$ |
| $T|_U$, $T_{V/U}$ | the induced involutions on a stable subspace and a quotient |
| reflection | a linear involution of type $(n-1,1)$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, eigenspace decompositions and stable subspaces.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for projections, direct-sum decompositions and reflections.
- Nathan Jacobson, *Lectures in Abstract Algebra*, volume II: *Linear Algebra* (Van Nostrand, 1953), for involutions and their invariant subspaces.
- Steven Roman, *Advanced Linear Algebra* (Springer, 3rd ed. 2008), for the lattice of invariant subspaces of a diagonalisable operator.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections and their fixed hyperplanes.
