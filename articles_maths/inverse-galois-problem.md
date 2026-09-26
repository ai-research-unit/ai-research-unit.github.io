# __The Inverse Galois Problem__

## Introduction

Galois theory attaches to every finite Galois extension $L/K$ a finite group $\operatorname{Gal}(L/K)$, and the fundamental theorem of *Galois Theory* shows that the extension is determined by the group and the action. The inverse problem asks for the converse: given a finite group $G$ and a field $K$, is there a Galois extension of $K$ with group $G$? The question is a statement about a single field and a single group, and its answer depends sharply on $K$. Over a finite field only the cyclic groups occur, because the absolute Galois group of $\mathbb{F}_q$ is the profinite completion of $\mathbb{Z}$. Over the rational numbers every abelian group occurs by the Kronecker–Weber theorem, every finite solvable group occurs by Shafarevich's theorem, the symmetric and alternating groups occur, and whether every finite group occurs is open. Over a field of rational functions $\mathbb{C}(t)$, every finite group occurs.

The prominence of the problem comes from this last fact and from the tool that transfers it. The existence of extensions with prescribed group over $\mathbb{C}(t)$ is the algebraic form of the existence theorem for branched coverings of the projective line, and it is available in this corpus only as a statement, since the topological language needed to state and prove the existence theorem belongs to Part II. The transfer from $\mathbb{C}(t)$ or $\overline{\mathbb{Q}}(t)$ to $\mathbb{Q}$ is Hilbert's irreducibility theorem, which converts an extension of $\mathbb{Q}(t)$ into infinitely many extensions of $\mathbb{Q}$; it is the standard device, and the reason the problem over $\mathbb{Q}$ is studied through the problem over $\mathbb{Q}(t)$, which is called the **regular** inverse Galois problem.

This article states the problem, collects the classes of groups for which it is solved and the fields over which it is completely solved, and describes the two main methods — the rigidity method and the embedding problem with its cohomological obstruction — without developing the geometric existence theorem, which belongs to Part II. The arithmetic input is *Cyclotomic Fields*, *Galois Cohomology*, *Class Field Theory* and *Global Fields*; the rational-function side lies outside this article; and the rationality questions surrounding the Noether problem are *Invariant Theory*.

Throughout, $K$ is a field, $\bar K$ a separable closure, $G_K = \operatorname{Gal}(\bar K/K)$ the absolute Galois group, and for a finite group $G$ one says that $G$ **occurs over $K$** if there is a finite Galois extension $L/K$ with $\operatorname{Gal}(L/K) \cong G$. A group $G$ occurs **regularly** over $K$ if it occurs over $K(t)$ with the extension having no constant field extension, that is, with $\bar K \cap L = K$.

---

## The Problem and its Elementary Cases

### Statement

**Problem (inverse Galois problem).** Let $K$ be a field. For which finite groups $G$ does $G$ occur over $K$?

**Theorem (elementary cases).** Let $G$ be a finite group.

**(a)** Over an algebraically closed field only the trivial group occurs, and over a real closed field only the trivial group and $\mathbb{Z}/2\mathbb{Z}$ occur.

**(b)** Over a finite field $\mathbb{F}_q$ exactly the cyclic groups occur, of every order; equivalently, $\operatorname{Gal}(\bar{\mathbb{F}}_q/\mathbb{F}_q) = \hat{\mathbb{Z}}$.

**(c)** Over a field $K$ with absolute Galois group $G_K$ — the inverse limit of the finite Galois groups $\operatorname{Gal}(L/K)$ — a finite group $G$ occurs if and only if $G$ is a quotient of some finite Galois group $\operatorname{Gal}(L/K)$ of $K$, equivalently a finite quotient of $G_K$; consequently the problem is the problem of describing the finite quotients of $G_K$.

**Proof.** (a) An algebraically closed field has no nontrivial finite extension; a real closed field $K$ has, up to isomorphism, exactly one nontrivial finite extension, namely $K(\sqrt{-1})$, of degree $2$, so that its absolute Galois group is of order $2$. Both are standard: the first from the definition of algebraic closedness, the second from the fact that a real closed field has a unique ordering and every element of $K(\sqrt{-1})$ is a square or the negative of a square. (b) The absolute Galois group of $\mathbb{F}_q$ is $\hat{\mathbb{Z}} = \varprojlim_n\mathbb{Z}/n\mathbb{Z}$, whose finite quotients are the cyclic groups, by the Galois theory of *Finite Fields*; and every cyclic group is such a quotient. (c) is the Galois correspondence: intermediate Galois extensions correspond to the closed normal subgroups of $G_K$, so finite Galois extensions correspond to the quotients of $G_K$ by a closed normal subgroup of finite index. $\square$

**Example (explicit cyclic groups).** Over $\mathbb{Q}$ the group $\mathbb{Z}/n\mathbb{Z}$ occurs for every $n$, as $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) = (\mathbb{Z}/n\mathbb{Z})^\times$, which has $\mathbb{Z}/n\mathbb{Z}$ as a quotient, and the corresponding subfield is the fixed field of the kernel, by the Galois theory of *Cyclotomic Fields*. For $n = 3$ the smallest explicit example is the splitting field of $x^3-3x+1$: its discriminant is $-4(-3)^3-27(1)^2 = 108-27 = 81 = 9^2$, a square, so the Galois group lies in $A_3 = \mathbb{Z}/3\mathbb{Z}$; the polynomial has no rational root, since $f(1) = -1$ and $f(-1) = 3$, so it is irreducible of degree $3$ and the group is $\mathbb{Z}/3\mathbb{Z}$. Its splitting field is the real subfield of $\mathbb{Q}(\zeta_9)$, of degree $\varphi(9)/2 = 3$ over $\mathbb{Q}$.

**Example ($S_n$ and $A_n$).** For every $n$ the symmetric group $S_n$ occurs over $\mathbb{Q}$: the general polynomial $T^n-s_1T^{n-1}+\cdots+(-1)^ns_n$ over the field $\mathbb{Q}(s_1,\ldots,s_n)$ of symmetric functions has splitting field of group $S_n$ by the fundamental theorem of symmetric polynomials, and Hilbert's irreducibility theorem below specialises this to ordinary polynomials over $\mathbb{Q}$; explicitly, Selmer's polynomial $x^n-x-1$ is irreducible over $\mathbb{Q}$ with Galois group $S_n$ for every $n$. The alternating group $A_n$ occurs for $n \geq 3$ by the same construction applied to the fixed field of $A_n$ in the splitting field over $\mathbb{Q}(s_1,\ldots,s_n)$, together with the multivariable form of Hilbert's irreducibility theorem; equivalently, it is the Galois group of an irreducible polynomial over $\mathbb{Q}$ whose discriminant is a square, such as $x^3-3x+1$ in degree $3$.

**Example.** The dihedral group $D_4$ of order $8$ occurs over $\mathbb{Q}$ as the Galois group of the splitting field of $x^4-2$: the splitting field is $\mathbb{Q}(\sqrt[4]{2},i)$, of degree $8$ over $\mathbb{Q}$, and the Galois action sends $\sqrt[4]{2}$ to $\pm\sqrt[4]{2}$ or $\pm i\sqrt[4]{2}$ and $i$ to $\pm i$, so the group is the semidirect product $(\mathbb{Z}/4\mathbb{Z})\rtimes(\mathbb{Z}/2\mathbb{Z})$ in which the nontrivial element of the second factor acts by inversion, that is, $D_4$.

### Hilbert's Irreducibility Theorem

**Theorem (Hilbert irreducibility).** Let $f(t,x) \in \mathbb{Q}[t,x]$ be irreducible as a polynomial in $x$ over $\mathbb{Q}(t)$. Then there are infinitely many rational values $t_0 \in \mathbb{Q}$ such that $f(t_0,x)$ is irreducible over $\mathbb{Q}$; more precisely, the set of such $t_0$ has complement of density zero among the rationals in any bounded interval. More generally, for a finite Galois extension $L/\mathbb{Q}(t)$ with group $G$, the set of specialisations $t_0$ for which the specialised extension has group $G$ (rather than a proper subgroup) is infinite.

**Proof sketch.** The proof is by counting: one bounds the number of rational points of height at most $H$ that lie on the algebraic set cut out by the condition that a root lie in a proper subfield, and shows this is $o(H)$; the estimates are those of *Global Fields* for the places of $\mathbb{Q}$. The full proof belongs to the arithmetic of global fields and is not reproduced here. $\square$

**Corollary.** If $G$ occurs regularly over $\mathbb{Q}$, then $G$ occurs over $\mathbb{Q}$.

**Proof.** Take a Galois extension $L/\mathbb{Q}(t)$ with group $G$ and no constant field extension, and specialise $t$ by Hilbert irreducibility; the specialised extension of $\mathbb{Q}$ has group $G$ because the group of the specialisation can only shrink, and it does not shrink for infinitely many $t_0$. $\square$

---

## What is Known

### Shafarevich's Theorem and Solvable Groups

**Theorem (Shafarevich).** Every finite solvable group occurs over $\mathbb{Q}$.

**Proof sketch.** The proof proceeds by induction on the order of the group through the **embedding problem**: given a Galois extension $L/\mathbb{Q}$ with group $\bar G$ and a surjection $G \to \bar G$ with kernel $A$, does there exist a Galois extension with group $G$ containing $L$? The obstructions lie in the cohomology of $A$, in the spirit of *Galois Cohomology*, and for solvable $A$ the obstruction theory, together with the theorem of Grunwald and Wang on the realisation of prescribed cyclic extensions and the Scholz–Reichardt theorem on the embedding of cyclic extensions of degree $p$ in extensions of degree $p^2$, controls the successive steps. For a nilpotent group the argument reduces to the case of $p$-groups and to the Frattini-quotient induction. $\square$

**Corollary.** Every abelian group, and every nilpotent group, occurs over $\mathbb{Q}$.

**Example.** For $p = 2$ the group $(\mathbb{Z}/2\mathbb{Z})^k$ occurs for every $k$ over $\mathbb{Q}$, as the Galois group of the extension generated by the square roots of $k$ independent squarefree rational numbers; the group of order $p$ occurs as $\operatorname{Gal}(\mathbb{Q}(\zeta_p)/\mathbb{Q})$'s quotient of order $p$, and the nonabelian group of order $21$, being solvable, occurs by Shafarevich's theorem although writing an explicit polynomial for it requires the embedding theory.

### The Rigidity Method

**Definition.** Let $G$ be a finite group and $\mathbf{C} = (C_1,\ldots,C_r)$ a tuple of conjugacy classes of $G$, with $C_i \neq 1$. For each $i$ choose $\sigma_i \in C_i$, and suppose that $\sigma_1\cdots\sigma_r = 1$ and $\langle\sigma_1,\ldots,\sigma_r\rangle = G$. Writing $n_i$ for the order of the centraliser of $\sigma_i$ in $G$, the tuple is **rigid** if

$$
\#\{(\tau_1,\ldots,\tau_r) : \tau_i \in C_i,\ \tau_1\cdots\tau_r = 1,\ \langle\tau_i\rangle = G\} = \frac{\lvert G\rvert}{n_1n_2\cdots n_r},
$$

that is, if the natural upper bound given by the character theory of $G$ is attained.

**Theorem (rigidity, Shafarevich, Fried–Völklein).** Let $G$ be a finite group with a rational rigid tuple of conjugacy classes, that is, a rigid tuple whose classes are stable under the action of the Galois group of $\mathbb{Q}$ on the character values. Then $G$ occurs regularly over $\mathbb{Q}$, hence occurs over $\mathbb{Q}$.

**Proof sketch.** The tuple gives a cover of the projective line branched over $r$ specified points, with group $G$; rigidity makes the cover rigid, that is, unique, so the branched covering is defined over $\mathbb{Q}$ rather than over an extension, and the moduli count identifies the field of definition. The argument is a count of Hurwitz numbers: the number of covers with given branch data is the coefficient in the class algebra of $\mathbb{Z}[G]$, and rigidity is the statement that this coefficient equals the expected one, forcing the cover to be unique and hence rational. The existence of the cover itself over $\mathbb{C}(t)$ is the existence theorem for branched coverings, whose statement is deferred to Part II. $\square$

**Example.** The method applies to the symmetric groups and to many simple groups. The Mathieu group $M_{11}$ of order $7920$ is known to occur over $\mathbb{Q}$ by a rigidity computation, and the Monster has been shown to occur over $\mathbb{Q}$ by the same circle of ideas; the group $\operatorname{PSL}(2,p)$ occurs for those primes $p$ that satisfy Shih's congruence conditions, and the Frobenius group of order $20$ arises from a rational rigid tuple of three classes. The method is the standard route to the occurrence of the large simple groups over $\mathbb{Q}$.

### The Regular Problem over $\mathbb{Q}(t)$ and over $\mathbb{C}(t)$

**Theorem (existence over a rational function field).** Over $\mathbb{C}(t)$ every finite group occurs, and over $\overline{\mathbb{Q}}(t)$ every finite group occurs; these are the algebraic forms of the existence theorem for branched coverings of the projective line, whose proof uses the topology of the sphere and the fundamental group and therefore belongs to Part II, where the topological language is available. Over $\mathbb{Q}(t)$, the regularity of the construction can be arranged when the branch points are rational, which is the content of the rigidity theorem above.

**Theorem (Ax).** Let $K$ be a field such that every nonempty variety over $K$ has a $K$-rational point, a **PAC field**. Then the absolute Galois group $G_K$ is projective: every embedding problem over $K$ with finite kernel admits a solution. Consequently no cohomological obstruction blocks the inverse Galois problem over such a field, and over PAC fields with large absolute Galois group every finite group occurs; the precise structural statement belongs to the arithmetic of fields and is recorded here as the sharpest contrast with the situation over $\mathbb{Q}$.

**Proof sketch.** The obstruction to an embedding problem is a class in the second cohomology of the kernel, and the class vanishes as soon as a certain algebraic variety — the variety of solutions of the problem, called the obstruction variety — has a rational point; the class is computed as the obstruction attached to that variety, and PAC gives the rational point. The argument is a computation in the cohomology of *Galois Cohomology* together with the rational-point property that defines PAC. $\square$

**Theorem (fields of small Galois group).** Over a finite field the occurring groups are exactly the cyclic ones; over a field with trivial absolute Galois group, only the trivial group; over a real closed field, only the trivial group and the group of order $2$. Over the algebraic closure of a finite field, again only the trivial group.

---

## The Embedding Problem

### Formulation

**Definition.** Let $L/K$ be a finite Galois extension with group $\bar G$ and let $1 \to A \to G \to \bar G \to 1$ be an exact sequence of finite groups. The **embedding problem** attached to this data asks whether there is a finite Galois extension $M/K$ containing $L$ with $\operatorname{Gal}(M/K) \cong G$, compatibly with the surjection on the group and the inclusion of fields. The problem is **split** if the sequence splits, and it is **Frattini** if $A$ lies in the Frattini subgroup of $G$.

**Theorem (obstruction).** Let $L/K$ be a Galois extension with group $\bar G$ and let $A$ be a finite $\bar G$-module (in the application, a finite abelian group with the action of $\bar G$). The obstruction to a compatible solution of the embedding problem with abelian kernel $A$ is a class

$$
\operatorname{ob} \in H^2(\bar G, A),
$$

which vanishes exactly when a solution exists; the classes in $H^2(G_K,A)$ classifying such problems are the cohomology classes of *Galois Cohomology*, and the vanishing of the obstruction is the statement in *Galois Cohomology* that the extension of modules splits compatibly with the homomorphism.

**Proof sketch.** A solution gives a splitting of the sequence over $\bar G$ compatible with the Galois action, and the difference of two solutions is a crossed homomorphism, hence a class in $H^1$; the obstruction is the coboundary of the cohomology class of the extension, and the standard computation in the group cohomology of *Galois Cohomology* gives the exactness needed. $\square$

**Theorem (Grunwald–Wang).** Let $K$ be a number field, $S$ a finite set of places of $K$ and, for each $v \in S$, a finite Galois extension of the completion $K_v$; then there is a global Galois extension of $K$ inducing the prescribed extension at every $v \in S$, except in the single exceptional case identified by Wang, concerning the cyclic extensions of degree $8$ over a field containing $\sqrt{-1}$ and with prescribed local behaviour at the places over $2$. The theorem is the technical heart of Shafarevich's proof, and the completions $K_v$ and the local fields involved belong to Part II, where they are constructed; the statement is recorded here for its role in the induction.

**Example (an embedding problem).** Let $L = \mathbb{Q}(\sqrt{2})$ and let $G$ be the dihedral group of order $8$, with kernel $A = \mathbb{Z}/4\mathbb{Z}$ mapping onto $\bar G = \mathbb{Z}/2\mathbb{Z}$. A solution is given by the splitting field of $x^4-2$, which contains $\mathbb{Q}(\sqrt2)$ and has group $D_4$, as exhibited above; concretely the extension $M/\mathbb{Q}$ with $\operatorname{Gal}(M/\mathbb{Q}) = D_4$ restricts to the given quadratic field. The example illustrates the pattern of the induction: each step embeds a known extension in a larger one.

### Relation to the Noether Problem

**Remark.** Let a finite group $G$ act faithfully on $\mathbb{Q}(x_1,\ldots,x_n)$ through a faithful linear representation, and consider the fixed field $\mathbb{Q}(x_1,\ldots,x_n)^G$, the invariant field of *Invariant Theory*. If this field is purely transcendental over $\mathbb{Q}$, then $G$ occurs over $\mathbb{Q}$, since the splitting field of a generic polynomial for the action has group $G$; this is the Noether problem in the direction of the inverse Galois problem. The converse fails, and the groups for which the fixed field is not rational — the counterexamples of Swan and Saltman — show that the Noether problem is strictly stronger. The two problems are linked by the same rationality question, and both are open in general.

---

## Summary

The inverse Galois problem asks which finite groups occur as Galois groups over a given field $K$; equivalently, which finite groups are quotients of the finite Galois groups of $K$, that is, the finite quotients of the absolute Galois group $G_K$. Over an algebraically closed field only the trivial group occurs, over a real closed field only the trivial group and $\mathbb{Z}/2\mathbb{Z}$, and over a finite field exactly the cyclic groups, because the absolute Galois group of $\mathbb{F}_q$ is $\hat{\mathbb{Z}}$. Over $\mathbb{Q}$ every cyclic group occurs through the cyclotomic fields, with $x^3-3x+1$ realising $\mathbb{Z}/3\mathbb{Z}$ with discriminant $81 = 9^2$; every finite solvable group occurs by Shafarevich's theorem, whose proof embeds extensions step by step using the Grunwald–Wang theorem and the Scholz–Reichardt theorem; every symmetric and alternating group occurs, through the general polynomial and Hilbert's irreducibility theorem, with Selmer's $x^n-x-1$ an explicit witness; and the dihedral group $D_4$ occurs as the group of $x^4-2$. Whether every finite group occurs over $\mathbb{Q}$ is open.

Over $\mathbb{C}(t)$ and over $\overline{\mathbb{Q}}(t)$ every finite group occurs, by the existence theorem for branched coverings of the projective line, whose statement belongs here and whose proof belongs to Part II; Hilbert's irreducibility theorem transfers a regular occurrence over $\mathbb{Q}(t)$ to an occurrence over $\mathbb{Q}$, so that the regular problem over $\mathbb{Q}(t)$ controls the problem over $\mathbb{Q}$. The rigidity method produces regular occurrences for groups carrying a rational rigid tuple of conjugacy classes, which covers many simple and sporadic groups including the Mathieu groups and the Monster. The embedding problem asks whether an extension with group $\bar G$ can be embedded in one with group $G$ when $A$ is the kernel of $G \to \bar G$; its obstruction is a class in $H^2(\bar G,A)$, and its solution theory is the cohomological content of *Galois Cohomology*. Over PAC fields every finite group occurs and the absolute Galois group is projective. The Noether problem, whether the invariant field $\mathbb{Q}(x_1,\ldots,x_n)^G$ is rational, implies the occurrence of $G$ but is strictly stronger, and it is treated in *Invariant Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $\bar K$ | Field, separable closure |
| $G_K$ | Absolute Galois group $\operatorname{Gal}(\bar K/K)$ |
| $G$, $\bar G$, $A$ | Finite group, its quotient, the kernel |
| $L/K$ | A Galois extension |
| $\mathbf{C} = (C_1,\ldots,C_r)$ | A tuple of conjugacy classes |
| $\sigma_i$, $n_i$ | Representatives and centraliser orders |
| $D_4$ | Dihedral group of order $8$ |
| $\zeta_n$ | Primitive $n$-th root of unity |
| $\mathbb{F}_q$, $\hat{\mathbb{Z}}$ | Finite field and its absolute Galois group |
| $H^2(\bar G,A)$ | Obstruction group of the embedding problem |
| PAC | Pseudo-algebraically-closed field |





## Further Reading

- David Hilbert, "Über die Irreduzibilität ganzer rationaler Functionen mit ganzzahligen Coefficienten", *Journal für die reine und angewandte Mathematik* 110 (1892), 104–129, for the irreducibility theorem.
- I. R. Shafarevich, "Construction of fields of algebraic numbers with given solvable Galois group", *Izv. Akad. Nauk SSSR Ser. Mat.* 18 (1954), 525–578, for the solvable case.
- Jean-Pierre Serre, *Topics in Galois Theory* (Jones and Bartlett, 1992), for the regular problem, the rigidity method and the relation to rationality questions.
- Helmut Völklein, *Groups as Galois Groups: An Introduction* (Cambridge University Press, 1996), for the rigidity method and Hurwitz spaces.
- Gunter Malle and B. Heinrich Matzat, *Inverse Galois Theory* (Springer, 2nd ed. 2018), for the complete account of the methods and the known cases.
- Ernst Selmer, "The irreducibility of $x^n-x-1$", *Mathematica Scandinavica* 4 (1956), 287–302, for the explicit polynomials with symmetric group.
- Michael D. Fried and Moshe Jarden, *Field Arithmetic* (Springer, 3rd ed. 2008), for PAC fields, Hilbertian fields and the structure of absolute Galois groups.
- Jean-Pierre Serre, *Cohomologie galoisienne* (Springer, 5th ed. 1994), for the embedding problem and its cohomological obstruction.
